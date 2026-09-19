/*
 * simple_resistor.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Aug 25 2026, 16:23 by COMSOL 6.4.0.293. */
public class simple_resistor {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model
         .modelPath("D:\\\u684c\u9762\\codex\\\u6848\u4f8b\u4e0b\u8f7d\\\u7535\u6c14\\\u8ba1\u7b97\u5bfc\u7ebf\u7535\u963b");

    model.label("simple_resistor.mph");

    model.title("\u8ba1\u7b97\u5bfc\u7ebf\u7535\u963b");

    model
         .description("\u6bcf\u79cd\u7535\u6c14\u8bbe\u5907\u90fd\u6709\u7535\u963b\uff0c\u4e5f\u5c31\u662f\u8bf4\uff0c\u5f53\u8bbe\u5907\u4e24\u7aef\u65bd\u52a0\u7535\u52bf\u5dee\u65f6\uff0c\u4f1a\u4ea7\u751f\u6b63\u6bd4\u7684\u7535\u6d41\u3002\u672c\u4f8b\u6f14\u793a\u5982\u4f55\u8ba1\u7b97\u94dc\u5bfc\u7ebf\u622a\u9762\u4e0a\u7684\u7535\u963b\u3002\u540c\u65f6\u7814\u7a76\u4e86\u7f51\u683c\u5927\u5c0f\u4e0e\u89e3\u7684\u6536\u655b\u6027\u4e4b\u95f4\u7684\u5173\u7cfb\u3002");

    model.param().label("Parameters 1");

    model.component().create("comp1", true);

    model.component("comp1").geom().create("geom1", 3);

    model.component("comp1").label("Component 1");

    model.result().table().create("tbl1", "Table");

    model.component("comp1").mesh().create("mesh1");

    model.component("comp1").geom("geom1").label("Geometry 1");
    model.component("comp1").geom("geom1").geomRep("comsol");
    model.component("comp1").geom("geom1").create("cyl1", "Cylinder");
    model.component("comp1").geom("geom1").feature("cyl1").label("Cylinder 1");
    model.component("comp1").geom("geom1").feature("cyl1").set("r", "0.5[mm]");
    model.component("comp1").geom("geom1").feature("cyl1").set("h", "10[mm]");
    model.component("comp1").geom("geom1").feature("fin").label("Form Union");
    model.component("comp1").geom("geom1").run();

    model.component("comp1").material().create("mat1", "Common");
    model.component("comp1").material("mat1").propertyGroup()
         .create("Enu", "Enu", "Young's modulus and Poisson's ratio");
    model.component("comp1").material("mat1").propertyGroup().create("linzRes", "linzRes", "Linearized resistivity");

    model.component("comp1").physics().create("ec", "ConductiveMedia", "geom1");
    model.component("comp1").physics("ec").create("gnd1", "Ground", 2);
    model.component("comp1").physics("ec").feature("gnd1").selection().set(3);
    model.component("comp1").physics("ec").create("term1", "Terminal", 2);
    model.component("comp1").physics("ec").feature("term1").selection().set(4);

    model.component("comp1").mesh("mesh1").autoMeshSize(2);

    model.result().table("tbl1").label("Table 1");
    model.result().table("tbl1").comments("Global Evaluation 1");

    model.thermodynamics().label("Thermodynamics");

    model.frame("material1").label("Moving Mesh 1");

    model.component("comp1").view("view1").label("View 1");
    model.component("comp1").view("view1").set("renderwireframe", true);
    model.component("comp1").view("view1").axis().label("Axis");
    model.component("comp1").view("view1").light("lgt1").label("Directional Light 1");
    model.component("comp1").view("view1").light("lgt2").label("Directional Light 2");
    model.component("comp1").view("view1").light("lgt3").label("Directional Light 3");

