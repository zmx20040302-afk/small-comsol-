function model = generated_build_one_dimensional_axial_bar()
%GENERATED_BUILD_ONE_DIMENSIONAL_AXIAL_BAR 1D COMSOL benchmark model.
% Boundary 1 is x=0 and boundary 2 is x=L for an interval geometry. Verify after build.
import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');
model.label('one_dimensional_axial_bar.mph');
model.param.set('L', '0.1[m]', 'One-dimensional domain length');
model.param.set('E_mod', '210000000000.0[Pa]', 'E mod');
model.param.set('nu_mat', '0.3[1]', 'nu mat');
model.param.set('rho_mat', '7850.0[kg/m^3]', 'rho mat');
model.param.set('p_load', '1000000.0[Pa]', 'p load');
model.param.set('hmax', '0.002[m]', 'hmax');

model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 1);
model.component('comp1').geom('geom1').lengthUnit('m');
model.component('comp1').geom('geom1').create('i1', 'Interval');
model.component('comp1').geom('geom1').feature('i1').set('p1', '0');
model.component('comp1').geom('geom1').feature('i1').set('p2', 'L');
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho_mat');
model.component('comp1').material('mat1').propertyGroup('def').set('youngsmodulus', 'E_mod');
model.component('comp1').material('mat1').propertyGroup('def').set('poissonsratio', 'nu_mat');
% Use the base Solid Mechanics interface so this axial-bar template does not require the Beam module.
model.component('comp1').physics.create('solid', 'SolidMechanics', 'geom1');
model.component('comp1').physics('solid').selection.all;
model.component('comp1').physics('solid').create('fix1', 'Fixed', 0);
model.component('comp1').physics('solid').feature('fix1').selection.set([1]);
model.component('comp1').physics('solid').create('bndl1', 'BoundaryLoad', 0);
model.component('comp1').physics('solid').feature('bndl1').selection.set([2]);
model.component('comp1').physics('solid').feature('bndl1').set('FperArea', {'p_load' '0' '0'});

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
model.study('std1').feature('stat').activate('solid', true);
model.study('std1').createAutoSequences('all');
model.study('std1').run;
model.result.numerical.create('u_max', 'EvalGlobal');
model.result.numerical('u_max').set('expr', 'maxop1(solid.disp)');
model.result.numerical.create('mises_max', 'EvalGlobal');
model.result.numerical('mises_max').set('expr', 'maxop1(solid.mises)');
% Saving is handled by the execution wrapper with mphsave(model, output_path).
end
