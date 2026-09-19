/*
 * eigenmodes_of_room.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Aug 25 2026, 17:53 by COMSOL 6.4.0.293. */
public class eigenmodes_of_room {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model
         .modelPath("D:\\\u684c\u9762\\codex\\\u6848\u4f8b\u4e0b\u8f7d\\COMSOL\\\u623f\u95f4\u7684\u7279\u5f81\u6a21\u6001");

    model.label("eigenmodes_of_room.mph");

    model.title("\u623f\u95f4\u7684\u7279\u5f81\u6a21\u6001");

    model
         .description("\u672c\u4f8b\u6a21\u62df\u5e26\u5bb6\u5177\u623f\u95f4\u5185\u7684\u58f0\u9a7b\u6ce2\uff0c\u5176\u7279\u5f81\u6a21\u6001\u4e0e\u7a7a\u623f\u95f4\u7684\u7cbe\u786e\u89e3\u7565\u6709\u4e0d\u540c\u3002");

    model.param().label("Parameters 1");

    model.component().create("comp1", true);

    model.component("comp1").geom().create("geom1", 3);

    model.component("comp1").label("Component 1");

    model.result().evaluationGroup().create("std1EvgFrq", "EvaluationGroup");
    model.result().evaluationGroup("std1EvgFrq").create("gev1", "EvalGlobal");

    model.component("comp1").mesh().create("mesh1");

    model.component("comp1").geom("geom1").label("Geometry 1");
    model.component("comp1").geom("geom1").geomRep("comsol");
    model.component("comp1").geom("geom1").create("imp1", "Import");
    model.component("comp1").geom("geom1").feature("imp1").label("Import 1");
    model.component("comp1").geom("geom1").feature("imp1").set("type", "native");
    model.component("comp1").geom("geom1").feature("imp1").set("filename", "eigenmodes_of_room.mphbin");
    model.component("comp1").geom("geom1").feature("fin").label("Form Union");
    model.component("comp1").geom("geom1").run();

    model.component("comp1").material().create("mat1", "Common");

    model.component("comp1").physics().create("acpr", "PressureAcoustics", "geom1");

    model.component("comp1").mesh("mesh1").create("ftet1", "FreeTet");

    model.thermodynamics().label("Thermodynamics");

    model.frame("material1").label("Moving Mesh 1");

    model.component("comp1").view("view1").label("View 1");
    model.component("comp1").view("view1").set("renderwireframe", true);
    model.component("comp1").view("view1").axis().label("Axis");
    model.component("comp1").view("view1").light("lgt1").label("Directional Light 1");
    model.component("comp1").view("view1").light("lgt2").label("Directional Light 2");
    model.component("comp1").view("view1").light("lgt3").label("Directional Light 3");

