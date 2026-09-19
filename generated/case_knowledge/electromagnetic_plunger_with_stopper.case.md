# electromagnetic_plunger_with_stopper

- Case directory: `D:\桌面\codex\案例下载\电气\带制动器的电磁柱塞`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-08-16T10:44:15.840844+00:00`

## File Summary

- count: 5
- kinds: {'comsol_mph': 1, 'matlab_livelink': 1, 'comsol_java': 1, 'json': 1, 'presentation_document': 1}
- matlab_files: 1
- java_files: 1
- pdf_files: 0
- pptx_files: 1
- mph_files: 1
- csv_files: 0
- json_files: 1

## Extracted Parameters

- `R_p` = `5[mm]` - Plunger radius
- `Len_p` = `48[mm]` - Plunger length
- `z0_p` = `20[mm]` - Initial plunger position
- `Tip_R_p` = `3[mm]` - Tip radius of plunger
- `Cut_angle` = `43[deg]` - Cut angle of the plunger tip
- `Guider_width` = `1.5[mm]` - Width of the guider
- `Thickness_core` = `4[mm]` - Core thickness
- `Height_Coil` = `40[mm]` - Height of the coil
- `Width_Coil` = `8[mm]` - Width of the coil
- `Height_blocker` = `10[mm]` - Height of the blocker
- `Height_core` = `Height_Coil+2*Thickness_core` - Height of the core
- `gap` = `0.5[mm]` - Airgap between plunger and guider
- `dt` = `0.2[s]` - Pulse length
- `tau` = `0.01[s]` - Rise/Decay time
- `I0` = `4[A]` - Input Current
- `k` = `40[N/m]` - Spring constant
- `N_turn` = `200` - Number of turns in the coil
- `Dia_wire` = `1[mm]` - Diameter of the wire in the coil

## 内容级读取结果

- 模型树证据数量: 34
- 理论关键词: 电磁, 结构力学, 流体
- geometry: pol1 / Polygon, mov1 / Move, geom1 / pol1 / source, geom1 / pol1 / table, geom1 / mov1 / disply, r1 / Rectangle, geom1 / r1 / pos
- physics: Solid Mechanics, Magnetic Fields, Global ODEs and DAEs
- studies: Stationary, Time Dependent
- boundary_conditions: pol1 / source, pol1 / table, mov1 / disply, r1 / pos

### 文件内容证据

- `electromagnetic_plunger_with_stopper.java`: 参数=18, 几何=6, 物理场=2, 研究=0, 结果=0
- `electromagnetic_plunger_with_stopper.m`: 参数=18, 几何=5, 物理场=2, 研究=0, 结果=0
- `electromagnetic_plunger_with_stopper_63.pptx`: 参数=0, 几何=0, 物理场=3, 研究=2, 结果=0
- `electromagnetic_plunger_with_stopper.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `electromagnetic_plunger_with_stopper_summary.json`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0

## PDF Summary and Physics Judgement

- Simple summary: electromagnetic_plunger_with_stopper 主要研究流动速度、压力或输运过程，PDF 用来说明问题目标、基本假设和求解对象；从核心内容看，建模时应优先选择 Solid Mechanics，并采用 Time Dependent 研究。
- Primary physics: `Solid Mechanics`
- Study type: `Time Dependent`
- Judgement rule: 若 PDF 的核心量和方程关键词指向 Solid Mechanics，并且脚本/文本中出现同类接口，就把它作为主物理场；研究类型可由 Time Dependent 确认。

### Judgement Evidence

- 脚本/文本识别到的物理场: Solid Mechanics, Magnetic Fields, Global ODEs and DAEs
- 识别到的研究类型: Stationary, Time Dependent
- 理论关键词: 电磁, 结构力学, 流体

## PDF Keywords to Geometry/Parameter/MATLAB Mapping

