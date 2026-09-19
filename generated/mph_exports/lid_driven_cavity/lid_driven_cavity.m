function out = model
%
% lid_driven_cavity.m
%
% Model exported on Aug 25 2026, 17:35 by COMSOL 6.4.0.293.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath(['D:\' native2unicode(hex2dec({'68' '4c'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode') '\codex\' native2unicode(hex2dec({'68' '48'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'4e' '0b'}), 'unicode')  native2unicode(hex2dec({'8f' '7d'}), 'unicode') '\COMSOL\' native2unicode(hex2dec({'98' '76'}), 'unicode')  native2unicode(hex2dec({'76' 'd6'}), 'unicode')  native2unicode(hex2dec({'9a' '71'}), 'unicode')  native2unicode(hex2dec({'52' 'a8'}), 'unicode')  native2unicode(hex2dec({'65' 'b9'}), 'unicode')  native2unicode(hex2dec({'81' '54'}), 'unicode')  native2unicode(hex2dec({'6d' '41'}), 'unicode') ]);

model.label('lid_driven_cavity.mph');

model.title([]);

model.description('');

model.baseSystem('none');

model.param.set('Re', '10000', 'Reynolds number');
model.param.set('xR', '1-0.1328', 'x-coordinate for right vortex');
model.param.set('yR', '0.1484', 'y-coordinate for right vortex');
model.param.set('xL', '0.0781', 'x-coordinate for left vortex');
model.param.set('yL', '0.0781', 'y-coordinate for left vortex');
model.param.set('xC', '0.6172', 'x-coordinate for center vortex');
model.param.set('yC', '0.7344', 'y-coordinate for center vortex');
model.param.label('Parameters 1');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 2);

model.component('comp1').label('Component 1');

model.result.table.create('tbl1', 'Table');
model.result.table.create('tbl2', 'Table');
model.result.table('tbl1').importData('lid_driven_cavity_literature1.txt');
model.result.table('tbl2').importData('lid_driven_cavity_literature2.txt');

model.component('comp1').mesh.create('mesh1');

model.component('comp1').geom('geom1').label('Geometry 1');
model.component('comp1').geom('geom1').create('sq1', 'Square');
model.component('comp1').geom('geom1').feature('sq1').label('Square 1');
model.component('comp1').geom('geom1').feature('fin').label('Form Union');
model.component('comp1').geom('geom1').run;

model.component('comp1').material.create('mat1', 'Common');

model.component('comp1').physics.create('spf', 'LaminarFlow', 'geom1');
model.component('comp1').physics('spf').create('wallbc2', 'WallBC', 1);
model.component('comp1').physics('spf').feature('wallbc2').selection.set([3]);
model.component('comp1').physics('spf').create('prpc1', 'PressurePointConstraint', 0);
model.component('comp1').physics('spf').feature('prpc1').selection.set([1]);

model.component('comp1').mesh('mesh1').create('map1', 'Map');
model.component('comp1').mesh('mesh1').feature('map1').create('dis1', 'Distribution');
model.component('comp1').mesh('mesh1').feature('map1').feature('dis1').selection.all;

model.result.table('tbl1').label('Table 1');
model.result.table('tbl2').label('Table 2');

model.thermodynamics.label('Thermodynamics');

model.component('comp1').view('view1').label('View 1');
model.component('comp1').view('view1').axis.label('Axis');
model.component('comp1').view('view1').axis.set('xmin', -0.24381932616233826);
model.component('comp1').view('view1').axis.set('xmax', 1.243819236755371);
model.component('comp1').view('view1').axis.set('ymin', -0.02499999850988388);
model.component('comp1').view('view1').axis.set('ymax', 1.024999976158142);

model.material.label('Materials');
model.component('comp1').material('mat1').label('Material 1');
model.component('comp1').material('mat1').propertyGroup('def').label('Basic');
model.component('comp1').material('mat1').propertyGroup('def').set('density', '1');
model.component('comp1').material('mat1').propertyGroup('def').set('dynamicviscosity', '1/Re');

