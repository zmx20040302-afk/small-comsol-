/*
 * heat_radiation_1d.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Aug 25 2026, 17:07 by COMSOL 6.4.0.293. */
public class heat_radiation_1d {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model
         .modelPath("D:\\\u684c\u9762\\codex\\\u6848\u4f8b\u4e0b\u8f7d\\COMSOL\\\u7a33\u6001\u8f90\u5c04\u4f20\u70ed - \u4e00\u7ef4");

    model.label("heat_radiation_1d.mph");

    model.title("\u7a33\u6001\u8f90\u5c04\u4f20\u70ed - \u4e00\u7ef4");

    model
         .description("\u672c\u4f8b\u662f\u4e00\u7ef4\u7a33\u6001\u70ed\u5206\u6790\u7684\u57fa\u51c6\u95ee\u9898\uff0c\u6a21\u62df\u56fa\u5b9a\u6e29\u5ea6\u4e3a 1000\u00a0K \u7684\u5de6\u7aef\u8f90\u5c04\u81f3 300\u00a0K \u7684\u53f3\u7aef\u7684\u60c5\u51b5\u3002\u5206\u6790\u5f97\u5230\u7684\u6e29\u5ea6\u573a\u4e0e NAFEMS \u57fa\u51c6\u89e3\u8fdb\u884c\u4e86\u6bd4\u8f83\u3002");

    model.param().label("Parameters 1");

    model.component().create("comp1", true);

    model.component("comp1").geom().create("geom1", 1);

    model.component("comp1").label("Component 1");

    model.result().table().create("tbl1", "Table");

    model.component("comp1").mesh().create("mesh1");

    model.component("comp1").geom("geom1").label("Geometry 1");
    model.component("comp1").geom("geom1").create("i1", "Interval");
    model.component("comp1").geom("geom1").feature("i1").label("Interval 1");
    model.component("comp1").geom("geom1").feature("i1").set("coord", new double[]{0, 0.1});
    model.component("comp1").geom("geom1").feature("fin").label("Form Union");
    model.component("comp1").geom("geom1").run();

    model.component("comp1").physics().create("ht", "HeatTransfer", "geom1");
    model.component("comp1").physics("ht").create("temp1", "TemperatureBoundary", 0);
    model.component("comp1").physics("ht").feature("temp1").selection().set(1);
    model.component("comp1").physics("ht").create("sar1", "SurfaceToAmbientRadiation", 0);
    model.component("comp1").physics("ht").feature("sar1").selection().set(2);

    model.result().table("tbl1").label("Table 1");
    model.result().table("tbl1").comments("Point Evaluation 1");

    model.thermodynamics().label("Thermodynamics");

    model.frame("material1").label("Moving Mesh 1");

    model.component("comp1").view("view1").label("View 1");
    model.component("comp1").view("view1").axis().label("Axis");
    model.component("comp1").view("view1").axis().set("xmin", -0.005000002682209015);
    model.component("comp1").view("view1").axis().set("xmax", 0.10500000417232513);

    model.material().label("Materials");

    model.common("cminpt").label("Default Model Inputs");