- Summary: 将 PDF 关键词、案例建模内容和 MATLAB/Java API 证据整理为可复用的几何与参数建模知识。
- PDF keywords: 电磁, 结构力学, 流体
- `R_p` -> Plunger radius; MATLAB: `model.param.set('R_p', value, description)`
- `Len_p` -> Plunger length; MATLAB: `model.param.set('Len_p', value, description)`
- `z0_p` -> Initial plunger position; MATLAB: `model.param.set('z0_p', value, description)`
- `Tip_R_p` -> Tip radius of plunger; MATLAB: `model.param.set('Tip_R_p', value, description)`
- `Cut_angle` -> Cut angle of the plunger tip; MATLAB: `model.param.set('Cut_angle', value, description)`
- `Guider_width` -> Width of the guider; MATLAB: `model.param.set('Guider_width', value, description)`
- `Thickness_core` -> Core thickness; MATLAB: `model.param.set('Thickness_core', value, description)`
- `Height_Coil` -> Height of the coil; MATLAB: `model.param.set('Height_Coil', value, description)`
- `Width_Coil` -> Width of the coil; MATLAB: `model.param.set('Width_Coil', value, description)`
- `Height_blocker` -> Height of the blocker; MATLAB: `model.param.set('Height_blocker', value, description)`
- `Height_core` -> Height of the core; MATLAB: `model.param.set('Height_core', value, description)`
- `gap` -> Airgap between plunger and guider; MATLAB: `model.param.set('gap', value, description)`

### Geometry and Parameter Checks

- 先根据 PDF 关键词判断几何对象、控制变量和输出量，再用 MATLAB/Java 模型树证据确认。
- 全局参数应优先来自 model.param.set、inputParam 或案例参数表，缺失时用待确认占位参数。
- 几何应先参数化，再创建命名选择集，避免后续边界条件依赖不稳定的实体编号。
- MATLAB 建模应按 parameter -> geom.create/feature -> selection -> physics.create -> mesh -> study 的顺序生成。
- 已识别几何证据：pol1 / Polygon；mov1 / Move；geom1 / pol1 / source；geom1 / pol1 / table；geom1 / mov1 / disply；r1 / Rectangle
- 已识别物理场证据：Solid Mechanics；Magnetic Fields；Global ODEs and DAEs
- 已识别参数：R_p、Len_p、z0_p、Tip_R_p、Cut_angle、Guider_width、Thickness_core、Height_Coil、Width_Coil、Height_blocker、Height_core、gap

## Modeling Principles Learned

- Readiness: `modeling_principles_ready`

### core_sequence

- 先定义全局参数和单位，再建立几何与选择集。
- 随后配置材料、物理场接口、边界条件、网格、研究/求解器和结果导出。
- 自动建模时必须保持 COMSOL 模型树顺序一致，避免先创建依赖后创建上游对象。
- 本案例已提取 18 个参数，可作为约束 JSON 和参数扫描变量。
- 几何证据显示模型可以从脚本中的 geom/feature 序列恢复。

### physics_reasoning

- 物理场接口来自 MATLAB/Java/摘要中的 physics.create 证据，应作为自动建模的主约束。
- 识别到物理场证据：Solid Mechanics
- 识别到物理场证据：Magnetic Fields
- 识别到物理场证据：Global ODEs and DAEs
- 边界条件和选择集需要复核边界编号；自动生成代码时应标注人工确认点。
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
- Transfer recognized physics interfaces to similar requirements: Solid Mechanics, Magnetic Fields, Global ODEs and DAEs.
- Reuse geometry construction patterns when new requirements share shape, import, array, sweep, or boolean operations.
- Use the learned study types as solver starting points: Stationary, Time Dependent.

### extension_questions

- Which parameters control geometry size, material response, boundary loading, and solver stability?
- Which output quantities can be converted into CSV columns for surrogate-model training?
- Can the same physics be tested under steady, transient, eigenfrequency, or parametric-sweep studies?
- How do the theory keywords change governing equations, assumptions, or validation targets: 电磁, 结构力学, 流体?
- Can COMSOL/LiveLink export a model-tree summary from the MPH file to verify selections and boundary IDs?

### new_model_directions

- Extend to load-case comparison, stress concentration analysis, and displacement safety checks.
- Build a corrected model workflow that separates geometry repair, material assignment, constraints, and load verification.
- Extend to inlet/outlet sensitivity, pressure-drop prediction, and flow-uniformity analysis.
- Add coupled transport, porous media, or nonisothermal flow when concentration or temperature fields are involved.
- Extend to terminal-current, resistance, field-distribution, and Joule-loss studies.
- Use electric-current outputs as coupling sources for thermal or structural models.

### parameter_sweep_ideas

