# magnetic_prospecting_embedded

- Case directory: `D:\桌面\codex\案例下载\电气\铁矿床的磁法勘探`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-08-20T12:34:38.643993+00:00`

## File Summary

- count: 5
- kinds: {'comsol_mph': 1, 'matlab_livelink': 1, 'comsol_java': 1, 'json': 1, 'pdf_document': 1}
- matlab_files: 1
- java_files: 1
- pdf_files: 1
- pptx_files: 0
- mph_files: 1
- csv_files: 0
- json_files: 1

## Extracted Parameters

- `x_area` = `4836[m]` - Area W-E width
- `y_area` = `3410[m]` - Area N-S width
- `z_area` = `737[m]` - Depth
- `z_air` = `1196[m]` - Height
- `x_ore` = `2500[m]` - Ore ellipsoid, East position
- `y_ore` = `1500[m]` - Ore ellipsoid, North position
- `z_ore` = `-24[m]` - Ore ellipsoid, Vertical position
- `a_ore` = `200[m]` - Ore ellipsoid a-semiaxis
- `b_ore` = `1000[m]` - Ore ellipsoid b-semiaxis
- `c_ore` = `50[m]` - Ore ellipsoid c-semiaxis
- `alpha_ore` = `0[deg]` - Ore ellipsoid, angle from North (azimuth)
- `Bx_geo` = `4847.6[nT]` - Geomagnetic field, East component
- `By_geo` = `23732.1[nT]` - Geomagnetic field, North component
- `Bz_geo` = `-40748.8[nT]` - Geomagnetic field, Vertical component
- `image_scaling` = `458[m]` - Scaling for Image function
- `dem_scaling` = `0[m]` - Scaling for DEM file
- `geomag_elevation` = `0[km]` - Elevation for geomagnetic field data retrieval
- `mur_magn` = `3.5` - Relative permeability of the magnetic material
- `c_magn` = `.25` - Fraction of magnetic material in the ore
- `Brx_magn` = `0[nT]` - Remanent magnetic flux density of the magnetic material, East component
- `Bry_magn` = `0[nT]` - Remanent magnetic flux density of the magnetic material, North component
- `Brz_magn` = `0[nT]` - Remanent magnetic flux density of the magnetic material, Vertical component
- `mur_ore` = `1+(mur_magn-1)*c_magn` - Relative permeability of the ore
- `Br_magn` = `75398[nT]` - Remanent magnetic flux density of the magnetic material in the direction of the geomagnetic field
- `check` = `1` - Parameter used to check the validity of other parameters

## 内容级读取结果

- 模型树证据数量: 28
- 理论关键词: 电磁, 多孔介质/裂隙, 结构力学
- physics: Electric Currents, Magnetic Fields
- studies: Stationary

### 文件内容证据

- `magnetic_prospecting_embedded.m`: 参数=20, 几何=0, 物理场=0, 研究=0, 结果=0
- `magnetic_prospecting_embedded.java`: 参数=20, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.acdc.magnetic_prospecting.pdf`: 参数=0, 几何=0, 物理场=2, 研究=1, 结果=0
- `magnetic_prospecting_embedded.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `magnetic_prospecting_embedded_summary.json`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0

## 每个 PDF 文件的简单总结

- `models.acdc.magnetic_prospecting.pdf`: models.acdc.magnetic_prospecting.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果，主要物理场线索为 Electric Currents、Magnetic Fields，研究类型线索为 Stationary；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；of local geomagnetic anomalies — deviations of the natural magnetostatic fields from their

## PDF Summary and Physics Judgement

- Simple summary: magnetic_prospecting_embedded 主要研究模型中的主要物理现象和输出量，PDF 用来说明问题目标、基本假设和求解对象；从核心内容看，建模时应优先选择 Solid Mechanics，并采用 Stationary 研究。
- Primary physics: `Solid Mechanics`
- Study type: `Stationary`
- Judgement rule: 若 PDF 的核心量和方程关键词指向 Solid Mechanics，并且脚本/文本中出现同类接口，就把它作为主物理场；研究类型可由 Stationary 确认。

### Judgement Evidence

- PDF: Model created in COMSOL Multiphysics 6.4
- PDF: of local geomagnetic anomalies — deviations of the natural magnetostatic fields from their
- PDF: Crustal magnetic anomalies may result from either induced or remnant magnetization of
- PDF: magnetization cause small deviations of magnetic fields from the norm (local geomagnetic
- 脚本/文本识别到的物理场: Electric Currents, Magnetic Fields
- 识别到的研究类型: Stationary
- 理论关键词: 电磁, 多孔介质/裂隙, 结构力学

## PDF Keywords to Geometry/Parameter/MATLAB Mapping

- Summary: 将 PDF 关键词、案例建模内容和 MATLAB/Java API 证据整理为可复用的几何与参数建模知识。
- PDF keywords: 电磁, 多孔介质/裂隙, 结构力学, models.acdc.magnetic_prospecting.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果，主要物理场线索为 Electric Currents、Magnetic Fields，研究类型线索为 Stationary；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；of local geomagnetic anomalies — deviations of the natural magnetostatic fields from their
- `x_area` -> Area W-E width; MATLAB: `model.param.set('x_area', value, description)`
- `y_area` -> Area N-S width; MATLAB: `model.param.set('y_area', value, description)`
- `z_area` -> Depth; MATLAB: `model.param.set('z_area', value, description)`
- `z_air` -> Height; MATLAB: `model.param.set('z_air', value, description)`
- `x_ore` -> Ore ellipsoid, East position; MATLAB: `model.param.set('x_ore', value, description)`
- `y_ore` -> Ore ellipsoid, North position; MATLAB: `model.param.set('y_ore', value, description)`
- `z_ore` -> Ore ellipsoid, Vertical position; MATLAB: `model.param.set('z_ore', value, description)`
- `a_ore` -> Ore ellipsoid a-semiaxis; MATLAB: `model.param.set('a_ore', value, description)`
- `b_ore` -> Ore ellipsoid b-semiaxis; MATLAB: `model.param.set('b_ore', value, description)`
- `c_ore` -> Ore ellipsoid c-semiaxis; MATLAB: `model.param.set('c_ore', value, description)`
- `alpha_ore` -> Ore ellipsoid, angle from North (azimuth); MATLAB: `model.param.set('alpha_ore', value, description)`
- `Bx_geo` -> Geomagnetic field, East component; MATLAB: `model.param.set('Bx_geo', value, description)`

### Geometry and Parameter Checks

- 先根据 PDF 关键词判断几何对象、控制变量和输出量，再用 MATLAB/Java 模型树证据确认。
- 全局参数应优先来自 model.param.set、inputParam 或案例参数表，缺失时用待确认占位参数。
- 几何应先参数化，再创建命名选择集，避免后续边界条件依赖不稳定的实体编号。
- MATLAB 建模应按 parameter -> geom.create/feature -> selection -> physics.create -> mesh -> study 的顺序生成。
- 已识别物理场证据：Electric Currents；Magnetic Fields
- 已识别参数：x_area、y_area、z_area、z_air、x_ore、y_ore、z_ore、a_ore、b_ore、c_ore、alpha_ore、Bx_geo

## Modeling Principles Learned

- Readiness: `modeling_principles_ready`

### core_sequence

- 先定义全局参数和单位，再建立几何与选择集。
- 随后配置材料、物理场接口、边界条件、网格、研究/求解器和结果导出。
- 自动建模时必须保持 COMSOL 模型树顺序一致，避免先创建依赖后创建上游对象。
- 本案例已提取 25 个参数，可作为约束 JSON 和参数扫描变量。

### physics_reasoning

- 物理场接口来自 MATLAB/Java/摘要中的 physics.create 证据，应作为自动建模的主约束。
- 识别到物理场证据：Electric Currents
- 识别到物理场证据：Magnetic Fields
- 理论关键词可用于判断控制方程、变量含义和验证目标。

### automation_evidence

- MATLAB/Java 文件可直接提供 COMSOL API 调用顺序，是自动建模最可靠的文本证据。
- MPH 文件被视为权威模型来源；若存在同名 MATLAB/Java/JSON 摘要，系统会读取这些旁路证据。

### verification_logic

- 生成模型后先运行基准算例，再做网格无关性和参数扫描。
- 若需要训练代理模型，必须导出包含输入参数和目标输出的 CSV。
- 训练后用未参与训练的 COMSOL 结果复核 RMSE、MAE、R2 和物理趋势。

## Thinking and Extension

- Readiness: `ready_for_reasoning_and_extension`

### transferable_knowledge

- Reuse the learned COMSOL order: parameters -> geometry -> selections -> materials -> physics -> mesh -> study -> results.
- Treat extracted parameters as future constraint variables and parametric sweep inputs.
- Transfer recognized physics interfaces to similar requirements: Electric Currents, Magnetic Fields.
- Use the learned study types as solver starting points: Stationary.

### extension_questions

- Which parameters control geometry size, material response, boundary loading, and solver stability?
- Which output quantities can be converted into CSV columns for surrogate-model training?
- Can the same physics be tested under steady, transient, eigenfrequency, or parametric-sweep studies?
- How do the theory keywords change governing equations, assumptions, or validation targets: 电磁, 多孔介质/裂隙, 结构力学?
- Can COMSOL/LiveLink export a model-tree summary from the MPH file to verify selections and boundary IDs?

### new_model_directions

- Extend to load-case comparison, stress concentration analysis, and displacement safety checks.
- Build a corrected model workflow that separates geometry repair, material assignment, constraints, and load verification.
- Extend to terminal-current, resistance, field-distribution, and Joule-loss studies.
- Use electric-current outputs as coupling sources for thermal or structural models.

### parameter_sweep_ideas

- Sweep `x_area` around the learned value `4836[m]` and export target outputs to CSV.
- Sweep `y_area` around the learned value `3410[m]` and export target outputs to CSV.
- Sweep `z_area` around the learned value `737[m]` and export target outputs to CSV.
- Sweep `z_air` around the learned value `1196[m]` and export target outputs to CSV.
- Sweep `x_ore` around the learned value `2500[m]` and export target outputs to CSV.
- Sweep `y_ore` around the learned value `1500[m]` and export target outputs to CSV.
- Sweep `z_ore` around the learned value `-24[m]` and export target outputs to CSV.
- Sweep `a_ore` around the learned value `200[m]` and export target outputs to CSV.
- Create a COMSOL parametric sweep table first; each row should contain input parameters and derived output quantities.

### code_generation_ideas

- Use existing MATLAB/Java scripts as the highest-confidence source for API call order.
- Generate a baseline MATLAB LiveLink builder from the learned parameter and model-tree evidence.
- Generate a Java builder with comments on boundary selections that must be verified inside COMSOL.
- Create a CSV export script for derived values before training a numerical surrogate.

### risk_checks

- Boundary IDs and named selections must be verified after geometry changes.
- Material properties and units must be checked before using generated scripts for real simulation.
- Mesh independence and baseline-solve convergence should be checked before parameter sweeps.
- No CSV sweep data was detected, so current learning supports reasoning and code generation more than numerical surrogate training.

## Thoughts

- PDF 文档用于理解案例目的、建模顺序、理论假设和验证目标。
- MATLAB 和 Java 文件是 COMSOL 模型树的可执行证据，应驱动自动建模脚本生成。
- MPH 文件需要通过 COMSOL with MATLAB 导出摘要后，才能可靠使用内部模型设置。
- 参数文本和脚本证据可转换为约束和参数扫描变量。
- 已从案例内容中抽取到模型树证据，可用于学习几何、物理场、材料、网格、研究和结果设置。
- 未发现训练 CSV，因此数值代理模型训练前需要先导出 COMSOL 参数扫描数据。

## Learning Summary After This Case

- Summary: 已学习 magnetic_prospecting_embedded 的 5 个文件；训练阶段=modeling_logic_learning_ready；参数数量=25；内容证据=28 条。
- Training readiness: modeling_logic_ready_but_needs_comsol_sweep_csv
- Reusable confidence: high

### 学到的建模逻辑

- Case files were treated as one COMSOL evidence package: documentation, scripts, binary model files, parameters, and data.
- The model tree should be reconstructed in this order: parameters, geometry, selections, materials, physics, mesh, study, results, and exports.
- MATLAB/Java scripts provide reusable COMSOL API call patterns for automated model construction.
- PDF documentation provides modeling purpose, assumptions, theoretical context, and validation targets.
- MPH files are remembered as authoritative model artifacts, but detailed internal settings require COMSOL/LiveLink extraction.
- 检测到的参数可用于生成约束 JSON，后续也可作为代理模型训练的扫描变量。
- 已完成内容级读取：从案例文件中抽取了参数、几何、物理场、材料、网格、研究、结果和边界条件等模型树证据。

### Reusable Assets

- 25 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Theory and workflow evidence from PDF documents.
- Original MPH files for later COMSOL-side verification.
- 28 条内容级模型树证据。

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 5 个案例文件；MATLAB=1，Java=1，PDF=1，MPH=1，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 内容级模型树抽取**
  - Evidence: 抽取到模型树证据 28 条；几何=0，物理场=2，材料=0，网格=0，研究=1，结果=0。
  - Judgement: 模型已读取案例内容并抽取 COMSOL 模型树结构，可用于后续自动建模和代码生成。
- **3. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：magnetic_prospecting_embedded.m, magnetic_prospecting_embedded.java
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **4. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 25 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **5. 理论与模型来源判断**
  - Evidence: PDF 文档=1，MPH 模型=1。
  - Judgement: PDF 用于补充理论、假设和教程目标；MPH 作为权威模型文件，后续应通过 COMSOL/LiveLink 提取内部设置。
- **6. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **7. 记忆库补充**
  - Evidence: 案例标题为 magnetic_prospecting_embedded，训练阶段为 modeling_logic_learning_ready。
  - Judgement: 该案例的文件摘要、参数、建模逻辑和下一步动作会写入案例知识库，并可被后续自动建模方案检索复用。

### Next Actions

- 把 PDF、MATLAB、Java、MPH、TXT、JSON 和 CSV 证据作为一个完整案例包读取。
- Extract model purpose, geometry sequence, parameters, selections, and model-tree features.
- Convert detected parameters into a constraints JSON with units and valid ranges.
- Use MATLAB/Java evidence to generate or adapt a LiveLink MATLAB builder.
- Run a COMSOL parametric sweep over selected parameters.
- Export a CSV containing input parameters and target outputs.
- Train the local surrogate model after the CSV exists.
- 几何和建模逻辑验证后，运行 COMSOL 参数扫描并导出 CSV 训练数据。

## Deep Learning Capability Plan

- Readiness: `ready_to_generate_comsol_sweep_dataset`
- Score: `70`

### Candidate Inputs

- `x_area`
- `y_area`
- `z_area`
- `z_air`
- `x_ore`
- `y_ore`
- `z_ore`
- `a_ore`
- `b_ore`
- `c_ore`
- `alpha_ore`
- `Bx_geo`
- `By_geo`
- `Bz_geo`
- `image_scaling`
- `dem_scaling`
- `geomag_elevation`
- `mur_magn`
- `c_magn`
- `Brx_magn`
- `Bry_magn`
- `Brz_magn`
- `mur_ore`
- `Br_magn`
- `check`

### Candidate Outputs

- `terminal_current`

### Training Workflow

- 读取 PDF/MATLAB/Java/MPH/CSV，把案例整理为统一证据包。
- 从脚本和文本中提取参数、几何、物理场、材料、网格、研究和结果节点。
- 把候选输入参数转成约束 JSON，并确定扫描范围。
- 运行 COMSOL 参数扫描，导出包含输入列和目标输出列的 CSV。
- 对比 baseline、Ridge、RandomForest、MLP，按测试 RMSE/MAE/R2 选择最佳模型。
- 用未参与训练的新 COMSOL 结果复核代理模型，并把训练报告写回案例记忆库。

### Dataset Requirements

- 当前案例未发现 CSV，需要先用 COMSOL 参数扫描导出训练数据。
- 每一行代表一次 COMSOL 参数扫描或验证运行。
- 输入列应来自案例参数、几何尺寸、材料参数、边界条件或工况变量。
- 输出列应来自最大值、平均值、积分量、目标函数、误差、位移、应力、温度、流量、电流等可验证结果。
- 训练前保留单位说明，并把 CSV、约束 JSON、生成脚本和模型报告一起保存为同一个训练记录。

## External Knowledge Alignment


### Similar Master Cases

- No master case index match was available.

### Official Documentation Checks

- No official documentation index match was available.

### Training Improvements

- 将单案例摘要升级为：本地案例证据 + 总案例库相似案例 + 官方文档校对的三层学习结果。
- 学习完成后先判断证据字段是否覆盖 geometry、materials、physics、boundary_conditions、mesh、solver、results。
- 未找到可用总案例库匹配时，只把当前案例作为局部经验，不自动推断未见过的 COMSOL 设置。
- 缺少官方文档索引匹配时，将 API 用法标记为待校对。
- 没有 CSV 时只完成建模逻辑学习；需要先完成 COMSOL 参数扫描、导出 CSV，再训练代理模型。

## Implementation Path

- 把 PDF、MATLAB、Java、MPH、TXT、JSON 和 CSV 证据作为一个完整案例包读取。
- Extract model purpose, geometry sequence, parameters, selections, and model-tree features.
- Convert detected parameters into a constraints JSON with units and valid ranges.
- Use MATLAB/Java evidence to generate or adapt a LiveLink MATLAB builder.
- Run a COMSOL parametric sweep over selected parameters.
- Export a CSV containing input parameters and target outputs.
- Train the local surrogate model after the CSV exists.

## Gaps

- Missing parameter-sweep CSV for numerical surrogate training.
- MPH files need COMSOL with MATLAB summaries for reliable internal settings.

## Source Files

- `magnetic_prospecting_embedded.mph` (comsol_mph, 37921892 bytes)
- `magnetic_prospecting_embedded.m` (matlab_livelink, 20162 bytes)
- `magnetic_prospecting_embedded.java` (comsol_java, 21563 bytes)
- `magnetic_prospecting_embedded_summary.json` (json, 1546 bytes)
- `models.acdc.magnetic_prospecting.pdf` (pdf_document, 1231145 bytes)
