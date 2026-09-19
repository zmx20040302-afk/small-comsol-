/*
 * capacitor_dc.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Aug 25 2026, 16:10 by COMSOL 6.4.0.293. */
public class capacitor_dc {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model.modelPath("D:\\\u684c\u9762\\codex\\\u6848\u4f8b\u4e0b\u8f7d\\\u7535\u6c14\\\u8ba1\u7b97\u7535\u5bb9");

    model.label("capacitor_dc.mph");

    model.title("\u8ba1\u7b97\u7535\u5bb9");

    model
         .description("\u7535\u5bb9\u5668\u7684\u6700\u7b80\u5355\u5f62\u5f0f\u662f\u53cc\u7aef\u7535\u6c14\u8bbe\u5907\uff0c\u5f53\u4e24\u7aef\u88ab\u65bd\u52a0\u7535\u538b\u5dee\u65f6\uff0c\u8fd9\u79cd\u7535\u5bb9\u5668\u53ef\u4ee5\u50a8\u5b58\u7535\u80fd\u3002\u50a8\u5b58\u7684\u7535\u80fd\u4e0e\u5916\u52a0\u7535\u538b\u7684\u5e73\u65b9\u6210\u6b63\u6bd4\uff0c\u5e76\u901a\u8fc7\u5668\u4ef6\u7684\u7535\u5bb9\u8fdb\u884c\u91cf\u5316\u3002\u672c\u4f8b\u4ecb\u7ecd\u4e86\u4e00\u4e2a\u7b80\u5355\u7684\u7535\u5bb9\u5668\u6a21\u578b\uff0c\u6c42\u89e3\u4e86\u9759\u7535\u6761\u4ef6\u4e0b\u7684\u7535\u573a\u548c\u5668\u4ef6\u7535\u5bb9\u3002");

    model.param().label("Parameters 1");

    model.component().create("comp1", true);

    model.component("comp1").geom().create("geom1", 3);

    model.component("comp1").label("Component 1");

    model.result().table().create("tbl1", "Table");

    model.component("comp1").mesh().create("mesh1");

    model.component("comp1").geom("geom1").label("Geometry 1");
    model.component("comp1").geom("geom1").lengthUnit("cm");
    model.component("comp1").geom("geom1").geomRep("comsol");
    model.component("comp1").geom("geom1").create("cyl1", "Cylinder");
    model.component("comp1").geom("geom1").feature("cyl1").label("Cylinder 1");
    model.component("comp1").geom("geom1").feature("cyl1").set("r", 20);
    model.component("comp1").geom("geom1").feature("cyl1").set("h", 20);
    model.component("comp1").geom("geom1").create("cyl2", "Cylinder");
    model.component("comp1").geom("geom1").feature("cyl2").label("Cylinder 2");
    model.component("comp1").geom("geom1").feature("cyl2").set("r", 10);
    model.component("comp1").geom("geom1").feature("cyl2").set("h", 4);
    model.component("comp1").geom("geom1").feature("cyl2").set("pos", new double[]{0, 0, 8});
    model.component("comp1").geom("geom1").feature("cyl2").set("layername", new String[]{"Layer 1"});
    model.component("comp1").geom("geom1").feature("cyl2").setIndex("layer", "5[mm]", 0);
    model.component("comp1").geom("geom1").feature("cyl2").set("layerside", false);
    model.component("comp1").geom("geom1").feature("cyl2").set("layerbottom", true);
    model.component("comp1").geom("geom1").feature("cyl2").set("layertop", true);
    model.component("comp1").geom("geom1").create("cyl3", "Cylinder");
    model.component("comp1").geom("geom1").feature("cyl3").label("Cylinder 3");
    model.component("comp1").geom("geom1").feature("cyl3").set("r", 0.75);
    model.component("comp1").geom("geom1").feature("cyl3").set("h", 8);
    model.component("comp1").geom("geom1").create("cyl4", "Cylinder");
    model.component("comp1").geom("geom1").feature("cyl4").label("Cylinder 4");
    model.component("comp1").geom("geom1").feature("cyl4").set("r", 0.75);
    model.component("comp1").geom("geom1").feature("cyl4").set("h", 8);
    model.component("comp1").geom("geom1").feature("cyl4").set("pos", new double[]{0, 0, 12});
    model.component("comp1").geom("geom1").feature("fin").label("Form Union");
    model.component("comp1").geom("geom1").run();

    model.component("comp1").selection().create("sel1", "Explicit");
    model.component("comp1").selection("sel1").set(2, 4, 5, 6);
    model.component("comp1").selection().create("com1", "Complement");
    model.component("comp1").selection().create("sel2", "Explicit");
    model.component("comp1").selection("sel2").geom("geom1", 3, 2, new String[]{"exterior"});
    model.component("comp1").selection("sel2").set(2, 5);
    model.component("comp1").selection().create("sel3", "Explicit");
    model.component("comp1").selection("sel3").geom("geom1", 3, 2, new String[]{"exterior"});
    model.component("comp1").selection("sel3").set(4, 6);
    model.component("comp1").selection("sel1").label("Metal");
    model.component("comp1").selection("com1").label("Insulators");
    model.component("comp1").selection("com1").set("input", new String[]{"sel1"});
    model.component("comp1").selection("sel2").label("Ground");
    model.component("comp1").selection("sel3").label("Terminal");