model.component('comp1').coordSystem('sys1').label('Boundary System 1');

model.common('cminpt').label('Default Model Inputs');

model.component('comp1').physics('spf').label('Laminar Flow');
model.component('comp1').physics('spf').prop('PhysicalModelProperty').set('textCompressibilityMixtureModel', 'The Mixture Model multiphysics coupling is restricted to incompressible flow');
model.component('comp1').physics('spf').prop('PhysicalModelProperty').set('textCompressibilityMixtureModel2', 'The Incompressible flow option is not available for the Mixture Model multiphysics coupling');
model.component('comp1').physics('spf').prop('TurbulenceModelProperty').set('c4_PS_om', '((9*0.52)+6)/11');
model.component('comp1').physics('spf').prop('TurbulenceModelProperty').set('c5_PS_om', '(10-(7*0.52))/11');
model.component('comp1').physics('spf').feature('fp1').label('Fluid Properties 1');
model.component('comp1').physics('spf').feature('fp1').featureInfo('info').label('Equation View');
model.component('comp1').physics('spf').feature('init1').label('Initial Values 1');
model.component('comp1').physics('spf').feature('init1').featureInfo('info').label('Equation View');
model.component('comp1').physics('spf').feature('wallbc1').set('zeta', '(-0.1)[V]');
model.component('comp1').physics('spf').feature('wallbc1').label('Wall 1');
model.component('comp1').physics('spf').feature('wallbc1').featureInfo('info').label('Equation View');
model.component('comp1').physics('spf').feature('grav1').label('Gravity 1');
model.component('comp1').physics('spf').feature('grav1').featureInfo('info').label('Equation View');
model.component('comp1').physics('spf').feature('dcont1').label('Flow Continuity 1');
model.component('comp1').physics('spf').feature('dcont1').featureInfo('info').label('Equation View');
model.component('comp1').physics('spf').feature('wallbc2').set('zeta', '(-0.1)[V]');
model.component('comp1').physics('spf').feature('wallbc2').set('uvw', 1);
model.component('comp1').physics('spf').feature('wallbc2').set('SlidingWall', true);
model.component('comp1').physics('spf').feature('wallbc2').label('Wall 2');
model.component('comp1').physics('spf').feature('wallbc2').featureInfo('info').label('Equation View');
model.component('comp1').physics('spf').feature('prpc1').label('Pressure Point Constraint 1');
model.component('comp1').physics('spf').feature('prpc1').featureInfo('info').label('Equation View');
model.component('comp1').physics('spf').feature('rtfr1').label('Rotating Frame 1');

model.component('comp1').mesh('mesh1').label('Mesh 1');
model.component('comp1').mesh('mesh1').feature('size').label('Size');
model.component('comp1').mesh('mesh1').feature('map1').label('Mapped 1');
model.component('comp1').mesh('mesh1').feature('map1').feature('dis1').label('Distribution 1');
model.component('comp1').mesh('mesh1').feature('map1').feature('dis1').set('type', 'predefined');
model.component('comp1').mesh('mesh1').feature('map1').feature('dis1').set('elemcount', 100);
model.component('comp1').mesh('mesh1').feature('map1').feature('dis1').set('elemratio', 5);
model.component('comp1').mesh('mesh1').feature('map1').feature('dis1').set('growthrate', 'exponential');
model.component('comp1').mesh('mesh1').feature('map1').feature('dis1').set('symmetric', true);
model.component('comp1').mesh('mesh1').run;

model.study.create('std1');
model.study('std1').create('stat', 'Stationary');

