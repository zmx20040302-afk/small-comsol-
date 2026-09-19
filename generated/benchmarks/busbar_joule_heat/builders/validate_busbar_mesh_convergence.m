builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
mphstart('localhost', 2037);

mesh_sizes = {'4[mm]', '3[mm]', '2[mm]'};
temperature_max = nan(numel(mesh_sizes), 1);
joule_power = nan(numel(mesh_sizes), 1);
status = strings(numel(mesh_sizes), 1);

for index = 1:numel(mesh_sizes)
  try
    model = busbar_joule_heat_baseline();
    model.param.set('mh', mesh_sizes{index});
    model.component('comp1').mesh('mesh1').clearMesh;
    model.component('comp1').mesh('mesh1').run;
    model.sol('sol1').runAll;
    temperature_max(index) = mphmax(model, 'T', 3);
    try
      joule_power(index) = mphint2(model, 'ec.Qh', 3);
    catch
      % Keep NaN when this COMSOL version exposes a different loss variable.
    end
    status(index) = "completed";
  catch ME
    status(index) = "failed: " + string(ME.message);
  end
end

result = table(string(mesh_sizes)', temperature_max, joule_power, status, ...
  'VariableNames', {'mesh_size', 'Tmax_K', 'Joule_power_W', 'status'});
writetable(result, fullfile(builder_dir, 'busbar_mesh_convergence.csv'));
disp(result);

valid = temperature_max(~isnan(temperature_max));
if numel(valid) >= 2
  relative_change = abs(valid(end) - valid(end-1)) / valid(end) * 100;
  fprintf('MESH_TMAX_RELATIVE_CHANGE_PERCENT=%.6f\n', relative_change);
end
