function out = model
%
% simple_resistor.m
%
% Model exported on Aug 25 2026, 16:23 by COMSOL 6.4.0.293.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath(['D:\' native2unicode(hex2dec({'68' '4c'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode') '\codex\' native2unicode(hex2dec({'68' '48'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'4e' '0b'}), 'unicode')  native2unicode(hex2dec({'8f' '7d'}), 'unicode') '\' native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'6c' '14'}), 'unicode') '\' native2unicode(hex2dec({'8b' 'a1'}), 'unicode')  native2unicode(hex2dec({'7b' '97'}), 'unicode')  native2unicode(hex2dec({'5b' 'fc'}), 'unicode')  native2unicode(hex2dec({'7e' 'bf'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'96' '3b'}), 'unicode') ]);

model.label('simple_resistor.mph');

model.title([native2unicode(hex2dec({'8b' 'a1'}), 'unicode')  native2unicode(hex2dec({'7b' '97'}), 'unicode')  native2unicode(hex2dec({'5b' 'fc'}), 'unicode')  native2unicode(hex2dec({'7e' 'bf'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'96' '3b'}), 'unicode') ]);

model.description([native2unicode(hex2dec({'6b' 'cf'}), 'unicode')  native2unicode(hex2dec({'79' 'cd'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'6c' '14'}), 'unicode')  native2unicode(hex2dec({'8b' 'be'}), 'unicode')  native2unicode(hex2dec({'59' '07'}), 'unicode')  native2unicode(hex2dec({'90' 'fd'}), 'unicode')  native2unicode(hex2dec({'67' '09'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'96' '3b'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'4e' '5f'}), 'unicode')  native2unicode(hex2dec({'5c' '31'}), 'unicode')  native2unicode(hex2dec({'66' '2f'}), 'unicode')  native2unicode(hex2dec({'8b' 'f4'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'5f' '53'}), 'unicode')  native2unicode(hex2dec({'8b' 'be'}), 'unicode')  native2unicode(hex2dec({'59' '07'}), 'unicode')  native2unicode(hex2dec({'4e' '24'}), 'unicode')  native2unicode(hex2dec({'7a' 'ef'}), 'unicode')  native2unicode(hex2dec({'65' 'bd'}), 'unicode')  native2unicode(hex2dec({'52' 'a0'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'52' 'bf'}), 'unicode')  native2unicode(hex2dec({'5d' 'ee'}), 'unicode')  native2unicode(hex2dec({'65' 'f6'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'4f' '1a'}), 'unicode')  native2unicode(hex2dec({'4e' 'a7'}), 'unicode')  native2unicode(hex2dec({'75' '1f'}), 'unicode')  native2unicode(hex2dec({'6b' '63'}), 'unicode')  native2unicode(hex2dec({'6b' 'd4'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'6d' '41'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode')  native2unicode(hex2dec({'67' '2c'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'6f' '14'}), 'unicode')  native2unicode(hex2dec({'79' '3a'}), 'unicode')  native2unicode(hex2dec({'59' '82'}), 'unicode')  native2unicode(hex2dec({'4f' '55'}), 'unicode')  native2unicode(hex2dec({'8b' 'a1'}), 'unicode')  native2unicode(hex2dec({'7b' '97'}), 'unicode')  native2unicode(hex2dec({'94' 'dc'}), 'unicode')  native2unicode(hex2dec({'5b' 'fc'}), 'unicode')  native2unicode(hex2dec({'7e' 'bf'}), 'unicode')  native2unicode(hex2dec({'62' '2a'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode')  native2unicode(hex2dec({'4e' '0a'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'96' '3b'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode')  native2unicode(hex2dec({'54' '0c'}), 'unicode')  native2unicode(hex2dec({'65' 'f6'}), 'unicode')  native2unicode(hex2dec({'78' '14'}), 'unicode')  native2unicode(hex2dec({'7a' '76'}), 'unicode')  native2unicode(hex2dec({'4e' '86'}), 'unicode')  native2unicode(hex2dec({'7f' '51'}), 'unicode')  native2unicode(hex2dec({'68' '3c'}), 'unicode')  native2unicode(hex2dec({'59' '27'}), 'unicode')  native2unicode(hex2dec({'5c' '0f'}), 'unicode')  native2unicode(hex2dec({'4e' '0e'}), 'unicode')  native2unicode(hex2dec({'89' 'e3'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'65' '36'}), 'unicode')  native2unicode(hex2dec({'65' '5b'}), 'unicode')  native2unicode(hex2dec({'60' '27'}), 'unicode')  native2unicode(hex2dec({'4e' '4b'}), 'unicode')  native2unicode(hex2dec({'95' 'f4'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'51' '73'}), 'unicode')  native2unicode(hex2dec({'7c' 'fb'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode') ]);

model.param.label('Parameters 1');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 3);

model.component('comp1').label('Component 1');

model.result.table.create('tbl1', 'Table');

model.component('comp1').mesh.create('mesh1');

model.component('comp1').geom('geom1').label('Geometry 1');
model.component('comp1').geom('geom1').geomRep('comsol');
model.component('comp1').geom('geom1').create('cyl1', 'Cylinder');
model.component('comp1').geom('geom1').feature('cyl1').label('Cylinder 1');
model.component('comp1').geom('geom1').feature('cyl1').set('r', '0.5[mm]');
model.component('comp1').geom('geom1').feature('cyl1').set('h', '10[mm]');
model.component('comp1').geom('geom1').feature('fin').label('Form Union');
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').propertyGroup.create('Enu', 'Enu', 'Young''s modulus and Poisson''s ratio');
model.component('comp1').material('mat1').propertyGroup.create('linzRes', 'linzRes', 'Linearized resistivity');

model.component('comp1').physics.create('ec', 'ConductiveMedia', 'geom1');
model.component('comp1').physics('ec').create('gnd1', 'Ground', 2);
model.component('comp1').physics('ec').feature('gnd1').selection.set([3]);
model.component('comp1').physics('ec').create('term1', 'Terminal', 2);
model.component('comp1').physics('ec').feature('term1').selection.set([4]);

model.component('comp1').mesh('mesh1').autoMeshSize(2);

model.result.table('tbl1').label('Table 1');
model.result.table('tbl1').comments('Global Evaluation 1');

model.thermodynamics.label('Thermodynamics');

model.frame('material1').label('Moving Mesh 1');

model.component('comp1').view('view1').label('View 1');
model.component('comp1').view('view1').set('renderwireframe', true);
model.component('comp1').view('view1').axis.label('Axis');
model.component('comp1').view('view1').light('lgt1').label('Directional Light 1');
model.component('comp1').view('view1').light('lgt2').label('Directional Light 2');
model.component('comp1').view('view1').light('lgt3').label('Directional Light 3');

model.material.label('Materials');
model.component('comp1').material('mat1').label('Copper');
model.component('comp1').material('mat1').set('family', 'copper');
model.component('comp1').material('mat1').propertyGroup('def').label('Basic');
model.component('comp1').material('mat1').propertyGroup('def').set('relpermeability', {'1' '0' '0' '0' '1' '0' '0' '0' '1'});
model.component('comp1').material('mat1').propertyGroup('def').set('electricconductivity', {'5.998e7[S/m]' '0' '0' '0' '5.998e7[S/m]' '0' '0' '0' '5.998e7[S/m]'});
model.component('comp1').material('mat1').propertyGroup('def').set('thermalexpansioncoefficient', {'17e-6[1/K]' '0' '0' '0' '17e-6[1/K]' '0' '0' '0' '17e-6[1/K]'});
model.component('comp1').material('mat1').propertyGroup('def').set('heatcapacity', '385[J/(kg*K)]');
model.component('comp1').material('mat1').propertyGroup('def').set('relpermittivity', {'1' '0' '0' '0' '1' '0' '0' '0' '1'});
model.component('comp1').material('mat1').propertyGroup('def').set('density', '8960[kg/m^3]');
model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', {'400[W/(m*K)]' '0' '0' '0' '400[W/(m*K)]' '0' '0' '0' '400[W/(m*K)]'});
model.component('comp1').material('mat1').propertyGroup('Enu').label('Young''s modulus and Poisson''s ratio');
model.component('comp1').material('mat1').propertyGroup('Enu').info('category').label('Information');
model.component('comp1').material('mat1').propertyGroup('Enu').set('E', '110[GPa]');
model.component('comp1').material('mat1').propertyGroup('Enu').set('nu', '0.35');
model.component('comp1').material('mat1').propertyGroup('linzRes').label('Linearized resistivity');
model.component('comp1').material('mat1').propertyGroup('linzRes').info('category').label('Information');
model.component('comp1').material('mat1').propertyGroup('linzRes').set('rho0', '1.72e-8[ohm*m]');
model.component('comp1').material('mat1').propertyGroup('linzRes').set('alpha', '0.0039[1/K]');
model.component('comp1').material('mat1').propertyGroup('linzRes').set('Tref', '298[K]');
model.component('comp1').material('mat1').propertyGroup('linzRes').addInput('temperature');

model.component('comp1').coordSystem('sys1').label('Boundary System 1');

model.common('cminpt').label('Default Model Inputs');

model.component('comp1').physics('ec').label('Electric Currents');
model.component('comp1').physics('ec').feature('cucns1').label('Current Conservation in Solids 1');
model.component('comp1').physics('ec').feature('cucns1').feature('ddis1').set('tm', []);
model.component('comp1').physics('ec').feature('cucns1').feature('ddis1').label('Dispersion 1');
model.component('comp1').physics('ec').feature('cucns1').feature('ddis1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ec').feature('cucns1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ec').feature('ein1').label('Electric Insulation 1');
model.component('comp1').physics('ec').feature('ein1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ec').feature('init1').label('Initial Values 1');
model.component('comp1').physics('ec').feature('init1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ec').feature('dcont1').label('Electric Continuity 1');
model.component('comp1').physics('ec').feature('dcont1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ec').feature('gnd1').label('Ground 1');
model.component('comp1').physics('ec').feature('gnd1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ec').feature('term1').set('I0', 1);
model.component('comp1').physics('ec').feature('term1').label('Boundary Terminal 1');
model.component('comp1').physics('ec').feature('term1').featureInfo('info').label('Equation View');

model.component('comp1').mesh('mesh1').label('Mesh 1');
model.component('comp1').mesh('mesh1').contribute('geom/detail', true);

model.study.create('std1');
model.study('std1').create('stat', 'Stationary');

model.sol.create('sol1');
model.sol('sol1').attach('std1');

model.result.numerical.create('gev1', 'EvalGlobal');
model.result.create('pg1', 'PlotGroup3D');
model.result('pg1').create('vol1', 'Volume');

model.study('std1').label('Study 1');
model.study('std1').feature('stat').label('Stationary');

model.batch.label('Batch');

model.sol('sol1').createAutoSequence('std1');
model.sol('sol1').label('Solution 1');

model.study('std1').runNoGen;

model.result.label('Results');
model.result.numerical('gev1').label('Global Evaluation 1');
model.result.numerical('gev1').set('table', 'tbl1');
model.result.numerical('gev1').set('expr', {'ec.R11'});
model.result.numerical('gev1').set('unit', {['m' 'ohm' ]});
model.result.numerical('gev1').set('descr', {'Resistance'});
model.result.numerical('gev1').setResult;
model.result('pg1').label('Electric Potential (ec)');
model.result('pg1').set('frametype', 'spatial');
model.result('pg1').set('showlegendsmaxmin', true);
model.result('pg1').feature('vol1').label('Volume 1');
model.result('pg1').feature('vol1').set('descr', 'Electric potential');
model.result('pg1').feature('vol1').set('colortable', 'Dipole');
model.result('pg1').feature('vol1').set('evaluationsettings', 'parent');
model.result('pg1').feature('vol1').set('resolution', 'normal');

out = model;
