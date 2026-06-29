# COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究

- Source: `D:\桌面\COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究.docx`
- Paragraphs: 23

## Article Summary

文章围绕煤层超高压水力压裂数值模拟，研究不同地应力条件、主应力方向、煤层非均匀性和天然裂缝对单孔裂纹起裂压力、扩展方向、损伤演化和裂缝长度的影响。

## Modeling Requirement

Build a COMSOL hydraulic fracturing model for a single borehole under different confining stress conditions. 中文需求关键词：水力压裂 单孔 围压 主应力 天然裂缝 煤层 岩石裂隙流 多孔介质 裂缝拓展 损伤演化。 Use article parameters: square_side=300[mm] borehole_diameter=15[mm] stress_ratio_range=1.5~2.0 initial_pressure=0.1[MPa] mean_elastic_modulus=35.1[GPa] mean_compressive_strength=152[MPa] principal_stress_direction_135=135[deg] principal_stress_direction_180=180[deg] principal_stress_direction_90=90[deg]. Include features: 2D square domain central borehole natural fracture or weak-plane features coal/rock medium heterogeneous elastic modulus heterogeneous tensile/compressive strength Weibull random field distribution solid mechanics damage evolution pore/fluid pressure loading hydraulic fracture propagation outer boundary in-situ stress loading symmetric roller/fixed displacement support borehole injection pressure free triangular mesh local refinement near borehole and natural fractures time-dependent pressure/damage evolution parametric sweep over stress ratio and stress direction damage length vs time pressure field fracture path initiation pressure stress distribution fracture deflection and branching under natural fractures.

## Extracted Parameters

- `square_side` = `300[mm]` (geometry length)
- `borehole_diameter` = `15[mm]` (borehole diameter)
- `stress_ratio_range` = `1.5~2.0` (principal stress ratio range)
- `initial_pressure` = `0.1[MPa]` (initial pressure)
- `mean_elastic_modulus` = `35.1[GPa]` (Weibull mean elastic modulus)
- `mean_compressive_strength` = `152[MPa]` (Weibull mean compressive strength)
- `principal_stress_direction_135` = `135[deg]` (stress direction case)
- `principal_stress_direction_180` = `180[deg]` (stress direction case)
- `principal_stress_direction_90` = `90[deg]` (stress direction case)

## Model Features

- geometry: 2D square domain, central borehole, natural fracture or weak-plane features
- materials: coal/rock medium, heterogeneous elastic modulus, heterogeneous tensile/compressive strength, Weibull random field distribution
- physics: solid mechanics damage evolution, pore/fluid pressure loading, hydraulic fracture propagation
- boundary_conditions: outer boundary in-situ stress loading, symmetric roller/fixed displacement support, borehole injection pressure
- mesh: free triangular mesh, local refinement near borehole and natural fractures
- studies: time-dependent pressure/damage evolution, parametric sweep over stress ratio and stress direction
- outputs: damage length vs time, pressure field, fracture path, initiation pressure, stress distribution, fracture deflection and branching under natural fractures

## Correction Strategy

- Use the article parameters as the baseline constraints instead of generic thermal or structural defaults.
- Correct geometry to a 300 mm square domain with a 15 mm borehole and optional natural-fracture weak planes.
- Correct loads by sweeping principal stress ratio from 1.5 to 2.0 and stress directions such as 90, 135, and 180 degrees.
- Correct material definition by adding Weibull-distributed elastic modulus and strength rather than a single homogeneous material.
- Correct mesh by refining near the borehole, expected crack tips, and natural fractures.
- Correct validation outputs to compare damage length over time, pressure field, crack morphology, and initiation pressure against article/field observations.
- Add a measurement-correction loop: compare simulated fracture/stress response with measured data and update fracture orientation, density, and weak-plane parameters.

## Memory-Assisted COMSOL Construction Plan

### Retrieved Cases
- `岩石裂隙流` score=5.760901812651248
- `dynamic_loaded_beam` score=5.302434289526359
- `pulley_stress` score=5.276939015148195
- `瞬态声压级6.3` score=5.204828993353749
- `激波管` score=5.1453125733564
- `圆柱绕流` score=5.082003561600919
- `螺旋静态混合器` score=5.067489992328232
- `真空干燥` score=5.061957298559955

### Construction Steps
- Clarify model objective, dimensionality, input parameters, outputs, and validation targets.
- Review retrieved similar cases and reuse their parameter names, geometry sequence, and LiveLink API patterns.
- Choose geometry strategy: reuse similar case script, import CAD, or generate parametric geometry.
- Define materials, units, selections, and reusable parameter groups.
- Add physics interfaces and boundary/initial conditions.
- Create mesh and study sequence, then solve a baseline model.
- Export derived values and plots for validation.

### Article-Specific Modifications
- Use the article parameters as the baseline constraints instead of generic thermal or structural defaults.
- Correct geometry to a 300 mm square domain with a 15 mm borehole and optional natural-fracture weak planes.
- Correct loads by sweeping principal stress ratio from 1.5 to 2.0 and stress directions such as 90, 135, and 180 degrees.
- Correct material definition by adding Weibull-distributed elastic modulus and strength rather than a single homogeneous material.
- Correct mesh by refining near the borehole, expected crack tips, and natural fractures.
- Correct validation outputs to compare damage length over time, pressure field, crack morphology, and initiation pressure against article/field observations.
- Add a measurement-correction loop: compare simulated fracture/stress response with measured data and update fracture orientation, density, and weak-plane parameters.

### Validation Outputs
- damage length vs time
- pressure field
- fracture path
- initiation pressure
- stress distribution
- fracture deflection and branching under natural fractures
