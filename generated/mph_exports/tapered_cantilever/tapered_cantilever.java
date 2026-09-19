/*
 * tapered_cantilever.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Aug 25 2026, 17:17 by COMSOL 6.4.0.293. */
public class tapered_cantilever {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model
         .modelPath("D:\\\u684c\u9762\\codex\\\u6848\u4f8b\u4e0b\u8f7d\\COMSOL\\\u4e24\u79cd\u8f7d\u8377\u5de5\u51b5\u4e0b\u7684\u9525\u5f62\u60ac\u81c2\u6881");

    model.label("tapered_cantilever.mph");

    model.title("\u4e24\u79cd\u8f7d\u8377\u5de5\u51b5\u4e0b\u7684\u9525\u5f62\u60ac\u81c2\u6881");

    model
         .description("\u672c\u4f8b\u6f14\u793a\u4e00\u4e2a\u8584\u9525\u5f62\u60ac\u81c2\u6881\u7684\u4e8c\u7ef4\u5e73\u9762\u5e94\u529b\u6a21\u578b\u3002\u68c0\u67e5\u4e86\u4e0d\u540c\u7684\u8fb9\u754c\u548c\u8f7d\u8377\u60c5\u51b5\uff0c\u6f14\u793a\u5982\u4f55\u65bd\u52a0\u5e76\u8ba1\u7b97\u4e0d\u540c\u7684\u8f7d\u8377\u53ca\u7ea6\u675f\u7ec4\u3002\u4eff\u771f\u5f97\u5230\u7684\u5e94\u529b\u4e0e NAFEMS \u57fa\u51c6\u503c\u8fdb\u884c\u4e86\u6bd4\u8f83\u3002");

    model.param().label("Parameters 1");

    model.component().create("comp1", true);

    model.component("comp1").geom().create("geom1", 2);

    model.component("comp1").label("Component 1");

    model.result().table().create("tbl1", "Table");
    model.result().table().create("tbl2", "Table");

    model.component("comp1").mesh().create("mesh1");

    model.component("comp1").geom("geom1").label("Geometry 1");
    model.component("comp1").geom("geom1").create("pol1", "Polygon");
    model.component("comp1").geom("geom1").feature("pol1").label("Polygon 1");
    model.component("comp1").geom("geom1").feature("pol1").set("x", "0 4 4 0 0");
    model.component("comp1").geom("geom1").feature("pol1").set("y", "0 1 3 4 0");
    model.component("comp1").geom("geom1").create("pt1", "Point");
    model.component("comp1").geom("geom1").feature("pt1").label("Point 1");
    model.component("comp1").geom("geom1").feature("pt1").set("p", new int[]{0, 2});
    model.component("comp1").geom("geom1").feature("fin").label("Form Union");
    model.component("comp1").geom("geom1").run();
    model.component("comp1").geom("geom1").run("fin");

    model.component("comp1").material().create("mat1", "Common");
    model.component("comp1").material("mat1").propertyGroup()
         .create("Enu", "Enu", "Young's modulus and Poisson's ratio");

    model.group().create("lg1", "LoadGroup");
    model.group("lg1").paramName("lgG");
    model.group().create("lg2", "LoadGroup");
    model.group("lg2").paramName("lgF");
    model.group().create("cg1", "ConstraintGroup");
    model.group("cg1").paramName("cgGravity");
    model.group().create("cg2", "ConstraintGroup");
    model.group("cg2").paramName("cgForce");

    model.component("comp1").physics().create("solid", "SolidMechanics", "geom1");
    model.component("comp1").physics("solid").create("fix1", "Fixed", 1);
    model.component("comp1").physics("solid").feature("fix1").selection().set(1, 3);
    model.component("comp1").physics("solid").create("bl1", "BodyLoad", 2);
    model.component("comp1").physics("solid").feature("bl1").selection().set(1);
    model.component("comp1").physics("solid").create("roll1", "Roller", 1);
    model.component("comp1").physics("solid").feature("roll1").selection().set(1, 3);
    model.component("comp1").physics("solid").create("bndl1", "BoundaryLoad", 1);
    model.component("comp1").physics("solid").feature("bndl1").selection().set(5);
    model.component("comp1").physics("solid").create("fix2", "Fixed", 0);
    model.component("comp1").physics("solid").feature("fix2").selection().set(2);

    model.result().table("tbl1").label("Table 1");
    model.result().table("tbl1").comments("Point Evaluation - normal stress");
    model.result().table("tbl2").label("Table 2");
    model.result().table("tbl2").comments("Point Evaluation - shear stress");

    model.thermodynamics().label("Thermodynamics");

    model.frame("material1").label("Moving Mesh 1");

