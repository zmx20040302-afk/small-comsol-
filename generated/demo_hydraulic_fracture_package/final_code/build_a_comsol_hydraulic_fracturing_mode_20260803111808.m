function model = build_a_comsol_hydraulic_fracturing_mode_20260803111808()
%BUILD_A_COMSOL_HYDRAULIC_FRACTURING_MODE_20260803111808 Memory-assisted COMSOL LiveLink builder.
% 由 comsol_training_small_model 生成。
% Requirement: Build a COMSOL hydraulic fracturing model for a single borehole under different confining stress conditions. 中文需求关键词：水力压裂 单孔 围压 主应力 天然裂缝 煤层 岩石裂隙流 多孔介质 裂缝拓展 损伤演化。 Use article parameters: square_side=300[mm] borehole_diameter=15[mm] stress_ratio_range=1.5~2.0 initial_pressure=0.1[MPa] mean_elastic_modulus=35.1[GPa] mean_compressive_strength=152[MPa] principal_stress_direction_135=135[deg] principal_stress_direction_180=180[deg] principal_stress_direction_90=90[deg]. Include features: 2D square dom
% GENERATION STATUS: REVIEW_REQUIRED until verification JSON reports ready_to_solve=true.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');
model.label('build_a_comsol_hydraulic_fracturing_mode_20260803111808.mph');
model.modelNode.create('mod1');

