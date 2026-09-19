/*
 * effective_diffusivity.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Aug 25 2026, 18:04 by COMSOL 6.4.0.293. */
public class effective_diffusivity {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model
         .modelPath("D:\\\u684c\u9762\\codex\\\u6848\u4f8b\u4e0b\u8f7d\\COMSOL\\\u591a\u5b54\u6750\u6599\u7684\u6709\u6548\u6269\u6563\u7cfb\u6570");

    model.label("effective_diffusivity.mph");

    model.title("\u591a\u5b54\u6750\u6599\u7684\u6709\u6548\u6269\u6563\u7cfb\u6570");

    model
         .description("\u672c\u4f8b\u7814\u7a76\u4eba\u5de5\u591a\u5b54\u7ed3\u6784\u4e2d\u7684\u4f20\u9012\uff0c\u901a\u8fc7\u6bd4\u8f83\u8be6\u7ec6\u6a21\u578b\u4e0e\u501f\u52a9\u6709\u6548\u4f20\u9012\u5c5e\u6027\u5b9e\u73b0\u7684\u7b80\u5316\u5747\u8d28\u591a\u5b54\u4ecb\u8d28\u65b9\u6cd5\uff0c\u4ecb\u7ecd\u4e86\u591a\u5b54\u4ecb\u8d28\u4e2d\u6709\u6548\u6269\u6563\u7cfb\u6570\u7684\u6982\u5ff5\u3002");

    model.param().set("D2", "1e-5[m^2/s]", "Diffusion coefficient");
    model.param().set("c_max", "3[mol/m^3]", "Peak initial concentration");
    model.param().set("k_f", "5[m/s]", "Mass transfer coefficient");
    model.param().set("a", "1000", "Dimensionless constant");
    model.param().set("epsilon", "0.383", "Porosity");
    model.param().set("D1", "2.15e-6[m^2/s]", "Diffusion coefficient, 1D");
    model.param().label("Parameters 1");

    model.component().create("comp1", true);

    model.component("comp1").geom().create("geom1", 2);

    model.component().create("comp2", true);

    model.component("comp2").geom().create("geom2", 1);

    model.component("comp1").label("Component 1");
    model.component("comp2").label("Component 2");

    model.result().table().create("tbl1", "Table");

    model.component("comp1").mesh().create("mesh1");
    model.component("comp2").mesh().create("mesh2");

