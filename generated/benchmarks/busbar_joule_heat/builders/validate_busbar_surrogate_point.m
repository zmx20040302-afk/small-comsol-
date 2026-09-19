builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
server_host = getenv('COMSOL_MPH_HOST');
if isempty(server_host), server_host = 'localhost'; end
server_port = str2double(getenv('COMSOL_MPH_PORT'));
if isnan(server_port), server_port = 2036; end
mphstart(server_host, server_port);

model = mphopen(fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
model.param.set('Vtot', '25[mV]');
model.param.set('htc', '7[W/(m^2*K)]');
model.study('std1').run;

tmax_k = mphmax(model, 'T', 3);
result = table(25, 7, tmax_k, tmax_k-273.15, ...
  'VariableNames', {'Vtot_mV', 'htc_W_m2K', 'Tmax_K', 'Tmax_C'});
writetable(result, fullfile(builder_dir, 'busbar_surrogate_holdout_comsol.csv'));
disp(result);
