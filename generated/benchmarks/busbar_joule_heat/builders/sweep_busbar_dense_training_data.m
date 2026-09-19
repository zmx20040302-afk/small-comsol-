builder_dir = fileparts(mfilename('fullpath'));
addpath(builder_dir);
addpath('D:/COMSOL64/Multiphysics/mli');
server_host = getenv('COMSOL_MPH_HOST');
if isempty(server_host), server_host = 'localhost'; end
server_port = str2double(getenv('COMSOL_MPH_PORT'));
if isnan(server_port), server_port = 2036; end
mphstart(server_host, server_port);

model = mphopen(fullfile(builder_dir, 'busbar_joule_heat_baseline.mph'));
voltages_mv = linspace(10, 30, 7);
heat_transfer_coefficients = linspace(2, 10, 7);
output_path = fullfile(builder_dir, 'busbar_dense_training_data.csv');
error_path = fullfile(builder_dir, 'busbar_dense_training_data.error.txt');
if isfile(error_path), delete(error_path); end
result = table();

potential_selection = mphgetselection(model.component('comp1').physics('ec').feature('pot1'));
convection_selection = mphgetselection(model.component('comp1').physics('ht').feature('hf1'));

try
  for voltage_mv = voltages_mv
    for htc_w_m2k = heat_transfer_coefficients
      model.param.set('Vtot', sprintf('%.12g[mV]', voltage_mv));
      model.param.set('htc', sprintf('%.12g[W/(m^2*K)]', htc_w_m2k));
      model.study('std1').run;
      tmax_k = mphmax(model, 'T', 3);
      terminal_current_a = abs(mphint2(model, 'ec.nJ', 2, 'selection', potential_selection.entities'));
      joule_power_w = mphint2(model, 'ec.Qh', 3);
      convection_power_w = abs(mphint2(model, 'ht.nteflux', 2, 'selection', convection_selection.entities'));
      energy_imbalance_percent = abs(joule_power_w-convection_power_w)/joule_power_w*100;
      next_row = table(voltage_mv, htc_w_m2k, tmax_k, tmax_k-273.15, terminal_current_a, joule_power_w, convection_power_w, energy_imbalance_percent, ...
        'VariableNames', {'Vtot_mV', 'htc_W_m2K', 'Tmax_K', 'Tmax_C', 'terminal_current_A', 'joule_power_W', 'convection_power_W', 'energy_imbalance_percent'});
      result = [result; next_row]; %#ok<AGROW>
      writetable(result, output_path);
      fprintf('Completed %d/%d: Vtot=%g mV, htc=%g W/(m^2*K)\\n', height(result), numel(voltages_mv)*numel(heat_transfer_coefficients), voltage_mv, htc_w_m2k);
    end
  end
catch errorInfo
  error_file = fopen(error_path, 'w');
  fprintf(error_file, '%s\\n', getReport(errorInfo, 'extended', 'hyperlinks', 'off'));
  fclose(error_file);
  rethrow(errorInfo);
end