    model.component("comp1").geom("geom1").label("Geometry 1");
    model.component("comp1").geom("geom1").create("sq1", "Square");
    model.component("comp1").geom("geom1").feature("sq1").label("Square 1");
    model.component("comp1").geom("geom1").feature("sq1").set("size", "0.08[mm]");
    model.component("comp1").geom("geom1").feature("sq1").set("pos", new String[]{"0.01[mm]", "0.01[mm]"});
    model.component("comp1").geom("geom1").feature("sq1").set("selresult", true);
    model.component("comp1").geom("geom1").feature("sq1").set("selresultshow", false);
    model.component("comp1").geom("geom1").create("fil1", "Fillet");
    model.component("comp1").geom("geom1").feature("fil1").label("Fillet 1");
    model.component("comp1").geom("geom1").feature("fil1").set("radius", "0.016[mm]");
    model.component("comp1").geom("geom1").feature("fil1").selection("point").named("sq1");
    model.component("comp1").geom("geom1").create("arr1", "Array");
    model.component("comp1").geom("geom1").feature("arr1").label("Array 1");
    model.component("comp1").geom("geom1").feature("arr1").set("fullsize", new double[]{8, 9});
    model.component("comp1").geom("geom1").feature("arr1").set("displ", new String[]{"0.1[mm]", "0.1[mm]"});
    model.component("comp1").geom("geom1").feature("arr1").selection("input").set("fil1");
    model.component("comp1").geom("geom1").create("mov1", "Move");
    model.component("comp1").geom("geom1").feature("mov1").label("Move 1");
    model.component("comp1").geom("geom1").feature("mov1").set("disply", "-0.05[mm]");
    model.component("comp1").geom("geom1").feature("mov1").selection("input")
         .set("arr1(2,1)", "arr1(2,2)", "arr1(2,3)", "arr1(2,4)", "arr1(2,5)", "arr1(2,6)", "arr1(2,7)", "arr1(2,8)", "arr1(2,9)", "arr1(4,1)", "arr1(4,2)", "arr1(4,3)", "arr1(4,4)", "arr1(4,5)", "arr1(4,6)", "arr1(4,7)", "arr1(4,8)", "arr1(4,9)", "arr1(6,1)", "arr1(6,2)", "arr1(6,3)", "arr1(6,4)", "arr1(6,5)", "arr1(6,6)", "arr1(6,7)", "arr1(6,8)", "arr1(6,9)", "arr1(8,1)", "arr1(8,2)", "arr1(8,3)", "arr1(8,4)", "arr1(8,5)", "arr1(8,6)", "arr1(8,7)", "arr1(8,8)", "arr1(8,9)");
    model.component("comp1").geom("geom1").create("r1", "Rectangle");
    model.component("comp1").geom("geom1").feature("r1").label("Rectangle 1");
    model.component("comp1").geom("geom1").feature("r1").set("size", new String[]{"0.8[mm]", "0.8[mm]"});
    model.component("comp1").geom("geom1").create("dif1", "Difference");
    model.component("comp1").geom("geom1").feature("dif1").label("Difference 1");
    model.component("comp1").geom("geom1").feature("dif1").selection("input").set("r1");
    model.component("comp1").geom("geom1").feature("dif1").selection("input2").named("sq1");
    model.component("comp1").geom("geom1").feature("fin").label("Form Union");
    model.component("comp1").geom("geom1").run("fin");
    model.component("comp1").geom("geom1").create("sel1", "ExplicitSelection");
    model.component("comp1").geom("geom1").feature("sel1").label("Top-Right Vertex");
    model.component("comp1").geom("geom1").feature("sel1").selection("selection").init(0);
    model.component("comp1").geom("geom1").feature("sel1").selection("selection").set("fin(1)", 532);
    model.component("comp1").geom("geom1").create("sel2", "ExplicitSelection");
    model.component("comp1").geom("geom1").feature("sel2").label("Left Boundary");
    model.component("comp1").geom("geom1").feature("sel2").selection("selection").init(1);
    model.component("comp1").geom("geom1").feature("sel2").selection("selection").set("fin(1)", 1);
    model.component("comp1").geom("geom1").create("sel3", "ExplicitSelection");
    model.component("comp1").geom("geom1").feature("sel3").label("Right Boundary");
    model.component("comp1").geom("geom1").feature("sel3").selection("selection").init(1);
    model.component("comp1").geom("geom1").feature("sel3").selection("selection").set("fin(1)", 276);
    model.component("comp1").geom("geom1").run();
    model.component("comp2").geom("geom2").label("Geometry 2");
    model.component("comp2").geom("geom2").create("i1", "Interval");
    model.component("comp2").geom("geom2").feature("i1").label("Interval 1");
    model.component("comp2").geom("geom2").feature("i1").set("coord", new String[]{"0", "8e-4"});
    model.component("comp2").geom("geom2").feature("fin").label("Form Union");
    model.component("comp2").geom("geom2").run();

    model.variable().create("var1");
    model.variable("var1").set("c0", "c_max*exp(a*(-(x/0.4[mm])^2))", "Initial concentration");
    model.component("comp1").variable().create("var2");
    model.component("comp1").variable("var2").set("flux_avg", "aveop1(k_f*c)", "Average flux");
    model.component("comp2").variable().create("var3");
    model.component("comp2").variable("var3").set("flux_hom", "k_f*c2", "Flux, 1D model");

    model.component("comp1").cpl().create("aveop1", "Average");
    model.component("comp1").cpl("aveop1").selection().named("geom1_sel3");

    model.component("comp1").physics().create("tds", "DilutedSpecies", "geom1");
    model.component("comp1").physics("tds").create("conc1", "Concentration", 1);
    model.component("comp1").physics("tds").feature("conc1").selection().named("geom1_sel2");
    model.component("comp1").physics("tds").create("fl1", "FluxBoundary", 1);
    model.component("comp1").physics("tds").feature("fl1").selection().named("geom1_sel3");
    model.component("comp2").physics().create("tds2", "DilutedSpecies", "geom2");
    model.component("comp2").physics("tds2").create("conc1", "Concentration", 0);
    model.component("comp2").physics("tds2").feature("conc1").selection().set(1);
    model.component("comp2").physics("tds2").create("fl1", "FluxBoundary", 0);
    model.component("comp2").physics("tds2").feature("fl1").selection().set(2);

