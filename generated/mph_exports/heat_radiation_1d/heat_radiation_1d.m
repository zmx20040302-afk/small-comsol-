function out = model
%
% heat_radiation_1d.m
%
% Model exported on Aug 25 2026, 17:07 by COMSOL 6.4.0.293.

import com.comsol.model.*
import com.comsol.model.util.*

model = ModelUtil.create('Model');

model.modelPath(['D:\' native2unicode(hex2dec({'68' '4c'}), 'unicode')  native2unicode(hex2dec({'97' '62'}), 'unicode') '\codex\' native2unicode(hex2dec({'68' '48'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'4e' '0b'}), 'unicode')  native2unicode(hex2dec({'8f' '7d'}), 'unicode') '\COMSOL\' native2unicode(hex2dec({'7a' '33'}), 'unicode')  native2unicode(hex2dec({'60' '01'}), 'unicode')  native2unicode(hex2dec({'8f' '90'}), 'unicode')  native2unicode(hex2dec({'5c' '04'}), 'unicode')  native2unicode(hex2dec({'4f' '20'}), 'unicode')  native2unicode(hex2dec({'70' 'ed'}), 'unicode') ' - ' native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'7e' 'f4'}), 'unicode') ]);

model.label('heat_radiation_1d.mph');

model.title([native2unicode(hex2dec({'7a' '33'}), 'unicode')  native2unicode(hex2dec({'60' '01'}), 'unicode')  native2unicode(hex2dec({'8f' '90'}), 'unicode')  native2unicode(hex2dec({'5c' '04'}), 'unicode')  native2unicode(hex2dec({'4f' '20'}), 'unicode')  native2unicode(hex2dec({'70' 'ed'}), 'unicode') ' - ' native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'7e' 'f4'}), 'unicode') ]);

