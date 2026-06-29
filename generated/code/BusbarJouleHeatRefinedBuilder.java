import com.comsol.model.*;
import com.comsol.model.util.*;

public class BusbarJouleHeatRefinedBuilder {
  public static Model run() {
    Model model = ModelUtil.create("Model");
    model.label("busbar_joule_heat_refined_builder.mph");
    model.modelNode().create("mod1");
    // Requirement: 根据母线板焦耳热案例生成电流和传热耦合模型，并指导如何修正现有脚本
    // 正式运行前请复核几何尺寸、选择集和物理场特征名称。

    // Parameters merged from matched case memory and defaults.
    model.param().set("rho_ref", "2500[kg/m^3]", "默认密度；请替换为材料数据");
    model.param().set("E_ref", "35.1[GPa]", "默认杨氏模量；请替换为案例或文章数据");
    model.param().set("k_ref", "1[W/(m*K)]", "使用传热时的默认导热系数");
    model.param().set("hmax", "0.02[m]", "Maximum mesh size");
    model.param().set("L_ref", "1[m]", "Reference length");
    model.param().set("W_ref", "1[m]", "Reference width");
    model.param().set("H_ref", "0.1[m]", "Reference height");
    model.param().set("L", "9[cm]", "母线板焦耳热");
    model.param().set("rad_1", "6[mm]", "母线板焦耳热");
    model.param().set("tbb", "5[mm]", "母线板焦耳热");
    model.param().set("wbb", "5[cm]", "母线板焦耳热");
    model.param().set("mh", "3[mm]", "母线板焦耳热");
    model.param().set("htc", "5[W/m^2/K]", "母线板焦耳热");
    model.param().set("Vtot", "20[mV]", "母线板焦耳热");
    model.param().set("Jan", "8000[A/m^2]", "Anode current density");
    model.param().set("htca", "5[W/m^2/K]", "Heat transfer coefficient to air");
    model.param().set("Ta", "35[degC]", "Air temperature");
    model.param().set("htce", "3000[W/m^2/K]", "Heat transfer coefficient to electrolyte");
    model.param().set("Te", "100[degC]", "Electrolyte temperature");
    model.param().set("c_g_w", "400[mm]", "Cell grid top width");
    model.param().set("c_g_l", "800[mm]", "Cell grid top length");
    model.param().set("c_g_h", "5[mm]", "Cell grid top height");
    model.param().set("s_l", "c_g_l/2-2*s_di", "Spine length");
    model.param().set("s_w", "c_g_w/2-2*s_di", "Spine width");
    model.param().set("s_h", "5[mm]", "Spine height");
    model.param().set("s_di", "10[mm]", "Spine to cell grid boundary distance");
    model.param().set("s_c_w", "65[mm]", "Spine center width");
    model.param().set("s_c_l", "60[mm]", "Spine cut out length");
    model.param().set("c_c_r", "40[mm]", "Central column radius");
    model.param().set("c_c_h", "70[mm]", "Central column height");
    model.param().set("c_c_d", "25[mm]", "Central column center hole depth");
    model.param().set("r_c_h", "6[mm]", "Rod connector height");

    model.component().create("comp1", true);
    model.component("comp1").geom().create("geom1", 2);
    model.component("comp1").geom("geom1").lengthUnit("m");
    // TODO: 明确尺寸后，用已学习案例的几何序列替换这个起始几何。
    model.component("comp1").geom("geom1").create("r1", "Rectangle");
    model.component("comp1").geom("geom1").feature("r1").set("size", new String[]{"L_ref", "W_ref"});
    model.component("comp1").geom("geom1").run();

    model.component("comp1").material().create("mat1", "Common");
    model.component("comp1").material("mat1").label("复核已学习案例中的材料");
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "rho_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("youngsmodulus", "E_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("thermalconductivity", "k_ref");

    // Physics inferred from requirement, matched cases, and COMSOL knowledge memory.
    model.component("comp1").physics().create("ht", "HeatTransferInSolids", "geom1");
    // Add heat flux, temperature, or convection features after selections are verified.
    model.component("comp1").physics().create("solid", "SolidMechanics", "geom1");
    // Add fixed constraints, loads, pore/fracture pressure, and stress boundary conditions.
    model.component("comp1").physics().create("ec", "ElectricCurrents", "geom1");
    // Add terminal, ground, and insulation boundary conditions.
    // 边界选择目前是占位内容。请在 COMSOL 中检查生成几何的边界编号。

    model.component("comp1").mesh().create("mesh1");
    model.component("comp1").mesh("mesh1").create("size1", "Size");
    model.component("comp1").mesh("mesh1").feature("size1").set("custom", true);
    model.component("comp1").mesh("mesh1").feature("size1").set("hmax", "hmax");
    model.component("comp1").mesh("mesh1").run();

    model.study().create("std1");
    model.study("std1").create("stat", "Stationary");
    model.study("std1").createAutoSequences("all");
    // model.study("std1").run(); // Enable after boundary selections and loads are verified.

    // Derived values suggested by memory-assisted plan.
    model.result().numerical().create("gev1", "EvalGlobal");
    model.result().numerical("gev1").label("Tmax");
    model.result().numerical("gev1").set("expr", "T");
    model.result().numerical().create("gev2", "EvalGlobal");
    model.result().numerical("gev2").label("Tavg");
    model.result().numerical("gev2").set("expr", "T");
    model.result().numerical().create("gev3", "EvalGlobal");
    model.result().numerical("gev3").label("heat_flux_integral");
    model.result().numerical("gev3").set("expr", "1");
    model.result().numerical().create("gev4", "EvalGlobal");
    model.result().numerical("gev4").label("max_current_density");
    model.result().numerical("gev4").set("expr", "ec.normJ");
    model.result().numerical().create("gev5", "EvalGlobal");
    model.result().numerical("gev5").label("electric_resistance");
    model.result().numerical("gev5").set("expr", "1");
    model.result().numerical().create("gev6", "EvalGlobal");
    model.result().numerical("gev6").label("terminal_current");
    model.result().numerical("gev6").set("expr", "ec.normJ");

    return model;
  }

  public static void main(String[] args) {
    Model model = run();
    model.save("busbar_joule_heat_refined_builder.mph");
  }
}