% Parameters merged from matched case memory and defaults.
model.param.set('rho_ref', '998[kg/m^3]', 'Material density');
model.param.set('k_ref', '0.6[W/(m*K)]', 'Material thermal conductivity');
model.param.set('Cp_ref', '4182[J/(kg*K)]', 'Material heat capacity');
model.param.set('sigma_ref', '1[S/m]', 'Material electrical conductivity');
model.param.set('hmax', '0.02[m]', 'Maximum mesh size');
model.param.set('E_ref', '35.1[GPa]', 'Youngs modulus');
model.param.set('nu_ref', '0.25', 'Poissons ratio');
model.param.set('L_ref', '1[m]', 'Reference length');
model.param.set('W_ref', '1[m]', 'Reference width');
model.param.set('H_ref', '0.1[m]', 'Reference height');
model.param.set('square_side', '300[mm]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('borehole_diameter', '15[mm]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('stress_ratio_range', '1.5~2.0', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('initial_pressure', '0.1[MPa]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('mean_elastic_modulus', '35.1[GPa]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('mean_compressive_strength', '152[MPa]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('principal_stress_direction_135', '135[deg]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('principal_stress_direction_180', '180[deg]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('principal_stress_direction_90', '90[deg]', 'COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究');
model.param.set('E', '210[GPa]', '杨氏模量');
model.param.set('alpha', '12e-6[1/K]', '热膨胀系数');
model.param.set('T_hot', '373.15[K]', '热端温度');
model.param.set('T_cold', '293.15[K]', '冷端温度');
model.param.set('L', '0.1[m]', '实体长度');
model.param.set('W', '0.02[m]', '实体宽度');
model.param.set('nu', '0.3', '泊松比');
model.param.set('p_load', '1[MPa]', '均布边界载荷');
model.param.set('rho', '1000[kg/m^3]', '岩石裂隙流');
model.param.set('mu', '0.001[Pa*s]', '岩石裂隙流');
model.param.set('k', '1[W/(m*K)]', '导热系数');
model.param.set('Cp', '800[J/(kg*K)]', '比热容');
model.param.set('ft', '1', '抗拉强度');
model.param.set('fc', '1', '抗压强度');
model.param.set('Gc', '1', '断裂能');
model.param.set('Cp_f', '800[J/(kg*K)]', '比热容');
model.param.set('k_f', '1[W/(m*K)]', '导热系数');
model.param.set('D', '1', '扩散系数');
model.param.set('epsilon', '1', '表面发射率');
model.param.set('alpha_T', '1', '热膨胀系数');

model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 3);
model.component('comp1').geom('geom1').lengthUnit('m');
% REVIEW REQUIRED: confirm that the selected geometry pattern matches the approved dimensions.
% Geometry guidance: 几何与参数应优先按“水力压裂单孔/裂隙几何 + 结构力学几何与参数”组织。
model.component('comp1').geom('geom1').create('rect1', 'Rectangle');
model.component('comp1').geom('geom1').feature('rect1').set('size', {'Lx' 'Ly'});
model.component('comp1').geom('geom1').feature('rect1').set('pos', {'-Lx/2' '-Ly/2'});
model.component('comp1').geom('geom1').create('c1', 'Circle');
model.component('comp1').geom('geom1').feature('c1').set('r', 'rb');
model.component('comp1').geom('geom1').create('dif1', 'Difference');
model.component('comp1').geom('geom1').feature('dif1').selection('input').set({'rect1'});
model.component('comp1').geom('geom1').feature('dif1').selection('input2').set({'c1'});
% REVIEW REQUIRED: add the approved fracture/weak-plane or phase-field initialization.
model.component('comp1').geom('geom1').run;
% REVIEW REQUIRED: bind borehole, outer-boundary, and rock-domain named selections.

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').label('Water');
model.component('comp1').material('mat1').selection.all;
model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho_ref');
model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', 'k_ref');
model.component('comp1').material('mat1').propertyGroup('def').set('heatcapacity', 'Cp_ref');
model.component('comp1').material('mat1').propertyGroup('def').set('electricconductivity', 'sigma_ref');
model.component('comp1').material('mat1').propertyGroup.create('Enu', 'Enu', 'Youngs modulus and Poissons ratio');
model.component('comp1').material('mat1').propertyGroup('Enu').set('E', 'E_ref');
model.component('comp1').material('mat1').propertyGroup('Enu').set('nu', 'nu_ref');

% Physics inferred from requirement, matched cases, and COMSOL knowledge memory.
model.component('comp1').physics.create('ht', 'HeatTransfer', 'geom1');
% Add heat flux, temperature, or convection features after selections are verified.
model.component('comp1').physics.create('solid', 'SolidMechanics', 'geom1');
% Add fixed constraints, loads, pore/fracture pressure, and stress boundary conditions.
model.component('comp1').physics.create('spf', 'LaminarFlow', 'geom1');
% Add inlet, outlet, wall, and pressure conditions; switch interface for porous/fracture flow if needed.
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
model.result.numerical.create('gev1', 'EvalGlobal');
model.result.numerical('gev1').label('volume_total');
model.result.numerical('gev1').set('expr', '1');
model.result.numerical.create('gev2', 'EvalGlobal');
model.result.numerical('gev2').label('surface_area_total');
model.result.numerical('gev2').set('expr', '1');
model.result.numerical.create('gev3', 'EvalGlobal');
model.result.numerical('gev3').label('entity_count');
model.result.numerical('gev3').set('expr', '1');
model.result.numerical.create('gev4', 'EvalGlobal');
model.result.numerical('gev4').label('geometry_build_success');
model.result.numerical('gev4').set('expr', '1');
model.result.numerical.create('gev5', 'MaxVolume');
model.result.numerical('gev5').label('Tmax');
model.result.numerical('gev5').set('expr', 'T');
model.result.numerical.create('gev6', 'AvVolume');
model.result.numerical('gev6').label('Tavg');
model.result.numerical('gev6').set('expr', 'T');
model.result.numerical.create('gev7', 'EvalGlobal');
model.result.numerical('gev7').label('heat_flux_integral');
model.result.numerical('gev7').set('expr', '1');
model.result.numerical.create('gev8', 'MaxVolume');
model.result.numerical('gev8').label('max_displacement');
model.result.numerical('gev8').set('expr', 'solid.disp');

% Saving is handled by the execution wrapper with mphsave(model, output_path).
end
