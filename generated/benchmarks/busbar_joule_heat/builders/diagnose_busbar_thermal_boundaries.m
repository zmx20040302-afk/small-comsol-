builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
mphstart('localhost', 2037);

model = mphopen(fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
convection_selection = mphgetselection(model.component('comp1').physics('ht').feature('hf1'));
convection_boundaries = convection_selection.entities';
terminal_boundaries = [8 15 43];
all_boundaries = 1:43;

joule_power_w = mphint2(model, 'ec.Qh', 3);
convection_flux_w = mphint2(model, 'ht.nteflux', 2, 'selection', convection_boundaries);
terminal_flux_w = mphint2(model, 'ht.nteflux', 2, 'selection', terminal_boundaries);
all_flux_w = mphint2(model, 'ht.nteflux', 2, 'selection', all_boundaries);

result = table(joule_power_w, convection_flux_w, terminal_flux_w, all_flux_w);
writetable(result, fullfile(builder_dir, 'busbar_thermal_boundary_diagnosis.csv'));
disp(result);
