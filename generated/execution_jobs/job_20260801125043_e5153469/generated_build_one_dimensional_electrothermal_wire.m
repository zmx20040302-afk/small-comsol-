function model = generated_build_one_dimensional_electrothermal_wire()
%GENERATED_BUILD_ONE_DIMENSIONAL_ELECTROTHERMAL_WIRE 1D COMSOL benchmark model.
% Boundary 1 is x=0 and boundary 2 is x=L for an interval geometry. Verify after build.
import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');
model.label('one_dimensional_electrothermal_wire.mph');
model.param.set('L', '0.1[m]', 'One-dimensional domain length');
model.param.set('k', '401[W/(m*K)]', 'k');
model.param.set('rho', '8960[kg/m^3]', 'rho');
model.param.set('Cp', '385[J/(kg*K)]', 'Cp');
model.param.set('sigma', '58000000.0[S/m]', 'sigma');
model.param.set('V_left', '0.01[V]', 'V left');
model.param.set('T_left', '293.15[K]', 'T left');
model.param.set('T_right', '293.15[K]', 'T right');
model.param.set('hmax', '0.002[m]', 'hmax');

model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 1);
model.component('comp1').geom('geom1').lengthUnit('m');
model.component('comp1').geom('geom1').create('i1', 'Interval');
model.component('comp1').geom('geom1').feature('i1').set('p1', '0');
model.component('comp1').geom('geom1').feature('i1').set('p2', 'L');
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', 'k');
model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho');
model.component('comp1').material('mat1').propertyGroup('def').set('heatcapacity', 'Cp');
model.component('comp1').material('mat1').propertyGroup('def').set('electricconductivity', 'sigma');
model.component('comp1').physics.create('ec', 'ConductiveMedia', 'geom1');
model.component('comp1').physics('ec').selection.all;
model.component('comp1').physics('ec').create('pot1', 'ElectricPotential', 0);
model.component('comp1').physics('ec').feature('pot1').selection.set([1]);
model.component('comp1').physics('ec').feature('pot1').set('V0', 'V_left');
model.component('comp1').physics('ec').create('gnd1', 'Ground', 0);
model.component('comp1').physics('ec').feature('gnd1').selection.set([2]);
model.component('comp1').physics.create('ht', 'HeatTransfer', 'geom1');
model.component('comp1').physics('ht').selection.all;
model.component('comp1').physics('ht').create('hs1', 'HeatSource', 1);
model.component('comp1').physics('ht').feature('hs1').selection.all;
model.component('comp1').physics('ht').feature('hs1').set('Q0', 'ec.Qh');
model.component('comp1').physics('ht').create('temp1', 'TemperatureBoundary', 0);
model.component('comp1').physics('ht').feature('temp1').selection.set([1]);
model.component('comp1').physics('ht').feature('temp1').set('T0', 'T_left');
model.component('comp1').physics('ht').create('temp2', 'TemperatureBoundary', 0);
model.component('comp1').physics('ht').feature('temp2').selection.set([2]);
model.component('comp1').physics('ht').feature('temp2').set('T0', 'T_right');

model.component('comp1').mesh.create('mesh1');
model.component('comp1').mesh('mesh1').create('size1', 'Size');
model.component('comp1').mesh('mesh1').feature('size1').set('custom', true);
model.component('comp1').mesh('mesh1').feature('size1').set('hmax', 'hmax');
model.component('comp1').mesh('mesh1').create('edg1', 'Edge');
model.component('comp1').mesh('mesh1').run;

model.component('comp1').cpl.create('maxop1', 'Maximum');
model.component('comp1').cpl('maxop1').selection.all;
model.study.create('std1');
model.study('std1').create('stat', 'Stationary');
model.study('std1').feature('stat').activate('ec', true);
model.study('std1').feature('stat').activate('ht', true);
model.study('std1').createAutoSequences('all');
model.study('std1').run;
model.result.numerical.create('T_max', 'EvalGlobal');
model.result.numerical('T_max').set('expr', 'maxop1(T)');
model.result.numerical.create('Q_joule_max', 'EvalGlobal');
model.result.numerical('Q_joule_max').set('expr', 'maxop1(ec.Qh)');
% Saving is handled by the execution wrapper with mphsave(model, output_path).
end
