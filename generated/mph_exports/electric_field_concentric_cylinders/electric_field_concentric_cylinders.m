function out = model
%
% electric_field_concentric_cylinders.m
%
% Model exported on Aug 25 2026, 15:44 by COMSOL 6.4.0.293.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath(['D:\' native2unicode(hex2dec({'68' '4c'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode') '\codex\' native2unicode(hex2dec({'68' '48'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'4e' '0b'}), 'unicode')  native2unicode(hex2dec({'8f' '7d'}), 'unicode') '\' native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'6c' '14'}), 'unicode') '\' native2unicode(hex2dec({'54' '0c'}), 'unicode')  native2unicode(hex2dec({'5f' 'c3'}), 'unicode')  native2unicode(hex2dec({'57' '06'}), 'unicode')  native2unicode(hex2dec({'67' 'f1'}), 'unicode')  native2unicode(hex2dec({'4e' '4b'}), 'unicode')  native2unicode(hex2dec({'95' 'f4'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'57' '3a'}), 'unicode') ]);

model.label('electric_field_concentric_cylinders.mph');

model.title([native2unicode(hex2dec({'54' '0c'}), 'unicode')  native2unicode(hex2dec({'5f' 'c3'}), 'unicode')  native2unicode(hex2dec({'57' '06'}), 'unicode')  native2unicode(hex2dec({'67' 'f1'}), 'unicode')  native2unicode(hex2dec({'4e' '4b'}), 'unicode')  native2unicode(hex2dec({'95' 'f4'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'57' '3a'}), 'unicode') ]);

model.description([native2unicode(hex2dec({'8f' 'd9'}), 'unicode')  native2unicode(hex2dec({'4e' '2a'}), 'unicode')  native2unicode(hex2dec({'4e' 'cb'}), 'unicode')  native2unicode(hex2dec({'7e' 'cd'}), 'unicode')  native2unicode(hex2dec({'60' '27'}), 'unicode')  native2unicode(hex2dec({'6a' '21'}), 'unicode')  native2unicode(hex2dec({'57' '8b'}), 'unicode')  native2unicode(hex2dec({'59' '04'}), 'unicode')  native2unicode(hex2dec({'74' '06'}), 'unicode')  native2unicode(hex2dec({'65' '59'}), 'unicode')  native2unicode(hex2dec({'79' 'd1'}), 'unicode')  native2unicode(hex2dec({'4e' '66'}), 'unicode')  native2unicode(hex2dec({'4e' '2d'}), 'unicode')  native2unicode(hex2dec({'5e' '38'}), 'unicode')  native2unicode(hex2dec({'89' 'c1'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'4e' '24'}), 'unicode')  native2unicode(hex2dec({'4e' '2a'}), 'unicode')  native2unicode(hex2dec({'65' 'e0'}), 'unicode')  native2unicode(hex2dec({'96' '50'}), 'unicode')  native2unicode(hex2dec({'95' '7f'}), 'unicode')  native2unicode(hex2dec({'54' '0c'}), 'unicode')  native2unicode(hex2dec({'5f' 'c3'}), 'unicode')  native2unicode(hex2dec({'57' '06'}), 'unicode')  native2unicode(hex2dec({'67' 'f1'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'97' '59'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'95' 'ee'}), 'unicode')  native2unicode(hex2dec({'98' '98'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode')  native2unicode(hex2dec({'75' '31'}), 'unicode')  native2unicode(hex2dec({'4e' '8e'}), 'unicode')  native2unicode(hex2dec({'62' '11'}), 'unicode')  native2unicode(hex2dec({'4e' 'ec'}), 'unicode')  native2unicode(hex2dec({'53' 'ef'}), 'unicode')  native2unicode(hex2dec({'4e' 'e5'}), 'unicode')  native2unicode(hex2dec({'4f' '7f'}), 'unicode')  native2unicode(hex2dec({'75' '28'}), 'unicode')  native2unicode(hex2dec({'89' 'e3'}), 'unicode')  native2unicode(hex2dec({'67' '90'}), 'unicode')  native2unicode(hex2dec({'65' 'b9'}), 'unicode')  native2unicode(hex2dec({'6c' 'd5'}), 'unicode')  native2unicode(hex2dec({'6c' '42'}), 'unicode')  native2unicode(hex2dec({'89' 'e3'}), 'unicode')  native2unicode(hex2dec({'8b' 'e5'}), 'unicode')  native2unicode(hex2dec({'95' 'ee'}), 'unicode')  native2unicode(hex2dec({'98' '98'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'56' 'e0'}), 'unicode')  native2unicode(hex2dec({'6b' '64'}), 'unicode')  native2unicode(hex2dec({'5c' '06'}), 'unicode')  native2unicode(hex2dec({'65' '70'}), 'unicode')  native2unicode(hex2dec({'50' '3c'}), 'unicode')  native2unicode(hex2dec({'4e' 'ff'}), 'unicode')  native2unicode(hex2dec({'77' '1f'}), 'unicode')  native2unicode(hex2dec({'7e' 'd3'}), 'unicode')  native2unicode(hex2dec({'67' '9c'}), 'unicode')  native2unicode(hex2dec({'4e' '0e'}), 'unicode')  native2unicode(hex2dec({'74' '06'}), 'unicode')  native2unicode(hex2dec({'8b' 'ba'}), 'unicode')  native2unicode(hex2dec({'7e' 'd3'}), 'unicode')  native2unicode(hex2dec({'67' '9c'}), 'unicode')  native2unicode(hex2dec({'8f' 'db'}), 'unicode')  native2unicode(hex2dec({'88' '4c'}), 'unicode')  native2unicode(hex2dec({'6b' 'd4'}), 'unicode')  native2unicode(hex2dec({'8f' '83'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode')  native2unicode(hex2dec({'67' '2c'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'80' '03'}), 'unicode')  native2unicode(hex2dec({'86' '51'}), 'unicode')  native2unicode(hex2dec({'4e' '24'}), 'unicode')  native2unicode(hex2dec({'79' 'cd'}), 'unicode')  native2unicode(hex2dec({'60' 'c5'}), 'unicode')  native2unicode(hex2dec({'51' 'b5'}), 'unicode')  native2unicode(hex2dec({'ff' '1a'}), 'unicode')  native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'79' 'cd'}), 'unicode')  native2unicode(hex2dec({'66' '2f'}), 'unicode')  native2unicode(hex2dec({'6b' 'cf'}), 'unicode')  native2unicode(hex2dec({'4e' '2a'}), 'unicode')  native2unicode(hex2dec({'57' '06'}), 'unicode')  native2unicode(hex2dec({'67' 'f1'}), 'unicode')  native2unicode(hex2dec({'90' 'fd'}), 'unicode')  native2unicode(hex2dec({'51' '77'}), 'unicode')  native2unicode(hex2dec({'67' '09'}), 'unicode')  native2unicode(hex2dec({'56' 'fa'}), 'unicode')  native2unicode(hex2dec({'5b' '9a'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'4f' '4d'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'53' 'e6'}), 'unicode')  native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'79' 'cd'}), 'unicode')  native2unicode(hex2dec({'66' '2f'}), 'unicode')  native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'4e' '2a'}), 'unicode')  native2unicode(hex2dec({'57' '06'}), 'unicode')  native2unicode(hex2dec({'67' 'f1'}), 'unicode')  native2unicode(hex2dec({'51' '77'}), 'unicode')  native2unicode(hex2dec({'67' '09'}), 'unicode')  native2unicode(hex2dec({'88' '68'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'83' '77'}), 'unicode')  native2unicode(hex2dec({'5b' 'c6'}), 'unicode')  native2unicode(hex2dec({'5e' 'a6'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'80' '0c'}), 'unicode')  native2unicode(hex2dec({'53' 'e6'}), 'unicode')  native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'4e' '2a'}), 'unicode')  native2unicode(hex2dec({'52' '19'}), 'unicode')  native2unicode(hex2dec({'51' '77'}), 'unicode')  native2unicode(hex2dec({'67' '09'}), 'unicode')  native2unicode(hex2dec({'56' 'fa'}), 'unicode')  native2unicode(hex2dec({'5b' '9a'}), 'unicode')  native2unicode(hex2dec({'75' '35'}), 'unicode')  native2unicode(hex2dec({'4f' '4d'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode') ]);

model.param.set('ri', '0.1[m]', 'Radius of inner cylinder');
model.param.set('ro', '1[m]', 'Radius of outer cylinder');
model.param.set('V0', '100[V]', 'Potential at inner cylinder');
model.param.set('q0', '1e-7[C/m]', 'Charge at inner cylinder');
model.param.label('Parameters 1');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 1);

model.component('comp1').label('Component 1');

model.component('comp1').geom('geom1').axisymmetric(true);

model.component('comp1').mesh.create('mesh1');

model.component('comp1').geom('geom1').label('Geometry 1');
model.component('comp1').geom('geom1').create('i1', 'Interval');
model.component('comp1').geom('geom1').feature('i1').label('Interval 1');
model.component('comp1').geom('geom1').feature('i1').set('coord', {'ri' 'ro'});
model.component('comp1').geom('geom1').feature('fin').label('Form Union');
model.component('comp1').geom('geom1').run;

model.component('comp1').physics.create('es', 'Electrostatics', 'geom1');
model.component('comp1').physics('es').create('gnd1', 'Ground', 0);
model.component('comp1').physics('es').feature('gnd1').selection.set([2]);
model.component('comp1').physics('es').create('pot1', 'ElectricPotential', 0);
model.component('comp1').physics('es').feature('pot1').selection.set([1]);
model.component('comp1').physics.create('es2', 'Electrostatics', 'geom1');
model.component('comp1').physics('es2').create('gnd1', 'Ground', 0);
model.component('comp1').physics('es2').feature('gnd1').selection.set([2]);
model.component('comp1').physics('es2').create('sfcd1', 'SurfaceChargeDensity', 0);
model.component('comp1').physics('es2').feature('sfcd1').selection.set([1]);

model.thermodynamics.label('Thermodynamics');

model.frame('material1').label('Moving Mesh 1');

model.component('comp1').view('view1').label('View 1');
model.component('comp1').view('view1').axis.label('Axis');
model.component('comp1').view('view1').axis.set('xmin', 0.05500003695487976);
model.component('comp1').view('view1').axis.set('xmax', 1.0449999570846558);

model.material.label('Materials');

model.common('cminpt').label('Default Model Inputs');

model.component('comp1').physics('es').label('Electrostatics');
model.component('comp1').physics('es').feature('fsp1').label('Free Space 1');
model.component('comp1').physics('es').feature('fsp1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('axi1').label('Axial Symmetry 1');
model.component('comp1').physics('es').feature('axi1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('zc1').label('Zero Charge 1');
model.component('comp1').physics('es').feature('zc1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('init1').label('Initial Values 1');
model.component('comp1').physics('es').feature('init1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('gnd1').label('Ground 1');
model.component('comp1').physics('es').feature('gnd1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es').feature('pot1').set('V0', 'V0');
model.component('comp1').physics('es').feature('pot1').label('Electric Potential 1');
model.component('comp1').physics('es').feature('pot1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es2').label('Electrostatics 2');
model.component('comp1').physics('es2').feature('fsp1').label('Free Space 1');
model.component('comp1').physics('es2').feature('fsp1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es2').feature('axi1').label('Axial Symmetry 1');
model.component('comp1').physics('es2').feature('axi1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es2').feature('zc1').label('Zero Charge 1');
model.component('comp1').physics('es2').feature('zc1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es2').feature('init1').label('Initial Values 1');
model.component('comp1').physics('es2').feature('init1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es2').feature('gnd1').label('Ground 1');
model.component('comp1').physics('es2').feature('gnd1').featureInfo('info').label('Equation View');
model.component('comp1').physics('es2').feature('sfcd1').set('rhoqs', 'q0/(2*pi*ri)');
model.component('comp1').physics('es2').feature('sfcd1').label('Surface Charge Density 1');
model.component('comp1').physics('es2').feature('sfcd1').featureInfo('info').label('Equation View');

model.component('comp1').mesh('mesh1').label('Mesh 1');

model.study.create('std1');
model.study('std1').create('stat', 'Stationary');

model.sol.create('sol1');
model.sol('sol1').attach('std1');

model.result.create('pg1', 'PlotGroup1D');
model.result.create('pg2', 'PlotGroup1D');
model.result.create('pg3', 'PlotGroup1D');
model.result.create('pg4', 'PlotGroup1D');
model.result('pg1').create('lngr1', 'LineGraph');
model.result('pg1').create('lngr2', 'LineGraph');
model.result('pg1').feature('lngr1').set('xdata', 'expr');
model.result('pg1').feature('lngr1').selection.set([1]);
model.result('pg1').feature('lngr2').set('xdata', 'expr');
model.result('pg1').feature('lngr2').selection.set([1]);
model.result('pg1').feature('lngr2').set('expr', 'V0*log(r/ro)/log(ri/ro)');
model.result('pg2').create('lngr1', 'LineGraph');
model.result('pg2').create('lngr2', 'LineGraph');
model.result('pg2').feature('lngr1').set('xdata', 'expr');
model.result('pg2').feature('lngr1').selection.set([1]);
model.result('pg2').feature('lngr1').set('expr', 'V2');
model.result('pg2').feature('lngr2').set('xdata', 'expr');
model.result('pg2').feature('lngr2').selection.set([1]);
model.result('pg2').feature('lngr2').set('expr', '-q0*log(r/ro)/(2*pi*epsilon0_const)');
model.result('pg3').create('lngr1', 'LineGraph');
model.result('pg3').create('lngr2', 'LineGraph');
model.result('pg3').feature('lngr1').set('xdata', 'expr');
model.result('pg3').feature('lngr1').selection.set([1]);
model.result('pg3').feature('lngr1').set('expr', 'es.Er');
model.result('pg3').feature('lngr2').set('xdata', 'expr');
model.result('pg3').feature('lngr2').selection.set([1]);
model.result('pg3').feature('lngr2').set('expr', '-V0/(r*log(ri/ro))');
model.result('pg4').create('lngr1', 'LineGraph');
model.result('pg4').create('lngr2', 'LineGraph');
model.result('pg4').feature('lngr1').set('xdata', 'expr');
model.result('pg4').feature('lngr1').selection.set([1]);
model.result('pg4').feature('lngr1').set('expr', 'es2.Er');
model.result('pg4').feature('lngr2').set('xdata', 'expr');
model.result('pg4').feature('lngr2').selection.set([1]);
model.result('pg4').feature('lngr2').set('expr', 'q0/(2*pi*epsilon0_const*r)');

model.study('std1').label('Study 1');
model.study('std1').feature('stat').label('Stationary');

model.batch.label('Batch');

model.sol('sol1').createAutoSequence('std1');
model.sol('sol1').label('Solution 1');

model.study('std1').runNoGen;

model.result.label('Results');
model.result('pg1').label('Electric Potential Comparison, Potential');
model.result('pg1').set('titletype', 'label');
model.result('pg1').set('xlabel', 'r-coordinate (m)');
model.result('pg1').set('ylabel', 'Electric potential (V)');
model.result('pg1').set('ylabelactive', true);
model.result('pg1').set('xlabelactive', false);
model.result('pg1').feature('lngr1').label('Line Graph 1');
model.result('pg1').feature('lngr1').set('descr', 'Electric potential');
model.result('pg1').feature('lngr1').set('xdataexpr', 'r');
model.result('pg1').feature('lngr1').set('xdataunit', 'm');
model.result('pg1').feature('lngr1').set('xdatadescr', 'r-coordinate');
model.result('pg1').feature('lngr1').set('legend', true);
model.result('pg1').feature('lngr1').set('autosolution', false);
model.result('pg1').feature('lngr1').set('autodescr', true);
model.result('pg1').feature('lngr1').set('autoexpr', true);
model.result('pg1').feature('lngr1').set('evaluationsettings', 'parent');
model.result('pg1').feature('lngr1').set('resolution', 'normal');
model.result('pg1').feature('lngr2').label('Line Graph 2');
model.result('pg1').feature('lngr2').set('xdataexpr', 'r');
model.result('pg1').feature('lngr2').set('xdataunit', 'm');
model.result('pg1').feature('lngr2').set('xdatadescr', 'r-coordinate');
model.result('pg1').feature('lngr2').set('linewidth', 'preference');
model.result('pg1').feature('lngr2').set('legend', true);
model.result('pg1').feature('lngr2').set('legendmethod', 'manual');
model.result('pg1').feature('lngr2').set('legends', {'Analytical solution'});
model.result('pg1').feature('lngr2').set('evaluationsettings', 'parent');
model.result('pg1').feature('lngr2').set('resolution', 'normal');
model.result('pg2').label('Electric Potential Comparison, Charge Density');
model.result('pg2').set('titletype', 'label');
model.result('pg2').set('xlabel', 'r-coordinate (m)');
model.result('pg2').set('ylabel', 'Electric potential (V)');
model.result('pg2').set('ylabelactive', true);
model.result('pg2').set('xlabelactive', false);
model.result('pg2').feature('lngr1').label('Line Graph 1');
model.result('pg2').feature('lngr1').set('descr', 'Electric potential');
model.result('pg2').feature('lngr1').set('xdataexpr', 'r');
model.result('pg2').feature('lngr1').set('xdataunit', 'm');
model.result('pg2').feature('lngr1').set('xdatadescr', 'r-coordinate');
model.result('pg2').feature('lngr1').set('legend', true);
model.result('pg2').feature('lngr1').set('autosolution', false);
model.result('pg2').feature('lngr1').set('autodescr', true);
model.result('pg2').feature('lngr1').set('autoexpr', true);
model.result('pg2').feature('lngr1').set('evaluationsettings', 'parent');
model.result('pg2').feature('lngr1').set('resolution', 'normal');
model.result('pg2').feature('lngr2').label('Line Graph 2');
model.result('pg2').feature('lngr2').set('xdataexpr', 'r');
model.result('pg2').feature('lngr2').set('xdataunit', 'm');
model.result('pg2').feature('lngr2').set('xdatadescr', 'r-coordinate');
model.result('pg2').feature('lngr2').set('linewidth', 'preference');
model.result('pg2').feature('lngr2').set('legend', true);
model.result('pg2').feature('lngr2').set('legendmethod', 'manual');
model.result('pg2').feature('lngr2').set('legends', {'Analytical solution'});
model.result('pg2').feature('lngr2').set('evaluationsettings', 'parent');
model.result('pg2').feature('lngr2').set('resolution', 'normal');
model.result('pg3').label('Electric Field Comparison, Potential');
model.result('pg3').set('titletype', 'label');
model.result('pg3').set('xlabel', 'r-coordinate (m)');
model.result('pg3').set('ylabel', 'Electric field (V/m)');
model.result('pg3').set('ylabelactive', true);
model.result('pg3').set('xlabelactive', false);
model.result('pg3').feature('lngr1').label('Line Graph 1');
model.result('pg3').feature('lngr1').set('descr', 'Electric field, r-component');
model.result('pg3').feature('lngr1').set('xdataexpr', 'r');
model.result('pg3').feature('lngr1').set('xdataunit', 'm');
model.result('pg3').feature('lngr1').set('xdatadescr', 'r-coordinate');
model.result('pg3').feature('lngr1').set('linewidth', 'preference');
model.result('pg3').feature('lngr1').set('legend', true);
model.result('pg3').feature('lngr1').set('autosolution', false);
model.result('pg3').feature('lngr1').set('autodescr', true);
model.result('pg3').feature('lngr1').set('autoexpr', true);
model.result('pg3').feature('lngr1').set('evaluationsettings', 'parent');
model.result('pg3').feature('lngr1').set('resolution', 'normal');
model.result('pg3').feature('lngr2').label('Line Graph 2');
model.result('pg3').feature('lngr2').set('xdataexpr', 'r');
model.result('pg3').feature('lngr2').set('xdataunit', 'm');
model.result('pg3').feature('lngr2').set('xdatadescr', 'r-coordinate');
model.result('pg3').feature('lngr2').set('linewidth', 'preference');
model.result('pg3').feature('lngr2').set('legend', true);
model.result('pg3').feature('lngr2').set('legendmethod', 'manual');
model.result('pg3').feature('lngr2').set('legends', {'Analytical solution'});
model.result('pg3').feature('lngr2').set('evaluationsettings', 'parent');
model.result('pg3').feature('lngr2').set('resolution', 'normal');
model.result('pg4').label('Electric Field Comparison, Charge Density');
model.result('pg4').set('titletype', 'label');
model.result('pg4').set('xlabel', 'r-coordinate (m)');
model.result('pg4').set('ylabel', 'Electric field (V/m)');
model.result('pg4').set('ylabelactive', true);
model.result('pg4').set('xlabelactive', false);
model.result('pg4').feature('lngr1').label('Line Graph 1');
model.result('pg4').feature('lngr1').set('descr', 'Electric field, r-component');
model.result('pg4').feature('lngr1').set('xdataexpr', 'r');
model.result('pg4').feature('lngr1').set('xdataunit', 'm');
model.result('pg4').feature('lngr1').set('xdatadescr', 'r-coordinate');
model.result('pg4').feature('lngr1').set('linewidth', 'preference');
model.result('pg4').feature('lngr1').set('legend', true);
model.result('pg4').feature('lngr1').set('autosolution', false);
model.result('pg4').feature('lngr1').set('autodescr', true);
model.result('pg4').feature('lngr1').set('autoexpr', true);
model.result('pg4').feature('lngr1').set('evaluationsettings', 'parent');
model.result('pg4').feature('lngr1').set('resolution', 'normal');
model.result('pg4').feature('lngr2').label('Line Graph 2');
model.result('pg4').feature('lngr2').set('xdataexpr', 'r');
model.result('pg4').feature('lngr2').set('xdataunit', 'm');
model.result('pg4').feature('lngr2').set('xdatadescr', 'r-coordinate');
model.result('pg4').feature('lngr2').set('linewidth', 'preference');
model.result('pg4').feature('lngr2').set('legend', true);
model.result('pg4').feature('lngr2').set('legendmethod', 'manual');
model.result('pg4').feature('lngr2').set('legends', {'Analytical solution'});
model.result('pg4').feature('lngr2').set('evaluationsettings', 'parent');
model.result('pg4').feature('lngr2').set('resolution', 'normal');

out = model;