model.sol.create('sol1');
model.sol('sol1').attach('std1');
model.sol('sol1').create('st1', 'StudyStep');
model.sol('sol1').create('v1', 'Variables');
model.sol('sol1').create('s1', 'Stationary');
model.sol('sol1').feature('s1').create('p1', 'Parametric');
model.sol('sol1').feature('s1').create('fc1', 'FullyCoupled');
model.sol('sol1').feature('s1').create('d1', 'Direct');
model.sol('sol1').feature('s1').create('i1', 'Iterative');
model.sol('sol1').feature('s1').feature('i1').create('mg1', 'Multigrid');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('pr').create('sc1', 'SCGS');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('po').create('sc1', 'SCGS');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('cs').create('d1', 'Direct');
model.sol('sol1').feature('s1').feature.remove('fcDef');

model.result.dataset.create('cln1', 'CutLine2D');
model.result.dataset.create('cln2', 'CutLine2D');
model.result.create('pg1', 'PlotGroup2D');
model.result.create('pg2', 'PlotGroup2D');
model.result.create('pg3', 'PlotGroup1D');
model.result.create('pg4', 'PlotGroup1D');
model.result.create('pg5', 'PlotGroup2D');
model.result('pg1').create('surf1', 'Surface');
model.result('pg1').create('arws1', 'ArrowSurface');
model.result('pg2').create('con1', 'Contour');
model.result('pg2').feature('con1').set('expr', 'p');
model.result('pg3').create('lngr1', 'LineGraph');
model.result('pg3').create('tblp1', 'Table');
model.result('pg3').feature('lngr1').set('expr', 'u');
model.result('pg4').create('lngr1', 'LineGraph');
model.result('pg4').create('tblp1', 'Table');
model.result('pg4').feature('lngr1').set('expr', 'v');
model.result('pg5').create('str1', 'Streamline');
model.result('pg5').create('ann1', 'Annotation');
model.result('pg5').create('ann2', 'Annotation');
model.result('pg5').create('ann3', 'Annotation');
model.result('pg5').create('ann4', 'Annotation');
model.result('pg5').create('ann5', 'Annotation');

model.study('std1').label('Study 1');
model.study('std1').feature('stat').label('Stationary');
model.study('std1').feature('stat').set('useparam', true);
model.study('std1').feature('stat').set('pname', {'Re'});
model.study('std1').feature('stat').set('plistarr', {'100 400 1000 3200 5000 7500 10000'});
model.study('std1').feature('stat').set('punit', {''});

model.batch.label('Batch');

