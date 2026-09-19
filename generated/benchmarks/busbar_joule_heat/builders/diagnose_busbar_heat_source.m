builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
mphstart('localhost', 2037);

model = mphopen(fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
convection_selection = mphgetselection(model.component('comp1').physics('ht').feature('hf1'));
convection_boundaries = convection_selection.entities';

expressions = ["ec.Qh"; "ht.Q"; "emh1.Qh"; "emh1.Q"; "ht.Qext"];
locations = ["domain"; "domain"; "domain"; "domain"; "domain"];
values = nan(size(expressions));
status = strings(size(expressions));

for index = 1:numel(expressions)
  try
    values(index) = mphint2(model, char(expressions(index)), 3);
    status(index) = "ok";
  catch errorInfo
    status(index) = string(errorInfo.message);
  end
end

explicit_convection_w = mphint2(model, 'htc*(T-T_amb)', 2, 'selection', convection_boundaries);
normal_total_flux_w = mphint2(model, 'ht.nteflux', 2, 'selection', convection_boundaries);

source_result = table(expressions, locations, values, status);
writetable(source_result, fullfile(builder_dir, 'busbar_heat_source_diagnosis.csv'));
boundary_count = numel(convection_boundaries);
boundary_result = table(boundary_count, explicit_convection_w, normal_total_flux_w);
writetable(boundary_result, fullfile(builder_dir, 'busbar_convection_expression_diagnosis.csv'));
disp(source_result);
disp(boundary_result);