    model.material().label("Materials");
    model.component("comp1").material("mat1").label("Air");
    model.component("comp1").material("mat1").propertyGroup("def").label("Basic");
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "1.25");
    model.component("comp1").material("mat1").propertyGroup("def").set("soundspeed", "343");

    model.component("comp1").coordSystem("sys1").label("Boundary System 1");

    model.common("cminpt").label("Default Model Inputs");

    model.component("comp1").physics("acpr").label("Pressure Acoustics, Frequency Domain");
    model.component("comp1").physics("acpr").feature("fpam1").label("Pressure Acoustics 1");
    model.component("comp1").physics("acpr").feature("fpam1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("acpr").feature("shb1").label("Sound Hard Boundary (Wall) 1");
    model.component("comp1").physics("acpr").feature("shb1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("acpr").feature("init1").label("Initial Values 1");
    model.component("comp1").physics("acpr").feature("init1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("acpr").feature("dcont1").label("Continuity 1");
    model.component("comp1").physics("acpr").feature("dcont1").featureInfo("info").label("Equation View");

    model.component("comp1").mesh("mesh1").label("Mesh 1");
    model.component("comp1").mesh("mesh1").feature("size").label("Size");
    model.component("comp1").mesh("mesh1").feature("ftet1").label("Free Tetrahedral 1");
    model.component("comp1").mesh("mesh1").run();

    model.study().create("std1");
    model.study("std1").create("eig", "Eigenfrequency");

    model.sol().create("sol1");
    model.sol("sol1").attach("std1");

    model.result().dataset("dset1").selection().geom("geom1", 2);
    model.result().dataset("dset1").selection()
         .set(3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79);
    model.result().create("pg1", "PlotGroup3D");
    model.result().create("pg2", "PlotGroup3D");
    model.result().create("pg3", "PlotGroup3D");
    model.result().create("pg4", "PlotGroup3D");
    model.result("pg1").create("surf1", "Surface");
    model.result("pg1").create("con1", "Contour");
    model.result("pg2").create("surf1", "Surface");
    model.result("pg2").feature("surf1").set("expr", "acpr.Lp_t");
    model.result("pg3").create("iso1", "Isosurface");
    model.result("pg3").create("surf1", "Surface");
    model.result("pg4").create("surf1", "Surface");
    model.result("pg4").feature("surf1").set("expr", "acpr.Lp_t");

    model.study("std1").label("Study 1");
    model.study("std1").feature("eig").label("Eigenfrequency");
    model.study("std1").feature("eig").set("shift", "90");
    model.study("std1").feature("eig").set("ftplistmethod", "manual");
    model.study("std1").feature("eig").set("filtereigdescription", new String[]{"Damped natural frequency"});

    model.batch().label("Batch");

    model.sol("sol1").createAutoSequence("std1");
    model.sol("sol1").label("Solution 1");

    model.study("std1").runNoGen();

    model.result().label("Results");
    model.result().evaluationGroup("std1EvgFrq").label("Eigenfrequencies (Study 1)");
    model.result().evaluationGroup("std1EvgFrq").set("data", "dset1");
    model.result().evaluationGroup("std1EvgFrq").set("looplevelinput", new String[]{"all"});
    model.result().evaluationGroup("std1EvgFrq").feature("gev1").label("Global Evaluation 1");
    model.result().evaluationGroup("std1EvgFrq").feature("gev1")
         .set("expr", new String[]{"2*pi*freq", "imag(freq)/abs(freq)", "abs(freq)/imag(freq)/2"});
    model.result().evaluationGroup("std1EvgFrq").feature("gev1").set("unit", new String[]{"rad/s", "1", "1"});
    model.result().evaluationGroup("std1EvgFrq").feature("gev1")
         .set("descr", new String[]{"Angular frequency", "Damping ratio", "Quality factor"});
    model.result().evaluationGroup("std1EvgFrq").run();
    model.result("pg1").label("Acoustic Pressure (acpr)");
    model.result("pg1").set("showlegendsunit", true);
    model.result("pg1").feature("surf1").label("Surface 1");
    model.result("pg1").feature("surf1").set("descr", "Total acoustic pressure");
    model.result("pg1").feature("surf1").set("colortable", "WaveLight");
    model.result("pg1").feature("surf1").set("resolution", "normal");
    model.result("pg1").feature("con1").label("Contour 1");
    model.result("pg1").feature("con1").set("descr", "Total acoustic pressure");
    model.result("pg1").feature("con1").set("colorlegend", false);
    model.result("pg1").feature("con1").set("resolution", "normal");
    model.result("pg2").label("Sound Pressure Level (acpr)");
    model.result("pg2").set("showlegendsunit", true);
    model.result("pg2").feature("surf1").label("Surface 1");
    model.result("pg2").feature("surf1").set("descr", "Total sound pressure level");
    model.result("pg2").feature("surf1").set("colortable", "Rainbow");
    model.result("pg2").feature("surf1").set("colorscalemode", "linear");
    model.result("pg2").feature("surf1").set("resolution", "normal");
    model.result("pg3").label("Acoustic Pressure, Isosurfaces (acpr)");
    model.result("pg3").set("looplevel", new int[]{8});
    model.result("pg3").set("showlegendsunit", true);
    model.result("pg3").feature("iso1").label("Isosurface 1");
    model.result("pg3").feature("iso1").set("descr", "Total acoustic pressure");
    model.result("pg3").feature("iso1").set("colorlegend", false);
    model.result("pg3").feature("iso1").set("resolution", "normal");
    model.result("pg3").feature("surf1").label("Surface 1");
    model.result("pg3").feature("surf1").set("descr", "Total acoustic pressure");
    model.result("pg3").feature("surf1").set("evaluationsettings", "parent");
    model.result("pg3").feature("surf1").set("resolution", "normal");
    model.result("pg4").label("Sound Pressure Level (acpr) 1");
    model.result("pg4").set("showlegendsunit", true);
    model.result("pg4").feature("surf1").label("Surface 1");
    model.result("pg4").feature("surf1").set("descractive", true);
    model.result("pg4").feature("surf1").set("descr", "Total SPL");
    model.result("pg4").feature("surf1").set("colortable", "Rainbow");
    model.result("pg4").feature("surf1").set("colorscalemode", "linear");
    model.result("pg4").feature("surf1").set("resolution", "normal");

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
