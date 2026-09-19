addpath('D:/COMSOL64/Multiphysics/mli');
addpath('D:/桌面/codex/comsol1/comsol_training_small_model/matlab');
mphstart('localhost', 2036);
result = export_mph_code_bundle('D:/桌面/codex/案例下载/COMSOL/多孔材料的有效扩散系数/effective_diffusivity.mph', 'D:/桌面/codex/comsol1/comsol_training_small_model/generated/mph_exports/effective_diffusivity');
disp(['MATLAB_EXPORT=' result.matlab_path]);
disp(['JAVA_EXPORT=' result.java_path]);
disp(['SUMMARY_EXPORT=' result.summary_path]);