model.sol('sol1').label('Solution 1');
model.sol('sol1').feature('st1').label([native2unicode(hex2dec({'7f' '16'}), 'unicode')  native2unicode(hex2dec({'8b' 'd1'}), 'unicode')  native2unicode(hex2dec({'65' 'b9'}), 'unicode')  native2unicode(hex2dec({'7a' '0b'}), 'unicode') ': Stationary']);
model.sol('sol1').feature('v1').label('Dependent Variables 1');
model.sol('sol1').feature('v1').set('clistctrl', {'p1'});
model.sol('sol1').feature('v1').set('cname', {'Re'});
model.sol('sol1').feature('v1').set('clist', {'100 400 1000 3200 5000 7500 10000'});
model.sol('sol1').feature('s1').label('Stationary Solver 1');
model.sol('sol1').feature('s1').set('probesel', 'none');
model.sol('sol1').feature('s1').feature('dDef').label('Direct');
model.sol('sol1').feature('s1').feature('aDef').label('Advanced');
model.sol('sol1').feature('s1').feature('aDef').set('cachepattern', true);
model.sol('sol1').feature('s1').feature('p1').label('Parametric 1');
model.sol('sol1').feature('s1').feature('p1').set('pname', {'Re'});
model.sol('sol1').feature('s1').feature('p1').set('plistarr', {'100 400 1000 3200 5000 7500 10000'});
model.sol('sol1').feature('s1').feature('p1').set('punit', {''});
model.sol('sol1').feature('s1').feature('p1').set('excludelsqvalues', false);
model.sol('sol1').feature('s1').feature('fc1').label('Fully Coupled 1');
model.sol('sol1').feature('s1').feature('fc1').set('linsolver', 'd1');
model.sol('sol1').feature('s1').feature('fc1').set('initstep', 0.01);
model.sol('sol1').feature('s1').feature('fc1').set('maxiter', 100);
model.sol('sol1').feature('s1').feature('d1').label('Direct, fluid flow variables (spf)');
model.sol('sol1').feature('s1').feature('d1').set('linsolver', 'pardiso');
model.sol('sol1').feature('s1').feature('d1').set('pivotperturb', 1.0E-13);
model.sol('sol1').feature('s1').feature('i1').label('AMG, fluid flow variables (spf)');
model.sol('sol1').feature('s1').feature('i1').set('nlinnormuse', true);
model.sol('sol1').feature('s1').feature('i1').set('maxlinit', 1000);
model.sol('sol1').feature('s1').feature('i1').set('rhob', 75);
model.sol('sol1').feature('s1').feature('i1').feature('ilDef').label('Incomplete LU');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').label('Multigrid 1');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').set('prefun', 'saamg');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').set('maxcoarsedof', 80000);
model.sol('sol1').feature('s1').feature('i1').feature('mg1').set('strconn', 0.02);
model.sol('sol1').feature('s1').feature('i1').feature('mg1').set('saamgcompwise', true);
model.sol('sol1').feature('s1').feature('i1').feature('mg1').set('usesmooth', false);
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('pr').label('Presmoother');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('pr').feature('soDef').label('SOR 1');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('pr').feature('sc1').label('SCGS 1.1');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('pr').feature('sc1').set('linesweeptype', 'ssor');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('pr').feature('sc1').set('iter', 0);
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('po').label('Postsmoother');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('po').feature('soDef').label('SOR 1');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('po').feature('sc1').label('SCGS 1.1');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('po').feature('sc1').set('linesweeptype', 'ssor');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('po').feature('sc1').set('iter', 1);
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('cs').label('Coarse Solver');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('cs').feature('dDef').label('Direct');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('cs').feature('d1').label('Direct 1');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('cs').feature('d1').set('linsolver', 'pardiso');
model.sol('sol1').feature('s1').feature('i1').feature('mg1').feature('cs').feature('d1').set('pivotperturb', 1.0E-13);

model.study('std1').runNoGen;