    model.component("comp1").view("view1").label("View 1");
    model.component("comp1").view("view1").axis().label("Axis");
    model.component("comp1").view("view1").axis().set("xmin", -1.474972128868103);
    model.component("comp1").view("view1").axis().set("xmax", 5.470850467681885);
    model.component("comp1").view("view1").axis().set("ymin", -0.2966029644012451);
    model.component("comp1").view("view1").axis().set("ymax", 4.296602249145508);

    model.material().label("Materials");
    model.component("comp1").material("mat1").label("Material 1");
    model.component("comp1").material("mat1").propertyGroup("def").label("Basic");
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "7000[kg/m^3]");
    model.component("comp1").material("mat1").propertyGroup("Enu").label("Young's modulus and Poisson's ratio");
    model.component("comp1").material("mat1").propertyGroup("Enu").info("category").label("Information");
    model.component("comp1").material("mat1").propertyGroup("Enu").set("E", "210[GPa]");
    model.component("comp1").material("mat1").propertyGroup("Enu").set("nu", "0.3");

    model.group("lg1").label("Load Group Gravity");
    model.group("lg2").label("Load Group Force");
    model.group("cg1").label("Constraint Group Gravity");
    model.group("cg2").label("Constraint Group Force");

    model.component("comp1").coordSystem("sys1").label("Boundary System 1");

    model.common("cminpt").label("Default Model Inputs");

    model.component("comp1").physics("solid").label("Solid Mechanics");
    model.component("comp1").physics("solid").prop("Type2D").set("Type2D", "PlaneStress");
    model.component("comp1").physics("solid").prop("d").set("d", 0.1);
    model.component("comp1").physics("solid").prop("TransientSettings")
         .set("text", "Changes made to these settings only take effect when the default solver is generated.");
    model.component("comp1").physics("solid").feature("lemm1").label("Linear Elastic Material 1");
    model.component("comp1").physics("solid").feature("lemm1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("free1").label("Free 1");
    model.component("comp1").physics("solid").feature("free1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("init1").label("Initial Values 1");
    model.component("comp1").physics("solid").feature("init1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("dcont1").label("Continuity 1");
    model.component("comp1").physics("solid").feature("dcont1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("dcnt1").label("Contact 1");
    model.component("comp1").physics("solid").feature("dcnt1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("dgcnt1").label("General Contact 1");
    model.component("comp1").physics("solid").feature("dgcnt1").feature("cmod1").label("Contact Model 1");
    model.component("comp1").physics("solid").feature("dgcnt1").feature("cmod1").featureInfo("info")
         .label("Equation View");
    model.component("comp1").physics("solid").feature("dgcnt1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("fix1").set("constraintGroup", "cg1");
    model.component("comp1").physics("solid").feature("fix1").label("Fixed Constraint 1");
    model.component("comp1").physics("solid").feature("fix1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("bl1")
         .set("forceReferenceVolume", new String[][]{{"0"}, {"-g_const*solid.rho"}, {"0"}});
    model.component("comp1").physics("solid").feature("bl1").set("loadGroup", "lg1");
    model.component("comp1").physics("solid").feature("bl1").label("Body Load 1");
    model.component("comp1").physics("solid").feature("bl1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("roll1").set("constraintGroup", "cg2");
    model.component("comp1").physics("solid").feature("roll1").label("Roller 1");
    model.component("comp1").physics("solid").feature("roll1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("bndl1").set("forceType", "ForceLength");
    model.component("comp1").physics("solid").feature("bndl1")
         .set("forceReferenceLength", new String[][]{{"10[MN/m]"}, {"0"}, {"0"}});
    model.component("comp1").physics("solid").feature("bndl1").set("loadGroup", "lg2");
    model.component("comp1").physics("solid").feature("bndl1").label("Boundary Load 1");
    model.component("comp1").physics("solid").feature("bndl1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("solid").feature("fix2").label("Fixed Constraint 2");
    model.component("comp1").physics("solid").feature("fix2").featureInfo("info").label("Equation View");

    model.component("comp1").mesh("mesh1").label("Mesh 1");

    model.study().create("std1");
    model.study("std1").create("stat", "Stationary");

    model.sol().create("sol1");
    model.sol("sol1").attach("std1");

    model.result().numerical().create("pev1", "EvalPoint");
    model.result().numerical().create("pev2", "EvalPoint");
    model.result().numerical("pev1").selection().set(2);
    model.result().numerical("pev2").selection().set(2);
    model.result().create("pg1", "PlotGroup2D");
    model.result().create("pg2", "PlotGroup2D");
    model.result("pg1").create("surf1", "Surface");
    model.result("pg1").feature("surf1").set("expr", "solid.sGpxx");
    model.result("pg1").feature("surf1").create("def", "Deform");
    model.result("pg2").create("surf1", "Surface");
    model.result("pg2").feature("surf1").set("expr", "solid.sGpxy");
    model.result("pg2").feature("surf1").create("def", "Deform");

    model.study("std1").label("Study 1");
    model.study("std1").feature("stat").label("Stationary");
    model.study("std1").feature("stat").set("useloadcase", true);
    model.study("std1").feature("stat").set("loadcase", new String[]{"Gravity", "Force"});
    model.study("std1").feature("stat").set("loadgroup", new String[][]{{"on", "off"}, {"off", "on"}});
    model.study("std1").feature("stat").set("loadgroupweight", new String[][]{{"1.0", "1.0"}, {"1.0", "1.0"}});
    model.study("std1").feature("stat").set("constraintgroup", new String[][]{{"on", "off"}, {"off", "on"}});

    model.batch().label("Batch");

    model.sol("sol1").createAutoSequence("std1");
    model.sol("sol1").label("Solution 1");

    model.study("std1").runNoGen();

    model.result().label("Results");
    model.result().numerical("pev1").label("Point Evaluation - normal stress");
    model.result().numerical("pev1").set("table", "tbl1");
    model.result().numerical("pev1").set("expr", new String[]{"solid.sGpxx"});
    model.result().numerical("pev1").set("unit", new String[]{"N/m^2"});
    model.result().numerical("pev1").set("descr", new String[]{"Stress tensor, xx-component"});
    model.result().numerical("pev1")
         .set("const", new String[][]{{"solid.refpntx", "0", "Reference point for moment computation, x-coordinate"}, {"solid.refpnty", "0", "Reference point for moment computation, y-coordinate"}, {"solid.refpntz", "0", "Reference point for moment computation, z-coordinate"}});
    model.result().numerical("pev2").label("Point Evaluation - shear stress");
    model.result().numerical("pev2").set("table", "tbl2");
    model.result().numerical("pev2").set("expr", new String[]{"solid.sGpxy"});
    model.result().numerical("pev2").set("unit", new String[]{"N/m^2"});
    model.result().numerical("pev2").set("descr", new String[]{"Stress tensor, xy-component"});
    model.result().numerical("pev2")
         .set("const", new String[][]{{"solid.refpntx", "0", "Reference point for moment computation, x-coordinate"}, {"solid.refpnty", "0", "Reference point for moment computation, y-coordinate"}, {"solid.refpntz", "0", "Reference point for moment computation, z-coordinate"}});
    model.result().numerical("pev1").setResult();
    model.result().numerical("pev2").setResult();
    model.result("pg1").label("Normal stress");
    model.result("pg1").set("frametype", "spatial");
    model.result("pg1").feature("surf1").label("Surface 1");
    model.result("pg1").feature("surf1").set("descr", "Stress tensor, xx-component");
    model.result("pg1").feature("surf1")
         .set("const", new String[][]{{"solid.refpntx", "0", "Reference point for moment computation, x-coordinate"}, {"solid.refpnty", "0", "Reference point for moment computation, y-coordinate"}, {"solid.refpntz", "0", "Reference point for moment computation, z-coordinate"}});
    model.result("pg1").feature("surf1").set("colortable", "Prism");
    model.result("pg1").feature("surf1").set("threshold", "manual");
    model.result("pg1").feature("surf1").set("thresholdvalue", 0.2);
    model.result("pg1").feature("surf1").set("resolution", "normal");
    model.result("pg1").feature("surf1").feature("def").label("Deformation");
    model.result("pg1").feature("surf1").feature("def").set("descr", "Displacement field");
    model.result("pg1").feature("surf1").feature("def").set("scale", 277.3877053127705);
    model.result("pg1").feature("surf1").feature("def").set("scaleactive", false);
    model.result("pg2").label("Shear stress");
    model.result("pg2").set("looplevel", new int[]{1});
    model.result("pg2").set("frametype", "spatial");
    model.result("pg2").feature("surf1").label("Surface 1");
    model.result("pg2").feature("surf1").set("descr", "Stress tensor, xy-component");
    model.result("pg2").feature("surf1")
         .set("const", new String[][]{{"solid.refpntx", "0", "Reference point for moment computation, x-coordinate"}, {"solid.refpnty", "0", "Reference point for moment computation, y-coordinate"}, {"solid.refpntz", "0", "Reference point for moment computation, z-coordinate"}});
    model.result("pg2").feature("surf1").set("colortable", "Prism");
    model.result("pg2").feature("surf1").set("threshold", "manual");
    model.result("pg2").feature("surf1").set("thresholdvalue", 0.2);
    model.result("pg2").feature("surf1").set("resolution", "normal");
    model.result("pg2").feature("surf1").feature("def").label("Deformation");
    model.result("pg2").feature("surf1").feature("def").set("descr", "Displacement field");
    model.result("pg2").feature("surf1").feature("def").set("scale", 31924.596747330696);
    model.result("pg2").feature("surf1").feature("def").set("scaleactive", false);

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
