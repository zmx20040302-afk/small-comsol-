builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
mphstart('localhost', 2037);

model = mphopen(fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
convection_properties = mphgetproperties(model.component('comp1').physics('ht').feature('hf1'), 'returnstrings', 'on', 'showsel', 'on');
solver_properties = mphgetproperties(model.sol('sol1'), 'returnstrings', 'on');

save(fullfile(builder_dir, 'busbar_solver_and_convection_properties.mat'), 'convection_properties', 'solver_properties');
disp(convection_properties);
disp(solver_properties);