model.result.label('Results');
model.result.dataset('cln1').label('Cut Line 2D 1');
model.result.dataset('cln1').set('genpoints', {'.5' '0'; '.5' '1'});
model.result.dataset('cln2').label('Cut Line 2D 2');
model.result.dataset('cln2').set('genpoints', {'0' '.5'; '1' '.5'});
model.result('pg1').label('Velocity (spf)');
model.result('pg1').set('frametype', 'spatial');
model.result('pg1').set('smooth', 'internal');
model.result('pg1').feature('surf1').label('Surface');
model.result('pg1').feature('surf1').set('descr', 'Velocity magnitude');
model.result('pg1').feature('surf1').set('smooth', 'internal');
model.result('pg1').feature('surf1').set('resolution', 'normal');
model.result('pg1').feature('arws1').label('Arrow Surface 1');
model.result('pg1').feature('arws1').set('descr', 'Velocity field');
model.result('pg1').feature('arws1').set('scale', 0.0868417698113757);
model.result('pg1').feature('arws1').set('color', 'white');
model.result('pg1').feature('arws1').set('scaleactive', false);
model.result('pg2').label('Pressure (spf)');
model.result('pg2').set('frametype', 'spatial');
model.result('pg2').set('smooth', 'internal');
model.result('pg2').feature('con1').label('Contour');
model.result('pg2').feature('con1').set('descr', 'Pressure');
model.result('pg2').feature('con1').set('number', 40);
model.result('pg2').feature('con1').set('levelrounding', false);
model.result('pg2').feature('con1').set('smooth', 'internal');
model.result('pg2').feature('con1').set('resolution', 'normal');
model.result('pg3').label('u vs. y');
model.result('pg3').set('data', 'cln1');
model.result('pg3').set('ylabel', 'Velocity field, x-component');
model.result('pg3').set('legendpos', 'upperleft');
model.result('pg3').set('smooth', 'internal');
model.result('pg3').set('ylabelactive', false);
model.result('pg3').feature('lngr1').label('Line Graph 1');
model.result('pg3').feature('lngr1').set('descr', 'Velocity field, x-component');
model.result('pg3').feature('lngr1').set('linewidth', 'preference');
model.result('pg3').feature('lngr1').set('legend', true);
model.result('pg3').feature('lngr1').set('resolution', 'normal');
model.result('pg3').feature('tblp1').label('Table Graph 1');
model.result('pg3').feature('tblp1').set('linestyle', 'none');
model.result('pg3').feature('tblp1').set('linewidth', 'preference');
model.result('pg3').feature('tblp1').set('linemarker', 'cycle');
model.result('pg3').feature('tblp1').set('markerpos', 'datapoints');
model.result('pg4').label('v vs. x');
model.result('pg4').set('data', 'cln2');
model.result('pg4').set('ylabel', 'Velocity field, y-component');
model.result('pg4').set('smooth', 'internal');
model.result('pg4').set('ylabelactive', false);
model.result('pg4').feature('lngr1').label('Line Graph 1');
model.result('pg4').feature('lngr1').set('descr', 'Velocity field, y-component');
model.result('pg4').feature('lngr1').set('linewidth', 'preference');
model.result('pg4').feature('lngr1').set('legend', true);
model.result('pg4').feature('lngr1').set('resolution', 'normal');
model.result('pg4').feature('tblp1').label('Table Graph 1');
model.result('pg4').feature('tblp1').set('table', 'tbl2');
model.result('pg4').feature('tblp1').set('linestyle', 'none');
model.result('pg4').feature('tblp1').set('linewidth', 'preference');
model.result('pg4').feature('tblp1').set('linemarker', 'cycle');
model.result('pg4').feature('tblp1').set('markerpos', 'datapoints');
model.result('pg5').label('Streamline Plot');
model.result('pg5').set('looplevel', [1]);
model.result('pg5').set('smooth', 'internal');
model.result('pg5').feature('str1').label('Streamline 1');
model.result('pg5').feature('str1').set('descr', 'Velocity field');
model.result('pg5').feature('str1').set('posmethod', 'uniform');
model.result('pg5').feature('str1').set('udensity', 7.8);
model.result('pg5').feature('str1').set('resolution', 'normal');
model.result('pg5').feature('ann1').label('Annotation 1');
model.result('pg5').feature('ann1').set('text', 'Center');
model.result('pg5').feature('ann1').set('posxexpr', 'xC');
model.result('pg5').feature('ann1').set('posyexpr', 'yC');
model.result('pg5').feature('ann2').label('Annotation 2');
model.result('pg5').feature('ann2').set('text', 'Right vortex');
model.result('pg5').feature('ann2').set('posxexpr', 'xR');
model.result('pg5').feature('ann3').label('Annotation 3');
model.result('pg5').feature('ann3').set('text', 'Right vortex');
model.result('pg5').feature('ann3').set('posxexpr', 1);
model.result('pg5').feature('ann3').set('posyexpr', 'yR');
model.result('pg5').feature('ann4').label('Annotation 4');
model.result('pg5').feature('ann4').set('text', 'Left vortex');
model.result('pg5').feature('ann4').set('posyexpr', 'yL');
model.result('pg5').feature('ann5').label('Annotation 5');
model.result('pg5').feature('ann5').set('text', 'Left vortex');
model.result('pg5').feature('ann5').set('posxexpr', 'xL');

out = model;
