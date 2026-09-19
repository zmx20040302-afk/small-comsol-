function model = generated_build_solid_mechanics_rectangle()
import com.comsol.model.*
import com.comsol.model.util.*
model = ModelUtil.create('Model');
model.param.set('L', '0.1[m]', 'L');
model.param.set('W', '0.02[m]', 'W');
model.param.set('E', '210000000000[Pa]', 'E');
model.param.set('nu', '0.3[1]', 'nu');
model.param.set('rho', '7850[kg/m^3]', 'rho');
model.param.set('p_load', '2000000.0[Pa]', 'p_load');
model.param.set('hmax', '0.002[m]', 'hmax');
model.component.create('comp1', true);
model.component('comp1').geom.create('geom1', 2);
model.component('comp1').geom('geom1').create('r1', 'Rectangle');
model.component('comp1').geom('geom1').feature('r1').set('size', {'L' 'W'});
model.component('comp1').geom('geom1').run;
model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup('def').set('density', 'rho');
model.component('comp1').material('mat1').propertyGroup('def').set('youngsmodulus', 'E');
model.component('comp1').material('mat1').propertyGroup('def').set('poissonsratio', 'nu');
model.component('comp1').physics.create('solid', 'SolidMechanics', 'geom1');
model.component('comp1').physics('solid').create('fix1', 'Fixed', 1);
model.component('comp1').physics('solid').feature('fix1').selection.set([1]);
model.component('comp1').physics('solid').create('bndl1', 'BoundaryLoad', 1);
model.component('comp1').physics('solid').feature('bndl1').selection.set([3]);
model.component('comp1').physics('solid').feature('bndl1').set('FperArea', {'p_load' '0' '0'});
model.component('comp1').mesh.create('mesh1');
model.component('comp1').mesh('mesh1').create('size1', 'Size');
model.component('comp1').mesh('mesh1').feature('size1').set('custom', true);
model.component('comp1').mesh('mesh1').feature('size1').set('hmax', 'hmax');
model.component('comp1').mesh('mesh1').run;
model.study.create('std1');
model.study('std1').create('stat', 'Stationary');
model.study('std1').createAutoSequences('all');
model.study('std1').run;
end
