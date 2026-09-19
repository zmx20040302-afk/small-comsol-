try
  addpath('D:/桌面/codex/comsol1/comsol_training_small_model/generated/execution_jobs/job_20260801124440_1ae7eb64');
  if exist('mphstart', 'file') ~= 0
    server_host = getenv('COMSOL_MPH_HOST');
    if isempty(server_host), server_host = 'localhost'; end
    server_port = str2double(getenv('COMSOL_MPH_PORT'));
    if isnan(server_port), server_port = 2036; end
    mphstart(server_host, server_port);
  else
    error('LiveLink for COMSOL is not available on the MATLAB path.');
  end
  model = generated_build_one_dimensional_diffusion();
  % Re-run mesh and study here so result export always targets a solved dataset.
  model.component('comp1').mesh('mesh1').run;
  model.study('std1').run;
  mphsave(model, 'D:/桌面/codex/comsol1/comsol_training_small_model/generated/execution_jobs/job_20260801124440_1ae7eb64/job_20260801124440_1ae7eb64.mph');
  output_names = {'c_max'};
  output_expressions = {'maxop1(c)'};
  results_file = 'D:/桌面/codex/comsol1/comsol_training_small_model/generated/execution_jobs/job_20260801124440_1ae7eb64/job_20260801124440_1ae7eb64_results.csv';
  results_fid = fopen(results_file, 'w');
  if results_fid < 0, error('Unable to create results CSV: %s', results_file); end
  fprintf(results_fid, 'name,expression,value\n');
  for output_index = 1:numel(output_names)
    output_value = mphglobal(model, output_expressions{output_index});
    fprintf(results_fid, '%s,\"%s\",%.16g\n', output_names{output_index}, output_expressions{output_index}, output_value(1));
  end
  fclose(results_fid);
  disp(['COMSOL_RESULTS_CSV=' results_file]);
  disp('COMSOL_EXECUTION_SUCCESS');
catch ME
  disp(getReport(ME, 'extended', 'hyperlinks', 'off'));
  rethrow(ME);
end
