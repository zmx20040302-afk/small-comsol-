builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
mphstart('localhost', 2037);

model = mphopen(fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
potential_boundary = 43;
convection_selection = mphgetselection(model.component('comp1').physics('ht').feature('hf1'));
convection_boundaries = convection_selection.entities';

joule_power_w = mphint2(model, 'ec.Qh', 3);
current_a = nan;
current_expression = "";
for expression = ["ec.nJ", "ec.Jx*nx+ec.Jy*ny+ec.Jz*nz"]
  try
    current_a = mphint2(model, char(expression), 2, 'selection', potential_boundary);
    current_expression = expression;
    break;
  catch
  end
end

voltage_v = 20e-3;
electrical_input_w = abs(voltage_v * current_a);
heat_flux_w = mphint2(model, 'ht.nteflux', 2, 'selection', convection_boundaries);
outward_convection_w = abs(heat_flux_w);
electrical_to_joule_percent = abs(electrical_input_w-joule_power_w)/joule_power_w*100;
joule_to_convection_percent = abs(joule_power_w-outward_convection_w)/joule_power_w*100;

result = table(current_a, electrical_input_w, joule_power_w, heat_flux_w, outward_convection_w, electrical_to_joule_percent, joule_to_convection_percent, current_expression);
writetable(result, fullfile(builder_dir, 'busbar_energy_balance_refined.csv'));
disp(result);
