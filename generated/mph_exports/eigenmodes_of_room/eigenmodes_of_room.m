function out = model
%
% eigenmodes_of_room.m
%
% Model exported on Aug 25 2026, 17:53 by COMSOL 6.4.0.293.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath(['D:\' native2unicode(hex2dec({'68' '4c'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode') '\codex\' native2unicode(hex2dec({'68' '48'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'4e' '0b'}), 'unicode')  native2unicode(hex2dec({'8f' '7d'}), 'unicode') '\COMSOL\' native2unicode(hex2dec({'62' '3f'}), 'unicode')  native2unicode(hex2dec({'95' 'f4'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'72' '79'}), 'unicode')  native2unicode(hex2dec({'5f' '81'}), 'unicode')  native2unicode(hex2dec({'6a' '21'}), 'unicode')  native2unicode(hex2dec({'60' '01'}), 'unicode') ]);

model.label('eigenmodes_of_room.mph');

model.title([native2unicode(hex2dec({'62' '3f'}), 'unicode')  native2unicode(hex2dec({'95' 'f4'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'72' '79'}), 'unicode')  native2unicode(hex2dec({'5f' '81'}), 'unicode')  native2unicode(hex2dec({'6a' '21'}), 'unicode')  native2unicode(hex2dec({'60' '01'}), 'unicode') ]);

model.description([native2unicode(hex2dec({'67' '2c'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'6a' '21'}), 'unicode')  native2unicode(hex2dec({'62' 'df'}), 'unicode')  native2unicode(hex2dec({'5e' '26'}), 'unicode')  native2unicode(hex2dec({'5b' 'b6'}), 'unicode')  native2unicode(hex2dec({'51' '77'}), 'unicode')  native2unicode(hex2dec({'62' '3f'}), 'unicode')  native2unicode(hex2dec({'95' 'f4'}), 'unicode')  native2unicode(hex2dec({'51' '85'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'58' 'f0'}), 'unicode')  native2unicode(hex2dec({'9a' '7b'}), 'unicode')  native2unicode(hex2dec({'6c' 'e2'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'51' '76'}), 'unicode')  native2unicode(hex2dec({'72' '79'}), 'unicode')  native2unicode(hex2dec({'5f' '81'}), 'unicode')  native2unicode(hex2dec({'6a' '21'}), 'unicode')  native2unicode(hex2dec({'60' '01'}), 'unicode')  native2unicode(hex2dec({'4e' '0e'}), 'unicode')  native2unicode(hex2dec({'7a' '7a'}), 'unicode')  native2unicode(hex2dec({'62' '3f'}), 'unicode')  native2unicode(hex2dec({'95' 'f4'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'7c' 'be'}), 'unicode')  native2unicode(hex2dec({'78' '6e'}), 'unicode')  native2unicode(hex2dec({'89' 'e3'}), 'unicode')  native2unicode(hex2dec({'75' '65'}), 'unicode')  native2unicode(hex2dec({'67' '09'}), 'unicode')  native2unicode(hex2dec({'4e' '0d'}), 'unicode')  native2unicode(hex2dec({'54' '0c'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode') ]);

model.param.label('Parameters 1');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 3);

model.component('comp1').label('Component 1');

model.result.evaluationGroup.create('std1EvgFrq', 'EvaluationGroup');
model.result.evaluationGroup('std1EvgFrq').create('gev1', 'EvalGlobal');

model.component('comp1').mesh.create('mesh1');

model.component('comp1').geom('geom1').label('Geometry 1');
model.component('comp1').geom('geom1').geomRep('comsol');
model.component('comp1').geom('geom1').create('imp1', 'Import');
model.component('comp1').geom('geom1').feature('imp1').label('Import 1');
model.component('comp1').geom('geom1').feature('imp1').set('type', 'native');
model.component('comp1').geom('geom1').feature('imp1').set('filename', 'eigenmodes_of_room.mphbin');
model.component('comp1').geom('geom1').feature('fin').label('Form Union');
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');

model.component('comp1').physics.create('acpr', 'PressureAcoustics', 'geom1');

model.component('comp1').mesh('mesh1').create('ftet1', 'FreeTet');

model.thermodynamics.label('Thermodynamics');

model.frame('material1').label('Moving Mesh 1');

model.component('comp1').view('view1').label('View 1');
model.component('comp1').view('view1').set('renderwireframe', true);
model.component('comp1').view('view1').axis.label('Axis');
model.component('comp1').view('view1').light('lgt1').label('Directional Light 1');
model.component('comp1').view('view1').light('lgt2').label('Directional Light 2');
model.component('comp1').view('view1').light('lgt3').label('Directional Light 3');

model.material.label('Materials');
model.component('comp1').material('mat1').label('Air');
model.component('comp1').material('mat1').propertyGroup('def').label('Basic');
model.component('comp1').material('mat1').propertyGroup('def').set('density', '1.25');
model.component('comp1').material('mat1').propertyGroup('def').set('soundspeed', '343');

model.component('comp1').coordSystem('sys1').label('Boundary System 1');

model.common('cminpt').label('Default Model Inputs');

model.component('comp1').physics('acpr').label('Pressure Acoustics, Frequency Domain');
model.component('comp1').physics('acpr').feature('fpam1').label('Pressure Acoustics 1');
model.component('comp1').physics('acpr').feature('fpam1').featureInfo('info').label('Equation View');
model.component('comp1').physics('acpr').feature('shb1').label('Sound Hard Boundary (Wall) 1');
model.component('comp1').physics('acpr').feature('shb1').featureInfo('info').label('Equation View');
model.component('comp1').physics('acpr').feature('init1').label('Initial Values 1');
model.component('comp1').physics('acpr').feature('init1').featureInfo('info').label('Equation View');
model.component('comp1').physics('acpr').feature('dcont1').label('Continuity 1');
model.component('comp1').physics('acpr').feature('dcont1').featureInfo('info').label('Equation View');

model.component('comp1').mesh('mesh1').label('Mesh 1');
model.component('comp1').mesh('mesh1').feature('size').label('Size');
model.component('comp1').mesh('mesh1').feature('ftet1').label('Free Tetrahedral 1');
model.component('comp1').mesh('mesh1').run;

model.study.create('std1');
model.study('std1').create('eig', 'Eigenfrequency');

model.sol.create('sol1');
model.sol('sol1').attach('std1');

model.result.dataset('dset1').selection.geom('geom1', 2);
model.result.dataset('dset1').selection.set([3 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]);
model.result.create('pg1', 'PlotGroup3D');
model.result.create('pg2', 'PlotGroup3D');
model.result.create('pg3', 'PlotGroup3D');
model.result.create('pg4', 'PlotGroup3D');
model.result('pg1').create('surf1', 'Surface');
model.result('pg1').create('con1', 'Contour');
model.result('pg2').create('surf1', 'Surface');
model.result('pg2').feature('surf1').set('expr', 'acpr.Lp_t');
model.result('pg3').create('iso1', 'Isosurface');
model.result('pg3').create('surf1', 'Surface');
model.result('pg4').create('surf1', 'Surface');
model.result('pg4').feature('surf1').set('expr', 'acpr.Lp_t');

model.study('std1').label('Study 1');
model.study('std1').feature('eig').label('Eigenfrequency');
model.study('std1').feature('eig').set('shift', '90');
model.study('std1').feature('eig').set('ftplistmethod', 'manual');
model.study('std1').feature('eig').set('filtereigdescription', {'Damped natural frequency'});

model.batch.label('Batch');

model.sol('sol1').createAutoSequence('std1');
model.sol('sol1').label('Solution 1');

model.study('std1').runNoGen;

model.result.label('Results');
model.result.evaluationGroup('std1EvgFrq').label('Eigenfrequencies (Study 1)');
model.result.evaluationGroup('std1EvgFrq').set('data', 'dset1');
model.result.evaluationGroup('std1EvgFrq').set('looplevelinput', {'all'});
model.result.evaluationGroup('std1EvgFrq').feature('gev1').label('Global Evaluation 1');
model.result.evaluationGroup('std1EvgFrq').feature('gev1').set('expr', {'2*pi*freq' 'imag(freq)/abs(freq)' 'abs(freq)/imag(freq)/2'});
model.result.evaluationGroup('std1EvgFrq').feature('gev1').set('unit', {'rad/s' '1' '1'});
model.result.evaluationGroup('std1EvgFrq').feature('gev1').set('descr', {'Angular frequency' 'Damping ratio' 'Quality factor'});
model.result.evaluationGroup('std1EvgFrq').run;
model.result('pg1').label('Acoustic Pressure (acpr)');
model.result('pg1').set('showlegendsunit', true);
model.result('pg1').feature('surf1').label('Surface 1');
model.result('pg1').feature('surf1').set('descr', 'Total acoustic pressure');
model.result('pg1').feature('surf1').set('colortable', 'WaveLight');
model.result('pg1').feature('surf1').set('resolution', 'normal');
model.result('pg1').feature('con1').label('Contour 1');
model.result('pg1').feature('con1').set('descr', 'Total acoustic pressure');
model.result('pg1').feature('con1').set('colorlegend', false);
model.result('pg1').feature('con1').set('resolution', 'normal');
model.result('pg2').label('Sound Pressure Level (acpr)');
model.result('pg2').set('showlegendsunit', true);
model.result('pg2').feature('surf1').label('Surface 1');
model.result('pg2').feature('surf1').set('descr', 'Total sound pressure level');
model.result('pg2').feature('surf1').set('colortable', 'Rainbow');
model.result('pg2').feature('surf1').set('colorscalemode', 'linear');
model.result('pg2').feature('surf1').set('resolution', 'normal');
model.result('pg3').label('Acoustic Pressure, Isosurfaces (acpr)');
model.result('pg3').set('looplevel', [8]);
model.result('pg3').set('showlegendsunit', true);
model.result('pg3').feature('iso1').label('Isosurface 1');
model.result('pg3').feature('iso1').set('descr', 'Total acoustic pressure');
model.result('pg3').feature('iso1').set('colorlegend', false);
model.result('pg3').feature('iso1').set('resolution', 'normal');
model.result('pg3').feature('surf1').label('Surface 1');
model.result('pg3').feature('surf1').set('descr', 'Total acoustic pressure');
model.result('pg3').feature('surf1').set('evaluationsettings', 'parent');
model.result('pg3').feature('surf1').set('resolution', 'normal');
model.result('pg4').label('Sound Pressure Level (acpr) 1');
model.result('pg4').set('showlegendsunit', true);
model.result('pg4').feature('surf1').label('Surface 1');
model.result('pg4').feature('surf1').set('descractive', true);
model.result('pg4').feature('surf1').set('descr', 'Total SPL');
model.result('pg4').feature('surf1').set('colortable', 'Rainbow');
model.result('pg4').feature('surf1').set('colorscalemode', 'linear');
model.result('pg4').feature('surf1').set('resolution', 'normal');

out = model;