    model.material().label("Materials");
    model.component("comp1").material("mat1").label("Copper");
    model.component("comp1").material("mat1").set("family", "copper");
    model.component("comp1").material("mat1").propertyGroup("def").label("Basic");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("relpermeability", new String[]{"1", "0", "0", "0", "1", "0", "0", "0", "1"});
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("electricconductivity", new String[]{"5.998e7[S/m]", "0", "0", "0", "5.998e7[S/m]", "0", "0", "0", "5.998e7[S/m]"});
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("thermalexpansioncoefficient", new String[]{"17e-6[1/K]", "0", "0", "0", "17e-6[1/K]", "0", "0", "0", "17e-6[1/K]"});
    model.component("comp1").material("mat1").propertyGroup("def").set("heatcapacity", "385[J/(kg*K)]");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("relpermittivity", new String[]{"1", "0", "0", "0", "1", "0", "0", "0", "1"});
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "8960[kg/m^3]");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("thermalconductivity", new String[]{"400[W/(m*K)]", "0", "0", "0", "400[W/(m*K)]", "0", "0", "0", "400[W/(m*K)]"});
    model.component("comp1").material("mat1").propertyGroup("Enu").label("Young's modulus and Poisson's ratio");
    model.component("comp1").material("mat1").propertyGroup("Enu").info("category").label("Information");
    model.component("comp1").material("mat1").propertyGroup("Enu").set("E", "110[GPa]");
    model.component("comp1").material("mat1").propertyGroup("Enu").set("nu", "0.35");
    model.component("comp1").material("mat1").propertyGroup("linzRes").label("Linearized resistivity");
    model.component("comp1").material("mat1").propertyGroup("linzRes").info("category").label("Information");
    model.component("comp1").material("mat1").propertyGroup("linzRes").set("rho0", "1.72e-8[ohm*m]");
    model.component("comp1").material("mat1").propertyGroup("linzRes").set("alpha", "0.0039[1/K]");
    model.component("comp1").material("mat1").propertyGroup("linzRes").set("Tref", "298[K]");
    model.component("comp1").material("mat1").propertyGroup("linzRes").addInput("temperature");

    model.component("comp1").coordSystem("sys1").label("Boundary System 1");

    model.common("cminpt").label("Default Model Inputs");

    model.component("comp1").physics("ec").label("Electric Currents");
    model.component("comp1").physics("ec").feature("cucns1").label("Current Conservation in Solids 1");
    model.component("comp1").physics("ec").feature("cucns1").feature("ddis1").set("tm", new int[][]{});
    model.component("comp1").physics("ec").feature("cucns1").feature("ddis1").label("Dispersion 1");
    model.component("comp1").physics("ec").feature("cucns1").feature("ddis1").featureInfo("info")
         .label("Equation View");
    model.component("comp1").physics("ec").feature("cucns1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ec").feature("ein1").label("Electric Insulation 1");
    model.component("comp1").physics("ec").feature("ein1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ec").feature("init1").label("Initial Values 1");
    model.component("comp1").physics("ec").feature("init1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ec").feature("dcont1").label("Electric Continuity 1");
    model.component("comp1").physics("ec").feature("dcont1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ec").feature("gnd1").label("Ground 1");
    model.component("comp1").physics("ec").feature("gnd1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("ec").feature("term1").set("I0", 1);
    model.component("comp1").physics("ec").feature("term1").label("Boundary Terminal 1");
    model.component("comp1").physics("ec").feature("term1").featureInfo("info").label("Equation View");

    model.component("comp1").mesh("mesh1").label("Mesh 1");
    model.component("comp1").mesh("mesh1").contribute("geom/detail", true);

    model.study().create("std1");
    model.study("std1").create("stat", "Stationary");

    model.sol().create("sol1");
    model.sol("sol1").attach("std1");

    model.result().numerical().create("gev1", "EvalGlobal");
    model.result().create("pg1", "PlotGroup3D");
    model.result("pg1").create("vol1", "Volume");

    model.study("std1").label("Study 1");
    model.study("std1").feature("stat").label("Stationary");

    model.batch().label("Batch");

    model.sol("sol1").createAutoSequence("std1");
    model.sol("sol1").label("Solution 1");

    model.study("std1").runNoGen();

    model.result().label("Results");
    model.result().numerical("gev1").label("Global Evaluation 1");
    model.result().numerical("gev1").set("table", "tbl1");
    model.result().numerical("gev1").set("expr", new String[]{"ec.R11"});
    model.result().numerical("gev1").set("unit", new String[]{"m\u03a9"});
    model.result().numerical("gev1").set("descr", new String[]{"Resistance"});
    model.result().numerical("gev1").setResult();
    model.result("pg1").label("Electric Potential (ec)");
    model.result("pg1").set("frametype", "spatial");
    model.result("pg1").set("showlegendsmaxmin", true);
    model.result("pg1").feature("vol1").label("Volume 1");
    model.result("pg1").feature("vol1").set("descr", "Electric potential");
    model.result("pg1").feature("vol1").set("colortable", "Dipole");
    model.result("pg1").feature("vol1").set("evaluationsettings", "parent");
    model.result("pg1").feature("vol1").set("resolution", "normal");

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