model.description([native2unicode(hex2dec({'67' '2c'}), 'unicode')  native2unicode(hex2dec({'4f' '8b'}), 'unicode')  native2unicode(hex2dec({'66' '2f'}), 'unicode')  native2unicode(hex2dec({'4e' '00'}), 'unicode')  native2unicode(hex2dec({'7e' 'f4'}), 'unicode')  native2unicode(hex2dec({'7a' '33'}), 'unicode')  native2unicode(hex2dec({'60' '01'}), 'unicode')  native2unicode(hex2dec({'70' 'ed'}), 'unicode')  native2unicode(hex2dec({'52' '06'}), 'unicode')  native2unicode(hex2dec({'67' '90'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'57' 'fa'}), 'unicode')  native2unicode(hex2dec({'51' 'c6'}), 'unicode')  native2unicode(hex2dec({'95' 'ee'}), 'unicode')  native2unicode(hex2dec({'98' '98'}), 'unicode')  native2unicode(hex2dec({'ff' '0c'}), 'unicode')  native2unicode(hex2dec({'6a' '21'}), 'unicode')  native2unicode(hex2dec({'62' 'df'}), 'unicode')  native2unicode(hex2dec({'56' 'fa'}), 'unicode')  native2unicode(hex2dec({'5b' '9a'}), 'unicode')  native2unicode(hex2dec({'6e' '29'}), 'unicode')  native2unicode(hex2dec({'5e' 'a6'}), 'unicode')  native2unicode(hex2dec({'4e' '3a'}), 'unicode') ' 1000' native2unicode(hex2dec({'00' 'a0'}), 'unicode') 'K ' native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'5d' 'e6'}), 'unicode')  native2unicode(hex2dec({'7a' 'ef'}), 'unicode')  native2unicode(hex2dec({'8f' '90'}), 'unicode')  native2unicode(hex2dec({'5c' '04'}), 'unicode')  native2unicode(hex2dec({'81' 'f3'}), 'unicode') ' 300' native2unicode(hex2dec({'00' 'a0'}), 'unicode') 'K ' native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'53' 'f3'}), 'unicode')  native2unicode(hex2dec({'7a' 'ef'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'60' 'c5'}), 'unicode')  native2unicode(hex2dec({'51' 'b5'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode')  native2unicode(hex2dec({'52' '06'}), 'unicode')  native2unicode(hex2dec({'67' '90'}), 'unicode')  native2unicode(hex2dec({'5f' '97'}), 'unicode')  native2unicode(hex2dec({'52' '30'}), 'unicode')  native2unicode(hex2dec({'76' '84'}), 'unicode')  native2unicode(hex2dec({'6e' '29'}), 'unicode')  native2unicode(hex2dec({'5e' 'a6'}), 'unicode')  native2unicode(hex2dec({'57' '3a'}), 'unicode')  native2unicode(hex2dec({'4e' '0e'}), 'unicode') ' NAFEMS ' native2unicode(hex2dec({'57' 'fa'}), 'unicode')  native2unicode(hex2dec({'51' 'c6'}), 'unicode')  native2unicode(hex2dec({'89' 'e3'}), 'unicode')  native2unicode(hex2dec({'8f' 'db'}), 'unicode')  native2unicode(hex2dec({'88' '4c'}), 'unicode')  native2unicode(hex2dec({'4e' '86'}), 'unicode')  native2unicode(hex2dec({'6b' 'd4'}), 'unicode')  native2unicode(hex2dec({'8f' '83'}), 'unicode')  native2unicode(hex2dec({'30' '02'}), 'unicode') ]);

model.param.label('Parameters 1');

model.component.create('comp1', true);

model.component('comp1').geom.create('geom1', 1);

model.component('comp1').label('Component 1');

model.result.table.create('tbl1', 'Table');

model.component('comp1').mesh.create('mesh1');

model.component('comp1').geom('geom1').label('Geometry 1');
model.component('comp1').geom('geom1').create('i1', 'Interval');
model.component('comp1').geom('geom1').feature('i1').label('Interval 1');
model.component('comp1').geom('geom1').feature('i1').set('coord', [0 0.1]);
model.component('comp1').geom('geom1').feature('fin').label('Form Union');
model.component('comp1').geom('geom1').run;

model.component('comp1').physics.create('ht', 'HeatTransfer', 'geom1');
model.component('comp1').physics('ht').create('temp1', 'TemperatureBoundary', 0);
model.component('comp1').physics('ht').feature('temp1').selection.set([1]);
model.component('comp1').physics('ht').create('sar1', 'SurfaceToAmbientRadiation', 0);
model.component('comp1').physics('ht').feature('sar1').selection.set([2]);

model.result.table('tbl1').label('Table 1');
model.result.table('tbl1').comments('Point Evaluation 1');

model.thermodynamics.label('Thermodynamics');

model.frame('material1').label('Moving Mesh 1');

model.component('comp1').view('view1').label('View 1');
model.component('comp1').view('view1').axis.label('Axis');
model.component('comp1').view('view1').axis.set('xmin', -0.005000002682209015);
model.component('comp1').view('view1').axis.set('xmax', 0.10500000417232513);

model.material.label('Materials');

model.common('cminpt').label('Default Model Inputs');

model.component('comp1').physics('ht').label('Heat Transfer in Solids');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021StationInfo', 'Station: 744860');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021StationInfoFromReference', 'Station: 010010');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021StationInfoAroundLocation', 'Station: 744860');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021LocationInfo', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021LocationInfoFromReference', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021LocationInfoAroundLocation', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021CoordinatesInfo', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021CoordinatesInfoFromReference', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2021CoordinatesInfoAroundLocation', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017StationInfo', 'Station: 744860');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017StationInfoFromReference', 'Station: 010010');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017StationInfoAroundLocation', 'Station: 744860');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017LocationInfo', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017LocationInfoFromReference', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017LocationInfoAroundLocation', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017CoordinatesInfo', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017CoordinatesInfoFromReference', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('ashrae2017CoordinatesInfoAroundLocation', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('StationInfo', 'Station: 744860');
model.component('comp1').physics('ht').prop('AmbientSettings').set('StationInfoFromReference', 'Station: 010010');
model.component('comp1').physics('ht').prop('AmbientSettings').set('StationInfoAroundLocation', 'Station: 744860');
model.component('comp1').physics('ht').prop('AmbientSettings').set('LocationInfo', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('LocationInfoFromReference', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('LocationInfoAroundLocation', 'Location:');
model.component('comp1').physics('ht').prop('AmbientSettings').set('CoordinatesInfo', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('CoordinatesInfoFromReference', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('AmbientSettings').set('CoordinatesInfoAroundLocation', ['Coordinates: 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'N 0' native2unicode(hex2dec({'00' 'b0'}), 'unicode') 'W 0m']);
model.component('comp1').physics('ht').prop('RadiationSettings').set('refractiveIndex', 'Default transparent media refractive index:');
model.component('comp1').physics('ht').feature('solid1').set('k_mat', 'userdef');
model.component('comp1').physics('ht').feature('solid1').set('k', [55.563; 0; 0; 0; 55.563; 0; 0; 0; 55.563]);
model.component('comp1').physics('ht').feature('solid1').label('Solid 1');
model.component('comp1').physics('ht').feature('solid1').feature('opac1').set('refractiveIndexTitle', 'Transparent media refractive index:');
model.component('comp1').physics('ht').feature('solid1').feature('opac1').label('Opacity 1');
model.component('comp1').physics('ht').feature('solid1').feature('opac1').featureInfo('warning').label('Warning');
model.component('comp1').physics('ht').feature('solid1').feature('opac1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('solid1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('init1').set('Tinit', 1000);
model.component('comp1').physics('ht').feature('init1').label('Initial Values 1');
model.component('comp1').physics('ht').feature('init1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('ins1').label('Thermal Insulation 1');
model.component('comp1').physics('ht').feature('ins1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('idi1').label('Isothermal Domain Interface 1');
model.component('comp1').physics('ht').feature('idi1').feature('lopac1').set('refractiveIndexTitle', 'Transparent media refractive index:');
model.component('comp1').physics('ht').feature('idi1').feature('lopac1').label('Layer Opacity 1');
model.component('comp1').physics('ht').feature('idi1').feature('lopac1').featureInfo('warning').label('Warning');
model.component('comp1').physics('ht').feature('idi1').feature('lopac1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('idi1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('ltneb1').label('Local Thermal Nonequilibrium Boundary 1');
model.component('comp1').physics('ht').feature('ltneb1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('dcont1').label('Continuity 1');
model.component('comp1').physics('ht').feature('dcont1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('temp1').set('T0', 1000);
model.component('comp1').physics('ht').feature('temp1').label('Temperature 1');
model.component('comp1').physics('ht').feature('temp1').featureInfo('info').label('Equation View');
model.component('comp1').physics('ht').feature('sar1').set('epsilon_rad_mat', 'userdef');
model.component('comp1').physics('ht').feature('sar1').set('epsilon_rad', 0.98);
model.component('comp1').physics('ht').feature('sar1').set('Tamb', 300);
model.component('comp1').physics('ht').feature('sar1').label('Surface-to-Ambient Radiation 1');
model.component('comp1').physics('ht').feature('sar1').featureInfo('info').label('Equation View');

model.component('comp1').mesh('mesh1').label('Mesh 1');

model.study.create('std1');
model.study('std1').create('stat', 'Stationary');

model.sol.create('sol1');
model.sol('sol1').attach('std1');

model.result.numerical.create('pev1', 'EvalPoint');
model.result.numerical('pev1').selection.set([2]);
model.result.create('pg1', 'PlotGroup1D');
model.result('pg1').create('lngr1', 'LineGraph');
model.result('pg1').feature('lngr1').set('xdata', 'expr');
model.result('pg1').feature('lngr1').selection.set([1]);

model.study('std1').label('Study 1');
model.study('std1').feature('stat').label('Stationary');

model.batch.label('Batch');

model.sol('sol1').createAutoSequence('std1');
model.sol('sol1').label('Solution 1');

model.study('std1').runNoGen;

model.result.label('Results');
model.result.numerical('pev1').label('Point Evaluation 1');
model.result.numerical('pev1').set('table', 'tbl1');
model.result.numerical('pev1').set('descr', {'Temperature'});
model.result.numerical('pev1').setResult;
model.result('pg1').label('Temperature (ht)');
model.result('pg1').set('xlabel', 'x-coordinate (m)');
model.result('pg1').set('ylabel', 'Temperature (K)');
model.result('pg1').set('smooth', 'internal');
model.result('pg1').set('xlabelactive', false);
model.result('pg1').set('ylabelactive', false);
model.result('pg1').feature('lngr1').label('Line Graph 1');
model.result('pg1').feature('lngr1').set('descr', 'Temperature');
model.result('pg1').feature('lngr1').set('xdataexpr', 'x');
model.result('pg1').feature('lngr1').set('xdataunit', 'm');
model.result('pg1').feature('lngr1').set('xdatadescr', 'x-coordinate');
model.result('pg1').feature('lngr1').set('resolution', 'normal');

out = model;
