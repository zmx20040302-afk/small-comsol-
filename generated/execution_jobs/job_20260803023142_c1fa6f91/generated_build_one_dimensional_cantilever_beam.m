function model = generated_build_one_dimensional_cantilever_beam()
%GENERATED_BUILD_ONE_DIMENSIONAL_CANTILEVER_BEAM 1D COMSOL benchmark model.
% Boundary 1 is x=0 and boundary 2 is x=L for an interval geometry. Verify after build.
import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');
model.label('one_dimensional_cantilever_beam.mph');
model.param.set('L', '0.1[m]', 'One-dimensional domain length');
model.param.set('E', '210000000000.0[Pa]', 'E');
model.param.set('nu', '0.3[1]', 'nu');
model.param.set('rho', '7850.0[kg/m^3]', 'rho');
model.param.set('F', '10.0[N]', 'F');
model.param.set('hmax', '0.002[m]', 'hmax');

model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 1);
model.component('comp1').geom('geom1').lengthUnit('m');
model.component('comp1').geom('geom1').create('i1', 'Interval');
model.component('comp1').geom('geom1').feature('i1').set('p1', '0');
model.component('comp1').geom('geom1').feature('i1').set('p2', 'L');
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho');
model.component('comp1').material('mat1').propertyGroup('def').set('youngsmodulus', 'E');
model.component('comp1').material('mat1').propertyGroup('def').set('poissonsratio', 'nu');
model.component('comp1').physics.create('beam', 'Beam', 'geom1');
model.component('comp1').physics('beam').create('fix1', 'Fixed', 0);
model.component('comp1').physics('beam').feature('fix1').selection.set([1]);
model.component('comp1').physics('beam').create('load1', 'PointLoad', 0);
model.component('comp1').physics('beam').feature('load1').selection.set([2]);
model.component('comp1').physics('beam').feature('load1').set('F', {'F' '0' '0'});

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
model.study('std1').feature('stat').activate('beam', true);
model.study('std1').createAutoSequences('all');
model.study('std1').run;
model.result.numerical.create('u_max', 'EvalGlobal');
model.result.numerical('u_max').set('expr', 'maxop1(beam.disp)');
% Saving is handled by the execution wrapper with mphsave(model, output_path).
end