- Sweep `R_p` around the learned value `5[mm]` and export target outputs to CSV.
- Sweep `Len_p` around the learned value `48[mm]` and export target outputs to CSV.
- Sweep `z0_p` around the learned value `20[mm]` and export target outputs to CSV.
- Sweep `Tip_R_p` around the learned value `3[mm]` and export target outputs to CSV.
- Sweep `Cut_angle` around the learned value `43[deg]` and export target outputs to CSV.
- Sweep `Guider_width` around the learned value `1.5[mm]` and export target outputs to CSV.
- Sweep `Thickness_core` around the learned value `4[mm]` and export target outputs to CSV.
- Sweep `Height_Coil` around the learned value `40[mm]` and export target outputs to CSV.
- Sweep load, Young's modulus, thickness, fixed constraints, and contact/fracture parameters.
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

- PPT 演示文稿用于补充案例目标、关键假设、结果图说明和结论。
- MATLAB 和 Java 文件是 COMSOL 模型树的可执行证据，应驱动自动建模脚本生成。
- MPH 文件需要通过 COMSOL with MATLAB 导出摘要后，才能可靠使用内部模型设置。
- 参数文本和脚本证据可转换为约束和参数扫描变量。
- 已从案例内容中抽取到模型树证据，可用于学习几何、物理场、材料、网格、研究和结果设置。
- 未发现训练 CSV，因此数值代理模型训练前需要先导出 COMSOL 参数扫描数据。

## Learning Summary After This Case

- Summary: 已学习 electromagnetic_plunger_with_stopper 的 5 个文件；训练阶段=modeling_logic_learning_ready；参数数量=18；内容证据=34 条。
- Training readiness: modeling_logic_ready_but_needs_comsol_sweep_csv
- Reusable confidence: medium

### 学到的建模逻辑

- Case files were treated as one COMSOL evidence package: documentation, scripts, binary model files, parameters, and data.
- The model tree should be reconstructed in this order: parameters, geometry, selections, materials, physics, mesh, study, results, and exports.
- MATLAB/Java scripts provide reusable COMSOL API call patterns for automated model construction.
- MPH files are remembered as authoritative model artifacts, but detailed internal settings require COMSOL/LiveLink extraction.
- 检测到的参数可用于生成约束 JSON，后续也可作为代理模型训练的扫描变量。
- 已完成内容级读取：从案例文件中抽取了参数、几何、物理场、材料、网格、研究、结果和边界条件等模型树证据。

### Reusable Assets

- 18 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Original MPH files for later COMSOL-side verification.
- 34 条内容级模型树证据。

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 5 个案例文件；MATLAB=1，Java=1，PDF=0，MPH=1，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 内容级模型树抽取**
  - Evidence: 抽取到模型树证据 34 条；几何=7，物理场=3，材料=0，网格=0，研究=2，结果=0。
  - Judgement: 模型已读取案例内容并抽取 COMSOL 模型树结构，可用于后续自动建模和代码生成。
- **3. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：electromagnetic_plunger_with_stopper.m, electromagnetic_plunger_with_stopper.java
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **4. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 18 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **5. 理论与模型来源判断**
  - Evidence: PDF 文档=0，MPH 模型=1。
  - Judgement: MPH 是权威模型文件，但缺少 PDF 时理论背景和验证目标需要从脚本、文件名或后续人工说明补充。
- **6. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **7. 记忆库补充**
  - Evidence: 案例标题为 electromagnetic_plunger_with_stopper，训练阶段为 modeling_logic_learning_ready。
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

- `R_p`
- `Len_p`
- `z0_p`
- `Tip_R_p`
- `Cut_angle`
- `Guider_width`
- `Thickness_core`
- `Height_Coil`
- `Width_Coil`
- `Height_blocker`
- `Height_core`
- `gap`
- `dt`
- `tau`
- `I0`
- `k`
- `N_turn`
- `Dia_wire`

### Candidate Outputs

- `max_von_mises_stress`
- `max_displacement`

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

- `electromagnetic_plunger_with_stopper.mph` (comsol_mph, 97093671 bytes)
- `electromagnetic_plunger_with_stopper.m` (matlab_livelink, 55058 bytes)
- `electromagnetic_plunger_with_stopper.java` (comsol_java, 49960 bytes)
- `electromagnetic_plunger_with_stopper_summary.json` (json, 2133 bytes)
- `electromagnetic_plunger_with_stopper_63.pptx` (presentation_document, 16536709 bytes)