    model.component("comp1").physics("ht").label("Heat Transfer in Solids");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("ashrae2021StationInfo", "Station: 744860");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2021StationInfoFromReference", "Station: 010010");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2021StationInfoAroundLocation", "Station: 744860");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("ashrae2021LocationInfo", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2021LocationInfoFromReference", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2021LocationInfoAroundLocation", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2021CoordinatesInfo", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2021CoordinatesInfoFromReference", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2021CoordinatesInfoAroundLocation", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("ashrae2017StationInfo", "Station: 744860");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2017StationInfoFromReference", "Station: 010010");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2017StationInfoAroundLocation", "Station: 744860");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("ashrae2017LocationInfo", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2017LocationInfoFromReference", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2017LocationInfoAroundLocation", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2017CoordinatesInfo", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2017CoordinatesInfoFromReference", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("ashrae2017CoordinatesInfoAroundLocation", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("StationInfo", "Station: 744860");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("StationInfoFromReference", "Station: 010010");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("StationInfoAroundLocation", "Station: 744860");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("LocationInfo", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("LocationInfoFromReference", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings").set("LocationInfoAroundLocation", "Location:");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("CoordinatesInfo", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("CoordinatesInfoFromReference", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("AmbientSettings")
         .set("CoordinatesInfoAroundLocation", "Coordinates: 0\u00b0N 0\u00b0W 0m");
    model.component("comp1").physics("ht").prop("RadiationSettings")
         .set("refractiveIndex", "Default transparent media refractive index:");
    model.component("comp1").physics("ht").feature("solid1").set("k_mat", "userdef");
    model.component("comp1").physics("ht").feature("solid1")
         .set("k", new double[][]{{55.563}, {0}, {0}, {0}, {55.563}, {0}, {0}, {0}, {55.563}});
    model.component("comp1").physics("ht").feature("solid1").label("Solid 1");
    model.component("comp1").physics("ht").feature("solid1").feature("opac1")
         .set("refractiveIndexTitle", "Transparent media refractive index:");
    model.component("comp1").physics("ht").feature("solid1").feature("opac1").label("Opacity 1");
    model.component("comp1").physics("ht").feature("solid1").feature("opac1").featureInfo("warning")
         .label("Warning");
    model.component("comp1").physics("ht").feature("solid1").feature("opac1").featureInfo("info")
         .label("Equation View");
    model.component("comp1").physics("ht").feature("solid1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ht").feature("init1").set("Tinit", 1000);
    model.component("comp1").physics("ht").feature("init1").label("Initial Values 1");
    model.component("comp1").physics("ht").feature("init1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ht").feature("ins1").label("Thermal Insulation 1");
    model.component("comp1").physics("ht").feature("ins1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ht").feature("idi1").label("Isothermal Domain Interface 1");
    model.component("comp1").physics("ht").feature("idi1").feature("lopac1")
         .set("refractiveIndexTitle", "Transparent media refractive index:");
    model.component("comp1").physics("ht").feature("idi1").feature("lopac1").label("Layer Opacity 1");
    model.component("comp1").physics("ht").feature("idi1").feature("lopac1").featureInfo("warning").label("Warning");
    model.component("comp1").physics("ht").feature("idi1").feature("lopac1").featureInfo("info")
         .label("Equation View");
    model.component("comp1").physics("ht").feature("idi1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ht").feature("ltneb1").label("Local Thermal Nonequilibrium Boundary 1");
    model.component("comp1").physics("ht").feature("ltneb1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ht").feature("dcont1").label("Continuity 1");
    model.component("comp1").physics("ht").feature("dcont1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ht").feature("temp1").set("T0", 1000);
    model.component("comp1").physics("ht").feature("temp1").label("Temperature 1");
    model.component("comp1").physics("ht").feature("temp1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ht").feature("sar1").set("epsilon_rad_mat", "userdef");
    model.component("comp1").physics("ht").feature("sar1").set("epsilon_rad", 0.98);
    model.component("comp1").physics("ht").feature("sar1").set("Tamb", 300);
    model.component("comp1").physics("ht").feature("sar1").label("Surface-to-Ambient Radiation 1");
    model.component("comp1").physics("ht").feature("sar1").featureInfo("info").label("Equation View");

    model.component("comp1").mesh("mesh1").label("Mesh 1");

    model.study().create("std1");
    model.study("std1").create("stat", "Stationary");

    model.sol().create("sol1");
    model.sol("sol1").attach("std1");

    model.result().numerical().create("pev1", "EvalPoint");
    model.result().numerical("pev1").selection().set(2);
    model.result().create("pg1", "PlotGroup1D");
    model.result("pg1").create("lngr1", "LineGraph");
    model.result("pg1").feature("lngr1").set("xdata", "expr");
    model.result("pg1").feature("lngr1").selection().set(1);

    model.study("std1").label("Study 1");
    model.study("std1").feature("stat").label("Stationary");

    model.batch().label("Batch");

    model.sol("sol1").createAutoSequence("std1");
    model.sol("sol1").label("Solution 1");

    model.study("std1").runNoGen();

    model.result().label("Results");
    model.result().numerical("pev1").label("Point Evaluation 1");
    model.result().numerical("pev1").set("table", "tbl1");
    model.result().numerical("pev1").set("descr", new String[]{"Temperature"});
    model.result().numerical("pev1").setResult();
    model.result("pg1").label("Temperature (ht)");
    model.result("pg1").set("xlabel", "x-coordinate (m)");
    model.result("pg1").set("ylabel", "Temperature (K)");
    model.result("pg1").set("smooth", "internal");
    model.result("pg1").set("xlabelactive", false);
    model.result("pg1").set("ylabelactive", false);
    model.result("pg1").feature("lngr1").label("Line Graph 1");
    model.result("pg1").feature("lngr1").set("descr", "Temperature");
    model.result("pg1").feature("lngr1").set("xdataexpr", "x");
    model.result("pg1").feature("lngr1").set("xdataunit", "m");
    model.result("pg1").feature("lngr1").set("xdatadescr", "x-coordinate");
    model.result("pg1").feature("lngr1").set("resolution", "normal");

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
