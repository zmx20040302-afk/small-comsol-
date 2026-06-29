function summary = export_mph_summary(mphPath, outputJsonPath)
%EXPORT_MPH_SUMMARY Export a small JSON-like summary from a COMSOL MPH file.
%
% Requirements:
%   - COMSOL Multiphysics
%   - LiveLink for MATLAB
%
% Example:
%   summary = export_mph_summary('model.mph', 'model_summary.json');

import com.comsol.model.*
import com.comsol.model.util.*

model = mphload(mphPath);

summary = struct();
summary.source = mphPath;
summary.label = char(model.label());
summary.parameters = struct();

paramNames = model.param.varnames();
for i = 1:numel(paramNames)
    name = char(paramNames(i));
    summary.parameters.(matlab.lang.makeValidName(name)) = char(model.param.get(name));
end

summary.note = ['This summary is intentionally small. For full model trees, ' ...
    'export Java/MATLAB code from COMSOL or extend this script with model API calls.'];

if nargin > 1 && ~isempty(outputJsonPath)
    encoded = jsonencode(summary, PrettyPrint=true);
    fid = fopen(outputJsonPath, 'w');
    cleanup = onCleanup(@() fclose(fid));
    fwrite(fid, encoded, 'char');
end
end