    model.component("comp2").mesh("mesh2").autoMeshSize(2);

    model.result().table("tbl1").label("Table 1");
    model.result().table("tbl1").comments("Surface Integration 1");

    model.thermodynamics().label("Thermodynamics");

    model.frame("material1").label("Moving Mesh 1");
    model.frame("material2").label("Moving Mesh 2");

    model.variable("var1").label("Variables 1");
    model.component("comp1").variable("var2").label("Variables 2");
    model.component("comp2").variable("var3").label("Variables 3");

    model.component("comp1").view("view1").label("View 1");
    model.component("comp1").view("view1").axis().label("Axis");
    model.component("comp1").view("view1").axis().set("xmin", -2.6041126693598926E-4);
    model.component("comp1").view("view1").axis().set("xmax", 0.001060411217622459);
    model.component("comp1").view("view1").axis().set("ymin", -4.0000013541430235E-5);
    model.component("comp1").view("view1").axis().set("ymax", 8.399999933317304E-4);
    model.component("comp2").view("view2").label("View 2");
    model.component("comp2").view("view2").axis().label("Axis");
    model.component("comp2").view("view2").axis().set("xmin", -4.0000013541430235E-5);
    model.component("comp2").view("view2").axis().set("xmax", 8.399999933317304E-4);

    model.material().label("Materials");

    model.component("comp1").cpl("aveop1").label("Average 1");

    model.component("comp1").coordSystem("sys1").label("Boundary System 1");

    model.common("cminpt").label("Default Model Inputs");