    model.component("comp1").view("view1").hideEntities().create("hide1");
    model.component("comp1").view("view1").hideEntities("hide1").geom("geom1", 2);
    model.component("comp1").view("view1").hideEntities("hide1").set(1, 4, 23);
    model.view().create("view2", 2);

    model.component("comp1").material().create("mat1", "Common");
    model.component("comp1").material("mat1").selection().set();
    model.component("comp1").material("mat1").propertyGroup()
         .create("RefractiveIndex", "RefractiveIndex", "Refractive index");
    model.component("comp1").material("mat1").selection().set(3);

    model.component("comp1").physics().create("es", "Electrostatics", "geom1");
    model.component("comp1").physics("es").selection().named("com1");
    model.component("comp1").physics("es").create("ccns1", "ChargeConservationSolid", 3);
    model.component("comp1").physics("es").feature("ccns1").selection().set(3);
    model.component("comp1").physics("es").create("gnd1", "Ground", 2);
    model.component("comp1").physics("es").feature("gnd1").selection().named("sel2");
    model.component("comp1").physics("es").create("term1", "Terminal", 2);
    model.component("comp1").physics("es").feature("term1").selection().named("sel3");

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
    model.component("comp1").view("view1").hideEntities("hide1").label("Hide for Physics 1");
    model.view("view2").label("View 2D 2");
    model.view("view2").axis().label("Axis");
    model.view("view2").axis().set("xmin", -22.000001907348633);
    model.view("view2").axis().set("xmax", 22.000001907348633);
    model.view("view2").axis().set("ymin", -4.612143516540527);
    model.view("view2").axis().set("ymax", 24.612144470214844);

