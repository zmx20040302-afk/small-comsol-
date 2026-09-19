builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
mphstart('localhost', 2037);

model = mphopen(fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
convection_selection = mphgetselection(model.component('comp1').physics('ht').feature('hf1'));
convection_boundaries = convection_selection.entities';

joule_power_w = mphint2(model, 'ec.Qh', 3);
convection_power_w = nan;
convection_expression = "";
status = "completed";

for expression = ["ht.nteflux", "ht.tflux"]
  try
    convection_power_w = mphint2(model, char(expression), 2, 'selection', convection_boundaries);
    convection_expression = expression;
    break;
  catch ME
    status = "convection expression unavailable: " + string(ME.message);
  end
end

if ~isnan(convection_power_w)
  convection_power_w = abs(convection_power_w);
  relative_imbalance_percent = abs(joule_power_w - convection_power_w) / joule_power_w * 100;
else
  relative_imbalance_percent = nan;
end

result = table(joule_power_w, convection_power_w, relative_imbalance_percent, convection_expression, status);
writetable(result, fullfile(builder_dir, 'busbar_energy_balance.csv'));
disp(result);
