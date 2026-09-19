function out = model
%
% capacitor_dc.m
%
% Model exported on Aug 25 2026, 16:10 by COMSOL 6.4.0.293.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath(['D:\' native2unicode(hex2dec({'68' '4c'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode') '\codex\' native2unicode(hex2dec({'68' '48'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'4e' '0b'}), 'unicode')  native2unicode(hex2dec({'8f' '7d'}), 'unicode') '\' native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'6c' '14'}), 'unicode') '\' native2unicode(hex2dec({'8b' 'a1'}), 'unicode')  native2unicode(hex2dec({'7b' '97'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'5b' 'b9'}), 'unicode') ]);

model.label('capacitor_dc.mph');

model.title([native2unicode(hex2dec({'8b' 'a1'}), 'unicode')  native2unicode(hex2dec({'7b' '97'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'5b' 'b9'}), 'unicode') ]);

model.description([native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'5b' 'b9'}), 'unicode')  native2unicode(hex2dec({'56' '68'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'67' '00'}), 'unicode')  native2unicode(hex2dec({'7b' '80'}), 'unicode')  native2unicode(hex2dec({'53' '55'}), 'unicode')  native2unicode(hex2dec({'5f' '62'}), 'unicode')  native2unicode(hex2dec({'5f' '0f'}), 'unicode')  native2unicode(hex2dec({'66' '2f'}), 'unicode')  native2unicode(hex2dec({'53' 'cc'}), 'unicode')  native2unicode(hex2dec({'7a' 'ef'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'6c' '14'}), 'unicode')  native2unicode(hex2dec({'8b' 'be'}), 'unicode')  native2unicode(hex2dec({'59' '07'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'5f' '53'}), 'unicode')  native2unicode(hex2dec({'4e' '24'}), 'unicode')  native2unicode(hex2dec({'7a' 'ef'}), 'unicode')  native2unicode(hex2dec({'88' 'ab'}), 'unicode')  native2unicode(hex2dec({'65' 'bd'}), 'unicode')  native2unicode(hex2dec({'52' 'a0'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'53' '8b'}), 'unicode')  native2unicode(hex2dec({'5d' 'ee'}), 'unicode')  native2unicode(hex2dec({'65' 'f6'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'8f' 'd9'}), 'unicode')  native2unicode(hex2dec({'79' 'cd'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'5b' 'b9'}), 'unicode')  native2unicode(hex2dec({'56' '68'}), 'unicode')  native2unicode(hex2dec({'53' 'ef'}), 'unicode')  native2unicode(hex2dec({'4e' 'e5'}), 'unicode')  native2unicode(hex2dec({'50' 'a8'}), 'unicode')  native2unicode(hex2dec({'5b' '58'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'80' 'fd'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode')  native2unicode(hex2dec({'50' 'a8'}), 'unicode')  native2unicode(hex2dec({'5b' '58'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'80' 'fd'}), 'unicode')  native2unicode(hex2dec({'4e' '0e'}), 'unicode')  native2unicode(hex2dec({'59' '16'}), 'unicode')  native2unicode(hex2dec({'52' 'a0'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'53' '8b'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'5e' '73'}), 'unicode')  native2unicode(hex2dec({'65' 'b9'}), 'unicode')  native2unicode(hex2dec({'62' '10'}), 'unicode')  native2unicode(hex2dec({'6b' '63'}), 'unicode')  native2unicode(hex2dec({'6b' 'd4'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'5e' '76'}), 'unicode')  native2unicode(hex2dec({'90' '1a'}), 'unicode')  native2unicode(hex2dec({'8f' 'c7'}), 'unicode')  native2unicode(hex2dec({'56' '68'}), 'unicode')  native2unicode(hex2dec({'4e' 'f6'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'5b' 'b9'}), 'unicode')  native2unicode(hex2dec({'8f' 'db'}), 'unicode')  native2unicode(hex2dec({'88' '4c'}), 'unicode')  native2unicode(hex2dec({'91' 'cf'}), 'unicode')  native2unicode(hex2dec({'53' '16'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode')  native2unicode(hex2dec({'67' '2c'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'4e' 'cb'}), 'unicode')  native2unicode(hex2dec({'7e' 'cd'}), 'unicode')  native2unicode(hex2dec({'4e' '86'}), 'unicode')  native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'4e' '2a'}), 'unicode')  native2unicode(hex2dec({'7b' '80'}), 'unicode')  native2unicode(hex2dec({'53' '55'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'5b' 'b9'}), 'unicode')  native2unicode(hex2dec({'56' '68'}), 'unicode')  native2unicode(hex2dec({'6a' '21'}), 'unicode')  native2unicode(hex2dec({'57' '8b'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'6c' '42'}), 'unicode')  native2unicode(hex2dec({'89' 'e3'}), 'unicode')  native2unicode(hex2dec({'4e' '86'}), 'unicode')  native2unicode(hex2dec({'97' '59'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'67' '61'}), 'unicode')  native2unicode(hex2dec({'4e' 'f6'}), 'unicode')  native2unicode(hex2dec({'4e' '0b'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'57' '3a'}), 'unicode')  native2unicode(hex2dec({'54' '8c'}), 'unicode')  native2unicode(hex2dec({'56' '68'}), 'unicode')  native2unicode(hex2dec({'4e' 'f6'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'5b' 'b9'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode') ]);

model.param.label('Parameters 1');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 3);

model.component('comp1').label('Component 1');

model.result.table.create('tbl1', 'Table');

model.component('comp1').mesh.create('mesh1');

model.component('comp1').geom('geom1').label('Geometry 1');
model.component('comp1').geom('geom1').lengthUnit('cm');
model.component('comp1').geom('geom1').geomRep('comsol');
model.component('comp1').geom('geom1').create('cyl1', 'Cylinder');
model.component('comp1').geom('geom1').feature('cyl1').label('Cylinder 1');
model.component('comp1').geom('geom1').feature('cyl1').set('r', 20);
model.component('comp1').geom('geom1').feature('cyl1').set('h', 20);
model.component('comp1').geom('geom1').create('cyl2', 'Cylinder');
model.component('comp1').geom('geom1').feature('cyl2').label('Cylinder 2');
model.component('comp1').geom('geom1').feature('cyl2').set('r', 10);
model.component('comp1').geom('geom1').feature('cyl2').set('h', 4);
model.component('comp1').geom('geom1').feature('cyl2').set('pos', [0 0 8]);
model.component('comp1').geom('geom1').feature('cyl2').set('layername', {'Layer 1'});
model.component('comp1').geom('geom1').feature('cyl2').setIndex('layer', '5[mm]', 0);
model.component('comp1').geom('geom1').feature('cyl2').set('layerside', false);
model.component('comp1').geom('geom1').feature('cyl2').set('layerbottom', true);
model.component('comp1').geom('geom1').feature('cyl2').set('layertop', true);
model.component('comp1').geom('geom1').create('cyl3', 'Cylinder');
model.component('comp1').geom('geom1').feature('cyl3').label('Cylinder 3');
model.component('comp1').geom('geom1').feature('cyl3').set('r', 0.75);
model.component('comp1').geom('geom1').feature('cyl3').set('h', 8);
model.component('comp1').geom('geom1').create('cyl4', 'Cylinder');
model.component('comp1').geom('geom1').feature('cyl4').label('Cylinder 4');
model.component('comp1').geom('geom1').feature('cyl4').set('r', 0.75);
model.component('comp1').geom('geom1').feature('cyl4').set('h', 8);
model.component('comp1').geom('geom1').feature('cyl4').set('pos', [0 0 12]);
model.component('comp1').geom('geom1').feature('fin').label('Form Union');
model.component('comp1').geom('geom1').run;

model.component('comp1').selection.create('sel1', 'Explicit');
model.component('comp1').selection('sel1').set([2 4 5 6]);
model.component('comp1').selection.create('com1', 'Complement');
model.component('comp1').selection.create('sel2', 'Explicit');
model.component('comp1').selection('sel2').geom('geom1', 3, 2, {'exterior'});
model.component('comp1').selection('sel2').set([2 5]);
model.component('comp1').selection.create('sel3', 'Explicit');
model.component('comp1').selection('sel3').geom('geom1', 3, 2, {'exterior'});
model.component('comp1').selection('sel3').set([4 6]);
model.component('comp1').selection('sel1').label('Metal');
model.component('comp1').selection('com1').label('Insulators');
model.component('comp1').selection('com1').set('input', {'sel1'});
model.component('comp1').selection('sel2').label('Ground');
model.component('comp1').selection('sel3').label('Terminal');

model.component('comp1').view('view1').hideEntities.create('hide1');
model.component('comp1').view('view1').hideEntities('hide1').geom('geom1', 2);
model.component('comp1').view('view1').hideEntities('hide1').set([1 4 23]);
model.view.create('view2', 2);

model.component('comp1').material.create('mat1', 'Common');
model.component('comp1').material('mat1').selection.set([]);
model.component('comp1').material('mat1').propertyGroup.create('RefractiveIndex', 'RefractiveIndex', 'Refractive index');
model.component('comp1').material('mat1').selection.set([3]);

model.component('comp1').physics.create('es', 'Electrostatics', 'geom1');
model.component('comp1').physics('es').selection.named('com1');
model.component('comp1').physics('es').create('ccns1', 'ChargeConservationSolid', 3);
model.component('comp1').physics('es').feature('ccns1').selection.set([3]);
model.component('comp1').physics('es').create('gnd1', 'Ground', 2);
model.component('comp1').physics('es').feature('gnd1').selection.named('sel2');
model.component('comp1').physics('es').create('term1', 'Terminal', 2);
model.component('comp1').physics('es').feature('term1').selection.named('sel3');

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
model.component('comp1').view('view1').hideEntities('hide1').label('Hide for Physics 1');
model.view('view2').label('View 2D 2');
model.view('view2').axis.label('Axis');
model.view('view2').axis.set('xmin', -22.000001907348633);
model.view('view2').axis.set('xmax', 22.000001907348633);
model.view('view2').axis.set('ymin', -4.612143516540527);
model.view('view2').axis.set('ymax', 24.612144470214844);

model.material.label('Materials');
model.component('comp1').material('mat1').label('Glass (quartz)');
model.component('comp1').material('mat1').set('family', 'custom');
model.component('comp1').material('mat1').set('diffuse', 'custom');
model.component('comp1').material('mat1').set('ambient', 'custom');
model.component('comp1').material('mat1').set('noise', true);
model.component('comp1').material('mat1').set('fresnel', 0.99);
model.component('comp1').material('mat1').set('roughness', 0.02);
model.component('comp1').material('mat1').set('diffusewrap', 0);
model.component('comp1').material('mat1').set('reflectance', 0);
model.component('comp1').material('mat1').propertyGroup('def').label('Basic');
model.component('comp1').material('mat1').propertyGroup('def').set('relpermeability', {'1' '0' '0' '0' '1' '0' '0' '0' '1'});
model.component('comp1').material('mat1').propertyGroup('def').set('electricconductivity', {'1e-14[S/m]' '0' '0' '0' '1e-14[S/m]' '0' '0' '0' '1e-14[S/m]'});
model.component('comp1').material('mat1').propertyGroup('def').set('relpermittivity', {'4.2' '0' '0' '0' '4.2' '0' '0' '0' '4.2'});
model.component('comp1').material('mat1').propertyGroup('def').set('density', '2210[kg/m^3]');
model.component('comp1').material('mat1').propertyGroup('def').set('thermalconductivity', {'1.4[W/(m*K)]' '0' '0' '0' '1.4[W/(m*K)]' '0' '0' '0' '1.4[W/(m*K)]'});
model.component('comp1').material('mat1').propertyGroup('def').set('heatcapacity', '730[J/(kg*K)]');
model.component('comp1').material('mat1').propertyGroup('RefractiveIndex').label('Refractive index');
model.component('comp1').material('mat1').propertyGroup('RefractiveIndex').info('category').label('Information');
model.component('comp1').material('mat1').propertyGroup('RefractiveIndex').set('n', {'1.5' '0' '0' '0' '1.5' '0' '0' '0' '1.5'});

model.component('comp1').coordSystem('sys1').label('Boundary System 1');

model.common('cminpt').label('Default Model Inputs');

model.component('comp1').physics('es').label('Electrostatics');
model.component('comp1').physics('es').feature('fsp1').label('Free Space 1');
model.component('comp1').physics('es').feature('fsp1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('zc1').label('Zero Charge 1');
model.component('comp1').physics('es').feature('zc1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('init1').label('Initial Values 1');
model.component('comp1').physics('es').feature('init1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('ccns1').label('Charge Conservation in Solids 1');
model.component('comp1').physics('es').feature('ccns1').feature('ddis1').label('Dispersion 1');
model.component('comp1').physics('es').feature('ccns1').feature('ddis1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('ccns1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('gnd1').label('Ground 1');
model.component('comp1').physics('es').feature('gnd1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('term1').set('TerminalType', 'Voltage');
model.component('comp1').physics('es').feature('term1').label('Boundary Terminal 1');
model.component('comp1').physics('es').feature('term1').featureInfo('info').label('Equation View');

model.component('comp1').mesh('mesh1').label('Mesh 1');
model.component('comp1').mesh('mesh1').contribute('geom/detail', true);

model.study.create('std1');
model.study('std1').create('stat', 'Stationary');

model.sol.create('sol1');
model.sol('sol1').attach('std1');

model.result.dataset.create('dset2', 'Solution');
model.result.dataset.create('cpl1', 'CutPlane');
model.result.dataset('dset2').selection.named('sel1');
model.result.numerical.create('gev1', 'EvalGlobal');
model.result.create('pg1', 'PlotGroup3D');
model.result.create('pg2', 'PlotGroup2D');
model.result('pg1').create('surf1', 'Surface');
model.result('pg1').create('slc1', 'Slice');
model.result('pg1').create('arwv1', 'ArrowVolume');
model.result('pg1').feature('surf1').set('data', 'dset2');
model.result('pg1').feature('slc1').set('expr', 'es.normE');
model.result('pg1').feature('arwv1').create('col1', 'Color');
model.result('pg2').create('con1', 'Contour');
model.result('pg2').create('con2', 'Contour');

model.study('std1').label('Study 1');
model.study('std1').feature('stat').label('Stationary');

model.batch.label('Batch');

model.sol('sol1').createAutoSequence('std1');
model.sol('sol1').label('Solution 1');

model.study('std1').runNoGen;

model.result.label('Results');
model.result.dataset('cpl1').label('Cut Plane 1');
model.result.numerical('gev1').label('Global Evaluation 1');
model.result.numerical('gev1').set('table', 'tbl1');
model.result.numerical('gev1').set('expr', {'es.C11'});
model.result.numerical('gev1').set('unit', {'F'});
model.result.numerical('gev1').set('descr', {'Maxwell capacitance'});
model.result.numerical('gev1').setResult;
model.result('pg1').label('3D Plot Group 1');
model.result('pg1').feature('surf1').label('Surface 1');
model.result('pg1').feature('surf1').set('descr', 'Electric potential');
model.result('pg1').feature('surf1').set('coloring', 'uniform');
model.result('pg1').feature('surf1').set('color', 'gray');
model.result('pg1').feature('surf1').set('evaluationsettings', 'parent');
model.result('pg1').feature('surf1').set('resolution', 'normal');
model.result('pg1').feature('slc1').label('Slice 1');
model.result('pg1').feature('slc1').set('descr', 'Electric field norm');
model.result('pg1').feature('slc1').set('quickxnumber', 1);
model.result('pg1').feature('slc1').set('colortable', 'RainbowLight');
model.result('pg1').feature('slc1').set('evaluationsettings', 'parent');
model.result('pg1').feature('slc1').set('resolution', 'normal');
model.result('pg1').feature('arwv1').label('Arrow Volume 1');
model.result('pg1').feature('arwv1').set('descr', 'Electric field');
model.result('pg1').feature('arwv1').set('xnumber', 1);
model.result('pg1').feature('arwv1').set('ynumber', 24);
model.result('pg1').feature('arwv1').set('znumber', 11);
model.result('pg1').feature('arwv1').set('evaluationsettings', 'parent');
model.result('pg1').feature('arwv1').set('arrowlength', 'logarithmic');
model.result('pg1').feature('arwv1').set('scale', 0.11093332036270957);
model.result('pg1').feature('arwv1').set('scaleactive', false);
model.result('pg1').feature('arwv1').feature('col1').label('Color Expression 1');
model.result('pg1').feature('arwv1').feature('col1').set('descr', 'Electric potential');
model.result('pg1').feature('arwv1').feature('col1').set('colorlegend', false);
model.result('pg2').label('2D Plot Group 2');
model.result('pg2').feature('con1').label('Contour 1');
model.result('pg2').feature('con1').set('descr', 'Electric potential');
model.result('pg2').feature('con1').set('levelmethod', 'levels');
model.result('pg2').feature('con1').set('levels', 'range(0.1,0.1,0.9)');
model.result('pg2').feature('con1').set('contourtype', 'filled');
model.result('pg2').feature('con1').set('colortable', 'RainbowLight');
model.result('pg2').feature('con1').set('evaluationsettings', 'parent');
model.result('pg2').feature('con1').set('resolution', 'normal');
model.result('pg2').feature('con2').label('Contour 2');
model.result('pg2').feature('con2').set('descr', 'Electric potential');
model.result('pg2').feature('con2').set('titletype', 'none');
model.result('pg2').feature('con2').set('levelmethod', 'levels');
model.result('pg2').feature('con2').set('levels', 'range(0,0.1,1)');
model.result('pg2').feature('con2').set('contourlabels', true);
model.result('pg2').feature('con2').set('coloring', 'uniform');
model.result('pg2').feature('con2').set('colorlegend', false);
model.result('pg2').feature('con2').set('color', 'black');
model.result('pg2').feature('con2').set('evaluationsettings', 'parent');
model.result('pg2').feature('con2').set('resolution', 'normal');

out = model;
