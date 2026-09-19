function model = job_20260816084539_d9aa3ced()
%JOB_20260816084539_D9AA3CED Memory-assisted COMSOL LiveLink builder.
% 由 comsol_training_small_model 生成。
% Requirement: 建立母线板焦耳热标杆模型：电流场与固体传热通过 Joule Heating 耦合，输出温度与电流密度，并准备参数扫描 CSV。
% GENERATION STATUS: REVIEW_REQUIRED until verification JSON reports ready_to_solve=true.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');
model.label('job_20260816084539_d9aa3ced.mph');
model.modelNode.create('mod1');

% Parameters merged from matched case memory and defaults.
model.param.set('rho_ref', '8960[kg/m^3]', 'Material density');
model.param.set('k_ref', '400[W/(m*K)]', 'Material thermal conductivity');
model.param.set('Cp_ref', '385[J/(kg*K)]', 'Material heat capacity');
model.param.set('sigma_ref', '5.998e7[S/m]', 'Material electrical conductivity');
model.param.set('hmax', '0.02[m]', 'Maximum mesh size');
model.param.set('Vtot', '20[mV]', 'Applied electric potential difference');
model.param.set('T_amb', '293.15[K]', 'Ambient temperature');
model.param.set('htc', '5[W/(m^2*K)]', 'Convective heat transfer coefficient');
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
model.component('comp1').physics.create('ht', 'HeatTransfer', 'geom1');
% Add heat flux, temperature, or convection features after selections are verified.
model.component('comp1').physics.create('ec', 'ConductiveMedia', 'geom1');
% Electric Currents interface: add terminal, ground, and insulation boundary conditions.
model.component('comp1').multiphysics.create('emh1', 'ElectromagneticHeating', 2);
model.component('comp1').multiphysics('emh1').set('EMHeat_physics', 'ec');
model.component('comp1').multiphysics('emh1').set('Heat_physics', 'ht');
model.component('comp1').multiphysics('emh1').selection.all;
% Joule Heating coupling transfers electrical loss to the heat-transfer interface.
model.component('comp1').selection.create('sel_terminal', 'Explicit');
model.component('comp1').selection('sel_terminal').geom('geom1', 1);
model.component('comp1').selection('sel_terminal').label('Terminal boundary - review entity IDs');
model.component('comp1').selection.create('sel_ground', 'Explicit');
model.component('comp1').selection('sel_ground').geom('geom1', 1);
model.component('comp1').selection('sel_ground').label('Ground boundary - review entity IDs');
model.component('comp1').selection.create('sel_convection', 'Explicit');
model.component('comp1').selection('sel_convection').geom('geom1', 1);
model.component('comp1').selection('sel_convection').label('Exterior convection boundary - review entity IDs');
model.component('comp1').physics('ec').create('pot1', 'ElectricPotential', 1);
model.component('comp1').physics('ec').feature('pot1').selection.named('sel_terminal');
model.component('comp1').physics('ec').feature('pot1').set('V0', 'Vtot');
model.component('comp1').physics('ec').create('gnd1', 'Ground', 1);
model.component('comp1').physics('ec').feature('gnd1').selection.named('sel_ground');
model.component('comp1').physics('ht').create('hf1', 'HeatFluxBoundary', 1);
model.component('comp1').physics('ht').feature('hf1').selection.named('sel_convection');
model.component('comp1').physics('ht').feature('hf1').set('HeatFluxType', 'ConvectiveHeatFlux');
model.component('comp1').physics('ht').feature('hf1').set('h', 'htc');
model.component('comp1').physics('ht').feature('hf1').set('Text', 'T_amb');
% REVIEW REQUIRED: assign verified boundary IDs to sel_terminal, sel_ground, and sel_convection before solving.
% model.component('comp1').selection('sel_terminal').set([terminal_boundary_id]);
% model.component('comp1').selection('sel_ground').set([ground_boundary_id]);
% model.component('comp1').selection('sel_convection').set([exterior_boundary_ids]);
% 边界选择目前是占位内容。请在 COMSOL 中检查生成几何的边界编号。

model.component('comp1').mesh.create('mesh1');
model.component('comp1').mesh('mesh1').create('size1', 'Size');
model.component('comp1').mesh('mesh1').feature('size1').set('custom', true);
model.component('comp1').mesh('mesh1').feature('size1').set('hmax', 'hmax');
model.component('comp1').mesh('mesh1').create('ftri1', 'FreeTri');
model.component('comp1').mesh('mesh1').run;
% Create field-evaluation operators after the mesh so their source selection is mesh-aware.
model.component('comp1').cpl.create('maxop1', 'Maximum');
model.component('comp1').cpl('maxop1').selection.all;
model.component('comp1').cpl.create('aveop1', 'Average');
model.component('comp1').cpl('aveop1').selection.all;

model.study.create('std1');
model.study('std1').create('stat', 'Stationary');
model.study('std1').feature.create('param', 'Parametric');
model.study('std1').feature('param').set('pname', {'Vtot'});
model.study('std1').feature('param').set('plistarr', {'range(0.1[mV],0.025[mV],1[mV])'});
% REVIEW REQUIRED: replace the voltage sweep range with the approved values.
model.study('std1').createAutoSequences('all');
% model.study('std1').run; % Enable after selections, conditions, and solver settings are verified.

% Derived values suggested by memory-assisted plan.
model.result.numerical.create('gev1', 'MaxSurface');
model.result.numerical('gev1').label('Tmax');
model.result.numerical('gev1').set('expr', 'T');
model.result.numerical.create('gev2', 'AvSurface');
model.result.numerical('gev2').label('Tavg');
model.result.numerical('gev2').set('expr', 'T');
model.result.numerical.create('gev3', 'EvalGlobal');
model.result.numerical('gev3').label('heat_flux_integral');
model.result.numerical('gev3').set('expr', '1');
model.result.numerical.create('gev4', 'MaxSurface');
model.result.numerical('gev4').label('max_current_density');
model.result.numerical('gev4').set('expr', 'ec.normJ');
model.result.numerical.create('gev5', 'EvalGlobal');
model.result.numerical('gev5').label('electric_resistance');
model.result.numerical('gev5').set('expr', '1');
% REVIEW REQUIRED: export terminal_current with a boundary integration over the verified terminal selection.

% Saving is handled by the execution wrapper with mphsave(model, output_path).
end
