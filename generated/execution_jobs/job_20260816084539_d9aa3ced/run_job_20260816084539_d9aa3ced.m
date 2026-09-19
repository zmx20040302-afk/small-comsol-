try
  addpath('generated/execution_jobs/job_20260816084539_d9aa3ced');
  if exist('mphstart', 'file') ~= 0
    server_host = getenv('COMSOL_MPH_HOST');
    if isempty(server_host), server_host = 'localhost'; end
    server_port = str2double(getenv('COMSOL_MPH_PORT'));
    if isnan(server_port), server_port = 2036; end
    mphstart(server_host, server_port);
  else
    error('LiveLink for COMSOL is not available on the MATLAB path.');
  end
  model = job_20260816084539_d9aa3ced();
  % Re-run mesh and study here so result export always targets a solved dataset.
  model.component('comp1').mesh('mesh1').run;
  model.study('std1').run;
  mphsave(model, 'D:/桌面/codex/comsol1/comsol_training_small_model/generated/execution_jobs/job_20260816084539_d9aa3ced/job_20260816084539_d9aa3ced.mph');
  disp('COMSOL_EXECUTION_SUCCESS');
catch ME
  disp(getReport(ME, 'extended', 'hyperlinks', 'off'));
  rethrow(ME);
end
