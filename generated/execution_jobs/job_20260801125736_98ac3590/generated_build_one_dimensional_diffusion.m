function model = generated_build_one_dimensional_diffusion()
%GENERATED_BUILD_ONE_DIMENSIONAL_DIFFUSION 1D COMSOL benchmark model.
% Boundary 1 is x=0 and boundary 2 is x=L for an interval geometry. Verify after build.
import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');
model.label('one_dimensional_diffusion.mph');
model.param.set('L', '0.01[m]', 'One-dimensional domain length');
model.param.set('D', '1e-09[m^2/s]', 'D');
model.param.set('c_left', '1[mol/m^3]', 'c left');
model.param.set('c_right', '0[mol/m^3]', 'c right');
model.param.set('hmax', '0.0002[m]', 'hmax');

model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 1);
model.component('comp1').geom('geom1').lengthUnit('m');
model.component('comp1').geom('geom1').create('i1', 'Interval');
model.component('comp1').geom('geom1').feature('i1').set('p1', '0');
model.component('comp1').geom('geom1').feature('i1').set('p2', 'L');
model.component('comp1').geom('geom1').run;

model.component('comp1').physics.create('tds', 'DilutedSpecies', 'geom1');
model.component('comp1').physics('tds').selection.all;
model.component('comp1').physics('tds').feature('cdm1').set('Dm_c', {'D'});
model.component('comp1').physics('tds').feature('init1').set('initc', 'c_right');
model.component('comp1').physics('tds').create('conc1', 'Concentration', 0);
model.component('comp1').physics('tds').feature('conc1').selection.set([1]);
model.component('comp1').physics('tds').feature('conc1').set('c0', {'c_left'});
model.component('comp1').physics('tds').create('conc2', 'Concentration', 0);
model.component('comp1').physics('tds').feature('conc2').selection.set([2]);
model.component('comp1').physics('tds').feature('conc2').set('c0', {'c_right'});

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
model.study('std1').feature('stat').activate('tds', true);
model.study('std1').createAutoSequences('all');
model.study('std1').run;
model.result.numerical.create('c_max', 'EvalGlobal');
model.result.numerical('c_max').set('expr', 'maxop1(c)');
% Saving is handled by the execution wrapper with mphsave(model, output_path).
end