    model.component("comp1").physics("tds").label("Transport of Diluted Species");
    model.component("comp1").physics("tds").prop("TransportMechanism").set("Convection", false);
    model.component("comp1").physics("tds").feature("sp1").label("Species Properties 1");
    model.component("comp1").physics("tds").feature("sp1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("tds").feature("cdm1")
         .set("D_c", new String[][]{{"D2"}, {"0"}, {"0"}, {"0"}, {"D2"}, {"0"}, {"0"}, {"0"}, {"D2"}});
    model.component("comp1").physics("tds").feature("cdm1").label("Fluid 1");
    model.component("comp1").physics("tds").feature("cdm1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("tds").feature("nflx1").label("No Flux 1");
    model.component("comp1").physics("tds").feature("nflx1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("tds").feature("init1").set("initc", "c0");
    model.component("comp1").physics("tds").feature("init1").label("Initial Values 1");
    model.component("comp1").physics("tds").feature("init1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("tds").feature("dcont1").label("Continuity 1");
    model.component("comp1").physics("tds").feature("dcont1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("tds").feature("conc1").set("species", true);
    model.component("comp1").physics("tds").feature("conc1").set("c0", "c_max");
    model.component("comp1").physics("tds").feature("conc1").label("Concentration 1");
    model.component("comp1").physics("tds").feature("conc1").featureInfo("info").label("Equation View");
    model.component("comp1").physics("tds").feature("fl1").set("FluxType", "ExternalConvection");
    model.component("comp1").physics("tds").feature("fl1").set("species", true);
    model.component("comp1").physics("tds").feature("fl1").set("kc", "k_f");
    model.component("comp1").physics("tds").feature("fl1").label("Flux 1");
    model.component("comp1").physics("tds").feature("fl1").featureInfo("info").label("Equation View");
    model.component("comp2").physics("tds2").label("Transport of Diluted Species 2");
    model.component("comp2").physics("tds2").prop("TransportMechanism").set("Convection", false);
    model.component("comp2").physics("tds2").feature("sp1").label("Species Properties 1");
    model.component("comp2").physics("tds2").feature("sp1").featureInfo("info").label("Equation View");
    model.component("comp2").physics("tds2").feature("cdm1")
         .set("D_c2", new String[][]{{"D1/epsilon"}, {"0"}, {"0"}, {"0"}, {"D1/epsilon"}, {"0"}, {"0"}, {"0"}, {"D1/epsilon"}});
    model.component("comp2").physics("tds2").feature("cdm1").label("Fluid 1");
    model.component("comp2").physics("tds2").feature("cdm1").featureInfo("info").label("Equation View");
    model.component("comp2").physics("tds2").feature("nflx1").label("No Flux 1");
    model.component("comp2").physics("tds2").feature("nflx1").featureInfo("info").label("Equation View");
    model.component("comp2").physics("tds2").feature("init1").set("initc", "c0");
    model.component("comp2").physics("tds2").feature("init1").label("Initial Values 1");
    model.component("comp2").physics("tds2").feature("init1").featureInfo("info").label("Equation View");
    model.component("comp2").physics("tds2").feature("dcont1").label("Continuity 1");
    model.component("comp2").physics("tds2").feature("dcont1").featureInfo("info").label("Equation View");
    model.component("comp2").physics("tds2").feature("conc1").set("species", true);
    model.component("comp2").physics("tds2").feature("conc1").set("c0", "c_max");
    model.component("comp2").physics("tds2").feature("conc1").label("Concentration 1");
    model.component("comp2").physics("tds2").feature("conc1").featureInfo("info").label("Equation View");
    model.component("comp2").physics("tds2").feature("fl1").set("FluxType", "ExternalConvection");
    model.component("comp2").physics("tds2").feature("fl1").set("species", true);
    model.component("comp2").physics("tds2").feature("fl1").set("kc", "k_f/epsilon");
    model.component("comp2").physics("tds2").feature("fl1").label("Flux 1");
    model.component("comp2").physics("tds2").feature("fl1").featureInfo("info").label("Equation View");

    model.component("comp1").mesh("mesh1").label("Mesh 1");
    model.component("comp2").mesh("mesh2").label("Mesh 2");

    model.study().create("std1");
    model.study("std1").create("time", "Transient");
    model.study("std1").feature("time")
         .set("activate", new String[]{"tds", "on", "tds2", "off", "frame:spatial1", "on", "frame:spatial2", "on", "frame:material1", "on", 
         "frame:material2", "on", "comp1", "on", "comp2", "on"});
    model.study().create("std2");
    model.study("std2").create("time", "Transient");
    model.study("std2").feature("time")
         .set("activate", new String[]{"tds", "off", "tds2", "on", "frame:spatial1", "on", "frame:spatial2", "on", "frame:material1", "on", 
         "frame:material2", "on", "comp1", "on", "comp2", "on"});

    model.sol().create("sol1");
    model.sol("sol1").attach("std1");
    model.sol().create("sol2");

    model.result().dataset().remove("dset3");
    model.result().dataset("dset2").set("solution", "sol2");

    model.sol("sol2").attach("std2");

    model.result().dataset().create("dset3", "Solution");
    model.result().dataset("dset2").set("comp", "comp1");
    model.result().dataset("dset3").set("solution", "sol2");
    model.result().dataset("dset3").set("comp", "comp2");
    model.result().dataset().remove("dset4");
    model.result().numerical().create("int1", "IntSurface");
    model.result().numerical("int1").selection().all();
    model.result().create("pg1", "PlotGroup2D");
    model.result().create("pg2", "PlotGroup1D");
    model.result().create("pg3", "PlotGroup1D");
    model.result("pg1").create("surf1", "Surface");
    model.result("pg1").create("str1", "Streamline");
    model.result("pg1").feature("str1").selection().set(1);
    model.result("pg2").create("ptgr1", "PointGraph");
    model.result("pg2").create("ptgr2", "PointGraph");
    model.result("pg2").feature("ptgr1").selection().named("geom1_sel1");
    model.result("pg2").feature("ptgr1").set("expr", "flux_avg");
    model.result("pg2").feature("ptgr2").set("data", "dset3");
    model.result("pg2").feature("ptgr2").selection().set(2);
    model.result("pg2").feature("ptgr2").set("expr", "flux_hom");
    model.result("pg3").set("data", "dset3");
    model.result("pg3").create("lngr1", "LineGraph");
    model.result("pg3").feature("lngr1").set("xdata", "expr");
    model.result("pg3").feature("lngr1").selection().set(1);

    model.study("std1").label("Study 1");
    model.study("std1").feature("time").label("Time Dependent");
    model.study("std1").feature("time").set("tunit", "ms");
    model.study("std1").feature("time").set("tlist", "range(0,2,100)");
    model.study("std2").label("Study 2");
    model.study("std2").feature("time").label("Time Dependent");
    model.study("std2").feature("time").set("tunit", "ms");
    model.study("std2").feature("time").set("tlist", "range(0,2,100)");

    model.batch().label("Batch");

    model.sol("sol1").createAutoSequence("std1");
    model.sol("sol1").label("Solution 1");

    model.study("std1").runNoGen();

    model.sol("sol2").createAutoSequence("std2");
    model.sol("sol2").label("Solution 2");

    model.study("std2").runNoGen();

    model.result().label("Results");
    model.result().numerical("int1").label("Surface Integration 1");
    model.result().numerical("int1").set("table", "tbl1");
    model.result().numerical("int1").set("expr", new String[]{"1/(0.8[mm])^2"});
    model.result().numerical("int1").set("unit", new String[]{"1"});
    model.result().numerical("int1").set("descr", new String[]{""});
    model.result().numerical("int1").setResult();
    model.result("pg1").label("Concentration (tds)");
    model.result("pg1").set("looplevel", new int[]{26});
    model.result("pg1").set("titletype", "custom");
    model.result("pg1").set("showlegendsunit", true);
    model.result("pg1").feature("surf1").label("Surface 1");
    model.result("pg1").feature("surf1").set("descr", "Molar concentration, c");
    model.result("pg1").feature("surf1").set("resolution", "normal");
    model.result("pg1").feature("str1").label("Streamline 1");
    model.result("pg1").feature("str1").set("descr", "Total flux");
    model.result("pg1").feature("str1").set("selnumber", 40);
    model.result("pg1").feature("str1").set("pointtype", "arrow");
    model.result("pg1").feature("str1").set("arrowcount", 95);
    model.result("pg1").feature("str1").set("arrowlength", "logarithmic");
    model.result("pg1").feature("str1").set("arrowscale", 0.0014197199193539116);
    model.result("pg1").feature("str1").set("evaluationsettings", "parent");
    model.result("pg1").feature("str1").set("arrowcountactive", false);
    model.result("pg1").feature("str1").set("arrowscaleactive", false);
    model.result("pg1").feature("str1").set("resolution", "normal");
    model.result("pg2").label("Molar fluxes");
    model.result("pg2").set("titletype", "none");
    model.result("pg2").set("xlabel", "Time (ms)");
    model.result("pg2").set("ylabel", "Average flux (mol/(m*s))");
    model.result("pg2").set("ylabelactive", true);
    model.result("pg2").set("legendpos", "upperleft");
    model.result("pg2").set("xlabelactive", false);
    model.result("pg2").feature("ptgr1").label("2D");
    model.result("pg2").feature("ptgr1").set("linewidth", "preference");
    model.result("pg2").feature("ptgr1").set("legend", true);
    model.result("pg2").feature("ptgr1").set("autoplotlabel", true);
    model.result("pg2").feature("ptgr1").set("autopoint", false);
    model.result("pg2").feature("ptgr1").set("autosolution", false);
    model.result("pg2").feature("ptgr2").label("1D");
    model.result("pg2").feature("ptgr2").set("linestyle", "dashed");
    model.result("pg2").feature("ptgr2").set("linewidth", "preference");
    model.result("pg2").feature("ptgr2").set("legend", true);
    model.result("pg2").feature("ptgr2").set("autoplotlabel", true);
    model.result("pg2").feature("ptgr2").set("autopoint", false);
    model.result("pg2").feature("ptgr2").set("autosolution", false);
    model.result("pg3").label("Concentration (tds2)");
    model.result("pg3").set("titletype", "none");
    model.result("pg3").set("xlabel", "x-coordinate (m)");
    model.result("pg3").set("ylabel", "Molar concentration, c2 (mol/m<sup>3</sup>)");
    model.result("pg3").set("xlabelactive", false);
    model.result("pg3").set("ylabelactive", false);
    model.result("pg3").feature("lngr1").label("Line Graph 1");
    model.result("pg3").feature("lngr1").set("descr", "Molar concentration, c2");
    model.result("pg3").feature("lngr1").set("xdataexpr", "x");
    model.result("pg3").feature("lngr1").set("xdataunit", "m");
    model.result("pg3").feature("lngr1").set("xdatadescr", "x-coordinate");
    model.result("pg3").feature("lngr1").set("resolution", "normal");

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
