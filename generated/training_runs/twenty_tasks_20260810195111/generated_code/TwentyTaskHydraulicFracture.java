import com.comsol.model.*;
import com.comsol.model.util.*;

public class TwentyTaskHydraulicFracture {
  public static Model run() {
    Model model = ModelUtil.create("Model");
    model.label("twenty_task_hydraulic_fracture.mph");
    model.modelNode().create("mod1");
    // Requirement: 二维煤层单孔水力压裂建模
    // GENERATION STATUS: REVIEW_REQUIRED until verification JSON reports ready_to_solve=true.

    // Parameters merged from matched case memory and defaults.
    model.param().set("rho_ref", "998[kg/m^3]", "Material density");
    model.param().set("k_ref", "0.6[W/(m*K)]", "Material thermal conductivity");
    model.param().set("Cp_ref", "4182[J/(kg*K)]", "Material heat capacity");
    model.param().set("sigma_ref", "1[S/m]", "Material electrical conductivity");
    model.param().set("hmax", "0.02[m]", "Maximum mesh size");
    model.param().set("L_ref", "1[m]", "Reference length");
    model.param().set("W_ref", "1[m]", "Reference width");
    model.param().set("H_ref", "0.1[m]", "Reference height");
    model.param().set("square_side", "300[mm]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("borehole_diameter", "15[mm]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("stress_ratio_range", "1.5~2.0", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("initial_pressure", "0.1[MPa]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("mean_elastic_modulus", "35.1[GPa]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("mean_compressive_strength", "152[MPa]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("principal_stress_direction_135", "135[deg]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("principal_stress_direction_180", "180[deg]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("principal_stress_direction_90", "90[deg]", "COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究");
    model.param().set("E", "210[GPa]", "杨氏模量");
    model.param().set("alpha", "12e-6[1/K]", "热膨胀系数");
    model.param().set("T_hot", "373.15[K]", "热端温度");
    model.param().set("T_cold", "293.15[K]", "冷端温度");
    model.param().set("L", "0.05[m]", "长度");
    model.param().set("W", "0.02[m]", "宽度");
    model.param().set("k", "16[W/(m*K)]", "导热系数");
    model.param().set("heat_flux", "8000[W/m^2]", "热流");
    model.param().set("hconv", "35[W/(m^2*K)]", "对流换热系数");
    model.param().set("nu", "0.3", "泊松比");
    model.param().set("p_load", "1[MPa]", "均布边界载荷");
    model.param().set("H_v", "500[kJ/kg]", "Heat of Vaporization");
    model.param().set("rho", "1200[kg/m^3]", "Density");
    model.param().set("Cp", "1000[J/kg/K]", "Specific Heat");
    model.param().set("A", "20e3[1/s]", "Frfequency Factor");
    model.param().set("E_a", "50[kJ/mol]", "Activation Energy");
    model.param().set("ft", "1", "抗拉强度");
    model.param().set("fc", "1", "抗压强度");
    model.param().set("Gc", "1", "断裂能");
    model.param().set("epsilon", "1", "表面发射率");
    model.param().set("alpha_T", "1", "热膨胀系数");

    model.component().create("comp1", true);
    model.component("comp1").geom().create("geom1", 2);
    model.component("comp1").geom("geom1").lengthUnit("m");
    // REVIEW REQUIRED: confirm that the selected geometry pattern matches the approved dimensions.
    // Geometry guidance: 几何与参数应优先按“水力压裂单孔/裂隙几何”组织。
    model.component("comp1").geom("geom1").create("rect1", "Rectangle");
    model.component("comp1").geom("geom1").feature("rect1").set("size", new String[]{"Lx", "Ly"});
    model.component("comp1").geom("geom1").feature("rect1").set("pos", new String[]{"-Lx/2", "-Ly/2"});
    model.component("comp1").geom("geom1").create("c1", "Circle");
    model.component("comp1").geom("geom1").feature("c1").set("r", "rb");
    model.component("comp1").geom("geom1").create("dif1", "Difference");
    model.component("comp1").geom("geom1").feature("dif1").selection("input").set(new String[]{"rect1"});
    model.component("comp1").geom("geom1").feature("dif1").selection("input2").set(new String[]{"c1"});
    // REVIEW REQUIRED: add the approved fracture/weak-plane or phase-field initialization.
    model.component("comp1").geom("geom1").run();
    // REVIEW REQUIRED: bind borehole, outer-boundary, and rock-domain named selections.

    model.component("comp1").material().create("mat1", "Common");
    model.component("comp1").material("mat1").label("Water");
    model.component("comp1").material("mat1").selection().all();
    model.component("comp1").material("mat1").propertyGroup("def").set("density", "rho_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("thermalconductivity", "k_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("heatcapacity", "Cp_ref");
    model.component("comp1").material("mat1").propertyGroup("def").set("electricconductivity", "sigma_ref");

    // Physics inferred from requirement, matched cases, and COMSOL knowledge memory.
    model.component("comp1").physics().create("gph", "GeneralFormPDE", "geom1");
    // 请替换为已学习案例所需的准确 COMSOL 物理接口。
    // 边界选择目前是占位内容。请在 COMSOL 中检查生成几何的边界编号。

    model.component("comp1").mesh().create("mesh1");
    model.component("comp1").mesh("mesh1").create("size1", "Size");
    model.component("comp1").mesh("mesh1").feature("size1").set("custom", true);
    model.component("comp1").mesh("mesh1").feature("size1").set("hmax", "hmax");
    model.component("comp1").mesh("mesh1").run();

    model.study().create("std1");
    model.study("std1").create("stat", "Stationary");
    model.study("std1").createAutoSequences("all");
    // model.study("std1").run(); // Enable after selections, conditions, and solver settings are verified.

    // Derived values suggested by memory-assisted plan.
    model.result().numerical().create("gev1", "EvalGlobal");
    model.result().numerical("gev1").label("primary_quantity_of_interest");
    model.result().numerical("gev1").set("expr", "1");
    model.result().numerical().create("gev2", "EvalGlobal");
    model.result().numerical("gev2").label("validation_error");
    model.result().numerical("gev2").set("expr", "1");

    return model;
  }

  public static void main(String[] args) {
    Model model = run();
    model.save("twenty_task_hydraulic_fracture.mph");
  }
}
