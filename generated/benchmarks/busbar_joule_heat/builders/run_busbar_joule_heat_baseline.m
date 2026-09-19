try
  builder_dir = fileparts(mfilename('fullpath'));
  addpath(builder_dir);
  addpath('D:/COMSOL64/Multiphysics/mli');
  server_host = getenv('COMSOL_MPH_HOST');
  if isempty(server_host), server_host = 'localhost'; end
  server_port = str2double(getenv('COMSOL_MPH_PORT'));
  if isnan(server_port), server_port = 2036; end
  mphstart(server_host, server_port);
  model = busbar_joule_heat_baseline();
  mphsave(model, fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
  disp('BUSBAR_JOULE_HEAT_BASELINE_SUCCESS');
catch ME
  disp(getReport(ME, 'extended', 'hyperlinks', 'off'));
  rethrow(ME);
end
