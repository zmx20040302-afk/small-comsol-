import com.comsol.model.*;
import com.comsol.model.util.*;

public class TrainedMicromixerGeometryCheck {
  public static Model run() {
    Model model = ModelUtil.create("Model");
    model.label("trained_micromixer_geometry_check.mph");
    model.modelNode().create("mod1");
    // Requirement: 微混合器的几何模型和参数如何设置，给出 MATLAB 建模代码
    // 正式运行前请复核几何尺寸、选择集和物理场特征名称。

    // Parameters merged from matched case memory and defaults.
    model.param().set("rho_ref", "2500[kg/m^3]", "默认密度；请替换为材料数据");
    model.param().set("E_ref", "35.1[GPa]", "默认杨氏模量；请替换为案例或文章数据");
    model.param().set("k_ref", "1[W/(m*K)]", "使用传热时的默认导热系数");
    model.param().set("hmax", "0.02[m]", "Maximum mesh size");
    model.param().set("L_ref", "1[m]", "Reference length");
    model.param().set("W_ref", "1[m]", "Reference width");
    model.param().set("H_ref", "0.1[m]", "Reference height");
    model.param().set("c0", "27[mol/m^3]", "微混合器");
    model.param().set("D", "4.5e-9[m^2/s]", "微混合器");
    model.param().set("h_max", "0.1[mm]", "微混合器");
    model.param().set("U_mean", "10[mm/s]", "微混合器");
    model.param().set("a", "1.4[mm]", "微混合器");
    model.param().set("alpha", "36*U_mean/a^4", "微混合器");
    model.param().set("th_bl_i", "1.0[mm]", "Blade thickness");
    model.param().set("l_bl_i", "24[mm]", "Blade length");
    model.param().set("r_mx_i", "5.0[mm]", "Mixer radius");
    model.param().set("n_bl", "5", "Number of blades");
    model.param().set("il_mx", "12[mm]", "Mixer inlet length");
    model.param().set("ol_mx", "18[mm]", "Mixer outlet length");
    model.param().set("l_mx", "n_bl*l_bl_i+il_mx+ol_mx", "Mixer length");
    model.param().set("rho_l", "1.0e3[kg/m^3]", "Liquid density");
    model.param().set("visc_l", "1.0e-2[Pa*s]", "Liquid viscosity");
    model.param().set("u_av", "5.0[cm/s]", "Average velocity");
    model.param().set("c_in", "1.0[mole/m^3]", "Inlet concentration");
    model.param().set("D1", "1.0e-10[m^2/s]", "Diffusivity");
    model.param().set("th_bl", "1[mm]", "geometry input parameter");
    model.param().set("l_bl", "24[mm]", "geometry input parameter");
    model.param().set("r_mx", "5[mm]", "geometry input parameter");
    model.param().set("nr_bl", "1", "geometry input parameter");
    model.param().set("mslevel", "2", "Menger sponge level");
    model.param().set("d", "3[um]", "热微执行器的简化模型");
    model.param().set("dw", "15[um]", "热微执行器的简化模型");

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
    model.component("comp1").physics().create("spf", "LaminarFlow", "geom1");
    // Add inlet, outlet, wall, and pressure conditions; switch interface for porous/fracture flow if needed.
    model.component("comp1").physics().create("ec", "ElectricCurrents", "geom1");
    // Add terminal, ground, and insulation boundary conditions.
    model.component("comp1").physics().create("acpr", "PressureAcoustics", "geom1");
    // Add sound hard, pressure, source, or radiation boundaries.
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
    model.result().numerical("gev1").label("volume_total");
    model.result().numerical("gev1").set("expr", "1");
    model.result().numerical().create("gev2", "EvalGlobal");
    model.result().numerical("gev2").label("surface_area_total");
    model.result().numerical("gev2").set("expr", "1");
    model.result().numerical().create("gev3", "EvalGlobal");
    model.result().numerical("gev3").label("entity_count");
    model.result().numerical("gev3").set("expr", "1");
    model.result().numerical().create("gev4", "EvalGlobal");
    model.result().numerical("gev4").label("geometry_build_success");
    model.result().numerical("gev4").set("expr", "1");

    return model;
  }

  public static void main(String[] args) {
    Model model = run();
    model.save("trained_micromixer_geometry_check.mph");
  }
}
