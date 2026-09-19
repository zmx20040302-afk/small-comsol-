try
  addpath('D:/桌面/codex/comsol1/comsol_training_small_model/generated/execution_jobs/job_20260730164323_8bcbf2fb');
  if exist('mphstart', 'file') ~= 0
    server_host = getenv('COMSOL_MPH_HOST');
    if isempty(server_host), server_host = 'localhost'; end
    server_port = str2double(getenv('COMSOL_MPH_PORT'));
    if isnan(server_port), server_port = 2036; end
    mphstart(server_host, server_port);
  else
    error('LiveLink for COMSOL is not available on the MATLAB path.');
  end
  model = generated_build_one_dimensional_cantilever_beam();
  mphsave(model, 'D:/桌面/codex/comsol1/comsol_training_small_model/generated/execution_jobs/job_20260730164323_8bcbf2fb/job_20260730164323_8bcbf2fb.mph');
  disp('COMSOL_EXECUTION_SUCCESS');
catch ME
  disp(getReport(ME, 'extended', 'hyperlinks', 'off'));
  rethrow(ME);
end
