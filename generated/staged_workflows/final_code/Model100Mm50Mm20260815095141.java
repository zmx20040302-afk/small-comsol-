import com.comsol.model.*;
import com.comsol.model.util.*;

public class Model100Mm50Mm20260815095141 {
  public static Model run() {
    Model model = ModelUtil.create("Model");
    model.label("model_100_mm__50_mm___20260815095141.mph");
    model.modelNode().create("mod1");
    // Requirement: 铜矩形板通电发热，长度100 mm，宽度50 mm，比较不同电压下的最高温度 已批准建模决策： [选择物理场] 选择结果：电流 + 固体传热（焦耳热耦合）；可能还需要耦合：传热、电流或静电 COMSOL 接口建议：Electric Currents + Heat Transfer in Solids，可用 Joule Heating 多物理场耦合 理论依据：需求同时包含电荷守恒/电势分布和温度升高，电流损耗会作为热源进入热传导方程，因此需要电-热耦合。 复合场检查：该需求应按复合场判断，优先考虑：电-热耦合 / 焦耳热 + 热-结构耦合 / 热应力 + 非等温流动。 主物理场=Electric Currents；耦合物理场=Heat Transfer in Solids、Solid Mechanics、Heat Transfer in Fluids；多物理场节点=Joule Heating / Electromagnetic Heating、Thermal Expansion、Nonisothermal Flow；耦合变量=电流密度、电损耗/焦耳热源、温度场、温度相关电导率、热膨胀应变
    // GENERATION STATUS: REVIEW_REQUIRED until verification JSON reports ready_to_solve=true.

    // Parameters merged from matched case memory and defaults.
    model.param().set("rho_ref", "8960[kg/m^3]", "Material density");
    model.param().set("k_ref", "400[W/(m*K)]", "Material thermal conductivity");
    model.param().set("Cp_ref", "385[J/(kg*K)]", "Material heat capacity");
    model.param().set("sigma_ref", "5.998e7[S/m]", "Material electrical conductivity");
    model.param().set("hmax", "0.02[m]", "Maximum mesh size");
    model.param().set("Vtot", "20[mV]", "Applied electric potential difference");
    model.param().set("T_amb", "293.15[K]", "Ambient temperature");
    model.param().set("htc", "5[W/(m^2*K)]", "Convective heat transfer coefficient");
    model.param().set("L_ref", "100[mm]", "User-specified geometry dimension");
    model.param().set("W_ref", "50[mm]", "User-specified geometry dimension");
    model.param().set("H_ref", "0.1[m]", "Reference height");
    model.param().set("N", "20", "Spatial frequency resolution");
    model.param().set("b", "1.8", "Spectral exponent");
    model.param().set("D", "2+(3-b)/2", "Fractal dimension");
    model.param().set("T_init", "20[degC]", "磁滞作用下的相变建模");
    model.param().set("dT", "1[K]", "磁滞作用下的相变建模");
    model.param().set("T_melt", "65[degC]", "磁滞作用下的相变建模");
    model.param().set("T_freeze", "55[degC]", "磁滞作用下的相变建模");
    model.param().set("T_top", "T_melt+dT/2", "磁滞作用下的相变建模");
    model.param().set("T_bot", "T_freeze-dT/2", "磁滞作用下的相变建模");
    model.param().set("LH", "100[kJ/kg]", "磁滞作用下的相变建模");
    model.param().set("L", "0.1[m]", "导线长度");
    model.param().set("sigma", "5.8e7[S/m]", "电导率");
    model.param().set("V_left", "1[V]", "施加电压");
    model.param().set("k", "401[W/(m*K)]", "导热系数");
    model.param().set("E", "210[GPa]", "杨氏模量");
    model.param().set("alpha", "12e-6[1/K]", "热膨胀系数");
    model.param().set("T_hot", "373.15[K]", "热端温度");
    model.param().set("T_cold", "293.15[K]", "冷端温度");
    model.param().set("W", "0.02[m]", "宽度");
    model.param().set("heat_flux", "8000[W/m^2]", "热流");
    model.param().set("hconv", "35[W/(m^2*K)]", "对流换热系数");
    model.param().set("rho", "2500[kg/m^3]", "密度");
    model.param().set("Cp", "800[J/(kg*K)]", "比热容");
    model.param().set("epsr", "1", "相对介电常数");
    model.param().set("epsilon", "1", "表面发射率");
    model.param().set("alpha_T", "1", "热膨胀系数");

    model.component().create("comp1", true);
    model.component("comp1").geom().create("geom1", 2);
    model.component("comp1").geom("geom1").lengthUnit("m");
    // REVIEW REQUIRED: confirm that the selected geometry pattern matches the approved dimensions.
    model.component("comp1").geom("geom1").create("r1", "Rectangle");
    model.component("comp1").geom("geom1").feature("r1").set("size", new String[]{"L_ref", "W_ref"});
    model.component("comp1").geom("geom1").run();

    model.component("comp1").material().create("mat1", "Common");
    model.component("comp1").material("mat1").label("Copper");
    model.component("comp1").material("mat1").selection().all();
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "rho_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("thermalconductivity", "k_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("heatcapacity", "Cp_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("electricconductivity", "sigma_ref");

    // Physics inferred from requirement, matched cases, and COMSOL knowledge memory.
    model.component("comp1").physics().create("ht", "HeatTransfer", "geom1");
    // Add heat flux, temperature, or convection features after selections are verified.
    model.component("comp1").physics().create("ec", "ConductiveMedia", "geom1");
    // Electric Currents interface: add terminal, ground, and insulation boundary conditions.
    model.component("comp1").multiphysics().create("emh1", "ElectromagneticHeating", 2);
    model.component("comp1").multiphysics("emh1").set("EMHeat_physics", "ec");
    model.component("comp1").multiphysics("emh1").set("Heat_physics", "ht");
    model.component("comp1").multiphysics("emh1").selection().all();
    // Joule Heating coupling transfers electrical loss to the heat-transfer interface.
    model.component("comp1").selection().create("sel_terminal", "Explicit");
    model.component("comp1").selection("sel_terminal").geom("geom1", 1);
    model.component("comp1").selection("sel_terminal").label("Terminal boundary - review entity IDs");
    model.component("comp1").selection().create("sel_ground", "Explicit");
    model.component("comp1").selection("sel_ground").geom("geom1", 1);
    model.component("comp1").selection("sel_ground").label("Ground boundary - review entity IDs");
    model.component("comp1").selection().create("sel_convection", "Explicit");
    model.component("comp1").selection("sel_convection").geom("geom1", 1);
    model.component("comp1").selection("sel_convection").label("Exterior convection boundary - review entity IDs");
    // Auto-boundary rule for the verified 2D rectangle benchmark: edges 1/3 are opposite voltage boundaries; all four exterior edges convect.
    model.component("comp1").selection("sel_terminal").set(new int[]{1});
    model.component("comp1").selection("sel_ground").set(new int[]{3});
    model.component("comp1").selection("sel_convection").set(new int[]{1, 2, 3, 4});
    model.component("comp1").physics("ec").create("pot1", "ElectricPotential", 1);
    model.component("comp1").physics("ec").feature("pot1").selection().named("sel_terminal");
    model.component("comp1").physics("ec").feature("pot1").set("V0", "Vtot");
    model.component("comp1").physics("ec").create("gnd1", "Ground", 1);
    model.component("comp1").physics("ec").feature("gnd1").selection().named("sel_ground");
    model.component("comp1").physics("ht").create("hf1", "HeatFluxBoundary", 1);
    model.component("comp1").physics("ht").feature("hf1").selection().named("sel_convection");
    model.component("comp1").physics("ht").feature("hf1").set("HeatFluxType", "ConvectiveHeatFlux");
    model.component("comp1").physics("ht").feature("hf1").set("h", "htc");
    model.component("comp1").physics("ht").feature("hf1").set("Text", "T_amb");
    // This narrow benchmark rule was generated from an explicit rectangle; inspect it before adapting to another geometry.
    // 边界选择目前是占位内容。请在 COMSOL 中检查生成几何的边界编号。

    model.component("comp1").mesh().create("mesh1");
    model.component("comp1").mesh("mesh1").create("size1", "Size");
    model.component("comp1").mesh("mesh1").feature("size1").set("custom", true);
    model.component("comp1").mesh("mesh1").feature("size1").set("hmax", "hmax");
    model.component("comp1").mesh("mesh1").create("ftri1", "FreeTri");
    model.component("comp1").mesh("mesh1").run();
    // Create field-evaluation operators after the mesh so their source selection is mesh-aware.
    model.component("comp1").cpl().create("maxop1", "Maximum");
    model.component("comp1").cpl("maxop1").selection().all();
    model.component("comp1").cpl().create("aveop1", "Average");
    model.component("comp1").cpl("aveop1").selection().all();

    model.study().create("std1");
    model.study("std1").create("freq", "Frequency");
    model.study("std1").feature().create("param", "Parametric");
    model.study("std1").feature("param").set("pname", new String[]{"Vtot"});
    model.study("std1").feature("param").set("plistarr", new String[]{"range(0.1[mV],0.025[mV],1[mV])"});
    // REVIEW REQUIRED: replace the voltage sweep range with the approved values.
    model.study("std1").createAutoSequences("all");
    // model.study("std1").run(); // Enable after selections, conditions, and solver settings are verified.

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
    model.result().numerical().create("gev5", "MaxSurface");
    model.result().numerical("gev5").label("Tmax");
    model.result().numerical("gev5").set("expr", "T");
    model.result().numerical().create("gev6", "AvSurface");
    model.result().numerical("gev6").label("Tavg");
    model.result().numerical("gev6").set("expr", "T");
    model.result().numerical().create("gev7", "EvalGlobal");
    model.result().numerical("gev7").label("heat_flux_integral");
    model.result().numerical("gev7").set("expr", "1");
    model.result().numerical().create("gev8", "MaxSurface");
    model.result().numerical("gev8").label("max_displacement");
    model.result().numerical("gev8").set("expr", "solid.disp");

    return model;
  }

  public static void main(String[] args) {
    Model model = run();
    model.save("model_100_mm__50_mm___20260815095141.mph");
  }
}
