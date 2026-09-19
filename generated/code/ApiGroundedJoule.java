import com.comsol.model.*;
import com.comsol.model.util.*;

public class ApiGroundedJoule {
  public static Model run() {
    Model model = ModelUtil.create("Model");
    model.label("api_grounded_joule.mph");
    model.modelNode().create("mod1");
    // Requirement: copper electric current heat transfer joule heating, length 100 mm, width 50 mm, compare different voltages
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
    model.study("std1").create("stat", "Stationary");
    model.study("std1").feature().create("param", "Parametric");
    model.study("std1").feature("param").set("pname", new String[]{"Vtot"});
    model.study("std1").feature("param").set("plistarr", new String[]{"range(0.1[mV],0.025[mV],1[mV])"});
    // REVIEW REQUIRED: replace the voltage sweep range with the approved values.
    model.study("std1").createAutoSequences("all");
    // model.study("std1").run(); // Enable after selections, conditions, and solver settings are verified.

    // Derived values suggested by memory-assisted plan.
    model.result().numerical().create("gev1", "MaxSurface");
    model.result().numerical("gev1").label("Tmax");
    model.result().numerical("gev1").set("expr", "T");
    model.result().numerical().create("gev2", "AvSurface");
    model.result().numerical("gev2").label("Tavg");
    model.result().numerical("gev2").set("expr", "T");
    model.result().numerical().create("gev3", "EvalGlobal");
    model.result().numerical("gev3").label("heat_flux_integral");
    model.result().numerical("gev3").set("expr", "1");
    model.result().numerical().create("gev4", "MaxSurface");
    model.result().numerical("gev4").label("max_current_density");
    model.result().numerical("gev4").set("expr", "ec.normJ");
    model.result().numerical().create("gev5", "EvalGlobal");
    model.result().numerical("gev5").label("electric_resistance");
    model.result().numerical("gev5").set("expr", "1");
    // REVIEW REQUIRED: export terminal_current with a boundary integration over the verified terminal selection.

    return model;
  }

  public static void main(String[] args) {
    Model model = run();
    model.save("api_grounded_joule.mph");
  }
}
