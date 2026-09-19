function model = job_20260730020534_869cf9b3()
%JOB_20260730020534_869CF9B3 Memory-assisted COMSOL LiveLink builder.
% 由 comsol_training_small_model 生成。
% Requirement: 验证已批准母线板焦耳热 COMSOL 模型的一键执行队列。
% GENERATION STATUS: REVIEW_REQUIRED until verification JSON reports ready_to_solve=true.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');
model.label('job_20260730020534_869cf9b3.mph');
model.modelNode.create('mod1');

% Parameters merged from matched case memory and defaults.
model.param.set('rho_ref', '8960[kg/m^3]', 'Material density');
model.param.set('k_ref', '400[W/(m*K)]', 'Material thermal conductivity');
model.param.set('Cp_ref', '385[J/(kg*K)]', 'Material heat capacity');
model.param.set('sigma_ref', '5.998e7[S/m]', 'Material electrical conductivity');
model.param.set('hmax', '0.02[m]', 'Maximum mesh size');
model.param.set('L_ref', '1[m]', 'Reference length');
model.param.set('W_ref', '1[m]', 'Reference width');
model.param.set('H_ref', '0.1[m]', 'Reference height');
model.param.set('L', '9[cm]', '母线板焦耳热基准模型');
model.param.set('rad_1', '6[mm]', '母线板焦耳热基准模型');
model.param.set('tbb', '5[mm]', '母线板焦耳热基准模型');
model.param.set('wbb', '5[cm]', '母线板焦耳热基准模型');
model.param.set('mh', '3[mm]', '母线板焦耳热基准模型');
model.param.set('htc', '5[W/m^2/K]', '母线板焦耳热基准模型');
model.param.set('Vtot', '20[mV]', '母线板焦耳热基准模型');
model.param.set('Jan', '8000[A/m^2]', 'Anode current density');
model.param.set('htca', '5[W/m^2/K]', 'Heat transfer coefficient to air');
model.param.set('Ta', '35[degC]', 'Air temperature');
model.param.set('htce', '3000[W/m^2/K]', 'Heat transfer coefficient to electrolyte');
model.param.set('Te', '100[degC]', 'Electrolyte temperature');
model.param.set('c_g_w', '400[mm]', 'Cell grid top width');
model.param.set('c_g_l', '800[mm]', 'Cell grid top length');
model.param.set('c_g_h', '5[mm]', 'Cell grid top height');
model.param.set('s_l', 'c_g_l/2-2*s_di', 'Spine length');
model.param.set('s_w', 'c_g_w/2-2*s_di', 'Spine width');
model.param.set('s_h', '5[mm]', 'Spine height');
model.param.set('s_di', '10[mm]', 'Spine to cell grid boundary distance');
model.param.set('s_c_w', '65[mm]', 'Spine center width');
model.param.set('s_c_l', '60[mm]', 'Spine cut out length');
model.param.set('c_c_r', '40[mm]', 'Central column radius');
model.param.set('c_c_h', '70[mm]', 'Central column height');
model.param.set('c_c_d', '25[mm]', 'Central column center hole depth');
model.param.set('r_c_h', '6[mm]', 'Rod connector height');
model.param.set('rho', '2500[kg/m^3]', '密度');
model.param.set('k', '1[W/(m*K)]', '导热系数');
model.param.set('Cp', '800[J/(kg*K)]', '比热容');
model.param.set('sigma', '1[S/m]', '电导率');
model.param.set('epsilon', '1', '表面发射率');
model.param.set('alpha_T', '1', '热膨胀系数');
model.param.set('epsr', '1', '相对介电常数');

model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 2);
model.component('comp1').geom('geom1').lengthUnit('m');
% REVIEW REQUIRED: confirm that the selected geometry pattern matches the approved dimensions.
model.component('comp1').geom('geom1').create('r1', 'Rectangle');
model.component('comp1').geom('geom1').feature('r1').set('size', {'L_ref' 'W_ref'});
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').label('Copper');
model.component('comp1').material('mat1').selection.all;
model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho_ref');
model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', 'k_ref');
model.component('comp1').material('mat1').propertyGroup('def').set('heatcapacity', 'Cp_ref');
model.component('comp1').material('mat1').propertyGroup('def').set('electricconductivity', 'sigma_ref');

% Physics inferred from requirement, matched cases, and COMSOL knowledge memory.
model.component('comp1').physics.create('ht', 'HeatTransferInSolids', 'geom1');
% Add heat flux, temperature, or convection features after selections are verified.
% 边界选择目前是占位内容。请在 COMSOL 中检查生成几何的边界编号。

model.component('comp1').mesh.create('mesh1');
model.component('comp1').mesh('mesh1').create('size1', 'Size');
model.component('comp1').mesh('mesh1').feature('size1').set('custom', true);
model.component('comp1').mesh('mesh1').feature('size1').set('hmax', 'hmax');
model.component('comp1').mesh('mesh1').run;

model.study.create('std1');
model.study('std1').create('stat', 'Stationary');
model.study('std1').createAutoSequences('all');
% model.study('std1').run; % Enable after selections, conditions, and solver settings are verified.

% Derived values suggested by memory-assisted plan.
model.result.numerical.create('gev1', 'MaxVolume');
model.result.numerical('gev1').label('Tmax');
model.result.numerical('gev1').set('expr', 'T');
model.result.numerical.create('gev2', 'AvVolume');
model.result.numerical('gev2').label('Tavg');
model.result.numerical('gev2').set('expr', 'T');
model.result.numerical.create('gev3', 'EvalGlobal');
model.result.numerical('gev3').label('heat_flux_integral');
model.result.numerical('gev3').set('expr', '1');

model.save(fullfile(pwd, [model.label]));
end