    model.material().label("Materials");
    model.component("comp1").material("mat1").label("Glass (quartz)");
    model.component("comp1").material("mat1").set("family", "custom");
    model.component("comp1").material("mat1").set("diffuse", "custom");
    model.component("comp1").material("mat1").set("ambient", "custom");
    model.component("comp1").material("mat1").set("noise", true);
    model.component("comp1").material("mat1").set("fresnel", 0.99);
    model.component("comp1").material("mat1").set("roughness", 0.02);
    model.component("comp1").material("mat1").set("diffusewrap", 0);
    model.component("comp1").material("mat1").set("reflectance", 0);
    model.component("comp1").material("mat1").propertyGroup("def").label("Basic");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("relpermeability", new String[]{"1", "0", "0", "0", "1", "0", "0", "0", "1"});
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("electricconductivity", new String[]{"1e-14[S/m]", "0", "0", "0", "1e-14[S/m]", "0", "0", "0", "1e-14[S/m]"});
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("relpermittivity", new String[]{"4.2", "0", "0", "0", "4.2", "0", "0", "0", "4.2"});
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "2210[kg/m^3]");
    model.component("comp1").material("mat1").propertyGroup("def")
         .set("thermalconductivity", new String[]{"1.4[W/(m*K)]", "0", "0", "0", "1.4[W/(m*K)]", "0", "0", "0", "1.4[W/(m*K)]"});
    model.component("comp1").material("mat1").propertyGroup("def").set("heatcapacity", "730[J/(kg*K)]");
    model.component("comp1").material("mat1").propertyGroup("RefractiveIndex").label("Refractive index");
    model.component("comp1").material("mat1").propertyGroup("RefractiveIndex").info("category").label("Information");
    model.component("comp1").material("mat1").propertyGroup("RefractiveIndex")
         .set("n", new String[]{"1.5", "0", "0", "0", "1.5", "0", "0", "0", "1.5"});

    model.component("comp1").coordSystem("sys1").label("Boundary System 1");

    model.common("cminpt").label("Default Model Inputs");

    model.component("comp1").physics("es").label("Electrostatics");
    model.component("comp1").physics("es").feature("fsp1").label("Free Space 1");
    model.component("comp1").physics("es").feature("fsp1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("es").feature("zc1").label("Zero Charge 1");
    model.component("comp1").physics("es").feature("zc1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("es").feature("init1").label("Initial Values 1");
    model.component("comp1").physics("es").feature("init1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("es").feature("ccns1").label("Charge Conservation in Solids 1");
    model.component("comp1").physics("es").feature("ccns1").feature("ddis1").label("Dispersion 1");
    model.component("comp1").physics("es").feature("ccns1").feature("ddis1").featureInfo("info")
         .label("Equation View");
    model.component("comp1").physics("es").feature("ccns1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("es").feature("gnd1").label("Ground 1");
    model.component("comp1").physics("es").feature("gnd1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("es").feature("term1").set("TerminalType", "Voltage");
    model.component("comp1").physics("es").feature("term1").label("Boundary Terminal 1");
    model.component("comp1").physics("es").feature("term1").featureInfo("info").label("Equation View");

    model.component("comp1").mesh("mesh1").label("Mesh 1");
    model.component("comp1").mesh("mesh1").contribute("geom/detail", true);

    model.study().create("std1");
    model.study("std1").create("stat", "Stationary");

    model.sol().create("sol1");
    model.sol("sol1").attach("std1");

    model.result().dataset().create("dset2", "Solution");
    model.result().dataset().create("cpl1", "CutPlane");
    model.result().dataset("dset2").selection().named("sel1");
    model.result().numerical().create("gev1", "EvalGlobal");
    model.result().create("pg1", "PlotGroup3D");
    model.result().create("pg2", "PlotGroup2D");
    model.result("pg1").create("surf1", "Surface");
    model.result("pg1").create("slc1", "Slice");
    model.result("pg1").create("arwv1", "ArrowVolume");
    model.result("pg1").feature("surf1").set("data", "dset2");
    model.result("pg1").feature("slc1").set("expr", "es.normE");
    model.result("pg1").feature("arwv1").create("col1", "Color");
    model.result("pg2").create("con1", "Contour");
    model.result("pg2").create("con2", "Contour");

    model.study("std1").label("Study 1");
    model.study("std1").feature("stat").label("Stationary");

    model.batch().label("Batch");

    model.sol("sol1").createAutoSequence("std1");
    model.sol("sol1").label("Solution 1");

    model.study("std1").runNoGen();

    model.result().label("Results");
    model.result().dataset("cpl1").label("Cut Plane 1");
    model.result().numerical("gev1").label("Global Evaluation 1");
    model.result().numerical("gev1").set("table", "tbl1");
    model.result().numerical("gev1").set("expr", new String[]{"es.C11"});
    model.result().numerical("gev1").set("unit", new String[]{"F"});
    model.result().numerical("gev1").set("descr", new String[]{"Maxwell capacitance"});
    model.result().numerical("gev1").setResult();
    model.result("pg1").label("3D Plot Group 1");
    model.result("pg1").feature("surf1").label("Surface 1");
    model.result("pg1").feature("surf1").set("descr", "Electric potential");
    model.result("pg1").feature("surf1").set("coloring", "uniform");
    model.result("pg1").feature("surf1").set("color", "gray");
    model.result("pg1").feature("surf1").set("evaluationsettings", "parent");
    model.result("pg1").feature("surf1").set("resolution", "normal");
    model.result("pg1").feature("slc1").label("Slice 1");
    model.result("pg1").feature("slc1").set("descr", "Electric field norm");
    model.result("pg1").feature("slc1").set("quickxnumber", 1);
    model.result("pg1").feature("slc1").set("colortable", "RainbowLight");
    model.result("pg1").feature("slc1").set("evaluationsettings", "parent");
    model.result("pg1").feature("slc1").set("resolution", "normal");
    model.result("pg1").feature("arwv1").label("Arrow Volume 1");
    model.result("pg1").feature("arwv1").set("descr", "Electric field");
    model.result("pg1").feature("arwv1").set("xnumber", 1);
    model.result("pg1").feature("arwv1").set("ynumber", 24);
    model.result("pg1").feature("arwv1").set("znumber", 11);
    model.result("pg1").feature("arwv1").set("evaluationsettings", "parent");
    model.result("pg1").feature("arwv1").set("arrowlength", "logarithmic");
    model.result("pg1").feature("arwv1").set("scale", 0.11093332036270957);
    model.result("pg1").feature("arwv1").set("scaleactive", false);
    model.result("pg1").feature("arwv1").feature("col1").label("Color Expression 1");
    model.result("pg1").feature("arwv1").feature("col1").set("descr", "Electric potential");
    model.result("pg1").feature("arwv1").feature("col1").set("colorlegend", false);
    model.result("pg2").label("2D Plot Group 2");
    model.result("pg2").feature("con1").label("Contour 1");
    model.result("pg2").feature("con1").set("descr", "Electric potential");
    model.result("pg2").feature("con1").set("levelmethod", "levels");
    model.result("pg2").feature("con1").set("levels", "range(0.1,0.1,0.9)");
    model.result("pg2").feature("con1").set("contourtype", "filled");
    model.result("pg2").feature("con1").set("colortable", "RainbowLight");
    model.result("pg2").feature("con1").set("evaluationsettings", "parent");
    model.result("pg2").feature("con1").set("resolution", "normal");
    model.result("pg2").feature("con2").label("Contour 2");
    model.result("pg2").feature("con2").set("descr", "Electric potential");
    model.result("pg2").feature("con2").set("titletype", "none");
    model.result("pg2").feature("con2").set("levelmethod", "levels");
    model.result("pg2").feature("con2").set("levels", "range(0,0.1,1)");
    model.result("pg2").feature("con2").set("contourlabels", true);
    model.result("pg2").feature("con2").set("coloring", "uniform");
    model.result("pg2").feature("con2").set("colorlegend", false);
    model.result("pg2").feature("con2").set("color", "black");
    model.result("pg2").feature("con2").set("evaluationsettings", "parent");
    model.result("pg2").feature("con2").set("resolution", "normal");

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
