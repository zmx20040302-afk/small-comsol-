# bow_tie_laser_cavity

- Case directory: `D:\桌面\codex\案例下载\电气\蝶形激光腔`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-08-22T06:51:59.118137+00:00`

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

- `L1` = `0.1[m]` - Flat mirror half distance
- `L2` = `0.05[m]` - Spherical mirror half distance
- `th` = `10[deg]` - Flat mirror tilt angle
- `dth` = `0.1[deg]` - Initial ray angle from flat mirror normal
- `T0` = `1[us]` - Total computation time
- `dt` = `T0/200` - Time increment
- `D_FM` = `12.5[mm]` - Flat mirror diameter
- `L_FM` = `10[mm]` - Flat mirror thickness
- `X_FM` = `-L1*tan(th)` - Flat mirror X position
- `Y_FM` = `0[m]` - Flat mirror Y position
- `Z_FM` = `-L1` - Flat mirror Z position
- `RX_FM` = `0[deg]` - Flat mirror X rotation
- `RY_FM` = `th` - Flat mirror Y rotation
- `RZ_FM` = `0[deg]` - Flat mirror Z rotation
- `D_SM` = `12.5[mm]` - Spherical mirror diameter
- `L_SM` = `10[mm]` - Spherical mirror thickness
- `R_SM` = `0.5[m]` - Spherical mirror radius of curvature
- `X_SM` = `L2*tan(th)` - Spherical mirror X position
- `Y_SM` = `0[m]` - Spherical mirror Y position
- `Z_SM` = `L2` - Spherical mirror Z position
- `RX_SM` = `0[deg]` - Spherical mirror X rotation
- `RY_SM` = `th/2` - Spherical mirror Y rotation
- `RZ_SM` = `0[deg]` - Spherical mirror Z rotation
- `wl` = `0.78[um]` - Wavelength

## 内容级读取结果

- 模型树证据数量: 26
- 理论关键词: 结构力学, 优化/参数扫描
- physics: Ray Optics
- studies: Parametric Sweep

### 文件内容证据

- `bow_tie_laser_cavity.java`: 参数=20, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.roptics.bow_tie_laser_cavity.pdf`: 参数=0, 几何=0, 物理场=1, 研究=1, 结果=0
- `bow_tie_laser_cavity.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `bow_tie_laser_cavity.m`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `bow_tie_laser_cavity_summary.json`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0

## 每个 PDF 文件的简单总结

- `models.roptics.bow_tie_laser_cavity.pdf`: models.roptics.bow_tie_laser_cavity.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果，主要物理场线索为 Ray Optics，研究类型线索为 Parametric Sweep；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；approximation, or alternatively by geometrical optics simulation.

## PDF Summary and Physics Judgement

- Simple summary: bow_tie_laser_cavity 主要研究模型中的主要物理现象和输出量，PDF 用来说明问题目标、基本假设和求解对象；从核心内容看，建模时应优先选择 Solid Mechanics，并采用 Parametric Sweep 研究。
- Primary physics: `Solid Mechanics`
- Study type: `Parametric Sweep`
- Judgement rule: 若 PDF 的核心量和方程关键词指向 Solid Mechanics，并且脚本/文本中出现同类接口，就把它作为主物理场；研究类型可由 Parametric Sweep 确认。

### Judgement Evidence

- PDF: Model created in COMSOL Multiphysics 6.4
- PDF: approximation, or alternatively by geometrical optics simulation.
- PDF: whereas the time-dependent study terminates earlier if the ray escapes from the cavity. A
- PDF: result with the ABCD matrix theory.
- 脚本/文本识别到的物理场: Ray Optics
- 识别到的研究类型: Parametric Sweep
- 理论关键词: 结构力学, 优化/参数扫描

## PDF Keywords to Geometry/Parameter/MATLAB Mapping

- Summary: 将 PDF 关键词、案例建模内容和 MATLAB/Java API 证据整理为可复用的几何与参数建模知识。
- PDF keywords: 结构力学, 优化/参数扫描, models.roptics.bow_tie_laser_cavity.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果，主要物理场线索为 Ray Optics，研究类型线索为 Parametric Sweep；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；approximation, or alternatively by geometrical optics simulation.
- `L1` -> Flat mirror half distance; MATLAB: `model.param.set('L1', value, description)`
- `L2` -> Spherical mirror half distance; MATLAB: `model.param.set('L2', value, description)`
- `th` -> Flat mirror tilt angle; MATLAB: `model.param.set('th', value, description)`
- `dth` -> Initial ray angle from flat mirror normal; MATLAB: `model.param.set('dth', value, description)`
- `T0` -> Total computation time; MATLAB: `model.param.set('T0', value, description)`
- `dt` -> Time increment; MATLAB: `model.param.set('dt', value, description)`
- `D_FM` -> Flat mirror diameter; MATLAB: `model.param.set('D_FM', value, description)`
- `L_FM` -> Flat mirror thickness; MATLAB: `model.param.set('L_FM', value, description)`
- `X_FM` -> Flat mirror X position; MATLAB: `model.param.set('X_FM', value, description)`
- `Y_FM` -> Flat mirror Y position; MATLAB: `model.param.set('Y_FM', value, description)`
- `Z_FM` -> Flat mirror Z position; MATLAB: `model.param.set('Z_FM', value, description)`
- `RX_FM` -> Flat mirror X rotation; MATLAB: `model.param.set('RX_FM', value, description)`

### Geometry and Parameter Checks

- 先根据 PDF 关键词判断几何对象、控制变量和输出量，再用 MATLAB/Java 模型树证据确认。
- 全局参数应优先来自 model.param.set、inputParam 或案例参数表，缺失时用待确认占位参数。
- 几何应先参数化，再创建命名选择集，避免后续边界条件依赖不稳定的实体编号。
- MATLAB 建模应按 parameter -> geom.create/feature -> selection -> physics.create -> mesh -> study 的顺序生成。
- 已识别物理场证据：Ray Optics
- 已识别参数：L1、L2、th、dth、T0、dt、D_FM、L_FM、X_FM、Y_FM、Z_FM、RX_FM

## Modeling Principles Learned

- Readiness: `modeling_principles_ready`

### core_sequence

- 先定义全局参数和单位，再建立几何与选择集。
- 随后配置材料、物理场接口、边界条件、网格、研究/求解器和结果导出。
- 自动建模时必须保持 COMSOL 模型树顺序一致，避免先创建依赖后创建上游对象。
- 本案例已提取 24 个参数，可作为约束 JSON 和参数扫描变量。

### physics_reasoning

- 物理场接口来自 MATLAB/Java/摘要中的 physics.create 证据，应作为自动建模的主约束。
- 识别到物理场证据：Ray Optics
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
- Transfer recognized physics interfaces to similar requirements: Ray Optics.
- Use the learned study types as solver starting points: Parametric Sweep.

### extension_questions

- Which parameters control geometry size, material response, boundary loading, and solver stability?
- Which output quantities can be converted into CSV columns for surrogate-model training?
- Can the same physics be tested under steady, transient, eigenfrequency, or parametric-sweep studies?
- How do the theory keywords change governing equations, assumptions, or validation targets: 结构力学, 优化/参数扫描?
- Can COMSOL/LiveLink export a model-tree summary from the MPH file to verify selections and boundary IDs?

### new_model_directions

- Extend to load-case comparison, stress concentration analysis, and displacement safety checks.
- Build a corrected model workflow that separates geometry repair, material assignment, constraints, and load verification.

### parameter_sweep_ideas

- Sweep `L1` around the learned value `0.1[m]` and export target outputs to CSV.
- Sweep `L2` around the learned value `0.05[m]` and export target outputs to CSV.
- Sweep `th` around the learned value `10[deg]` and export target outputs to CSV.
- Sweep `dth` around the learned value `0.1[deg]` and export target outputs to CSV.
- Sweep `T0` around the learned value `1[us]` and export target outputs to CSV.
- Sweep `dt` around the learned value `T0/200` and export target outputs to CSV.
- Sweep `D_FM` around the learned value `12.5[mm]` and export target outputs to CSV.
- Sweep `L_FM` around the learned value `10[mm]` and export target outputs to CSV.
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

- Summary: 已学习 bow_tie_laser_cavity 的 5 个文件；训练阶段=modeling_logic_learning_ready；参数数量=24；内容证据=26 条。
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

- 24 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Theory and workflow evidence from PDF documents.
- Original MPH files for later COMSOL-side verification.
- 26 条内容级模型树证据。

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 5 个案例文件；MATLAB=1，Java=1，PDF=1，MPH=1，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 内容级模型树抽取**
  - Evidence: 抽取到模型树证据 26 条；几何=0，物理场=1，材料=0，网格=0，研究=1，结果=0。
  - Judgement: 模型已读取案例内容并抽取 COMSOL 模型树结构，可用于后续自动建模和代码生成。
- **3. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：bow_tie_laser_cavity.m, bow_tie_laser_cavity.java
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **4. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 24 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **5. 理论与模型来源判断**
  - Evidence: PDF 文档=1，MPH 模型=1。
  - Judgement: PDF 用于补充理论、假设和教程目标；MPH 作为权威模型文件，后续应通过 COMSOL/LiveLink 提取内部设置。
- **6. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **7. 记忆库补充**
  - Evidence: 案例标题为 bow_tie_laser_cavity，训练阶段为 modeling_logic_learning_ready。
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

- `L1`
- `L2`
- `th`
- `dth`
- `T0`
- `dt`
- `D_FM`
- `L_FM`
- `X_FM`
- `Y_FM`
- `Z_FM`
- `RX_FM`
- `RY_FM`
- `RZ_FM`
- `D_SM`
- `L_SM`
- `R_SM`
- `X_SM`
- `Y_SM`
- `Z_SM`
- `RX_SM`
- `RY_SM`
- `RZ_SM`
- `wl`

### Candidate Outputs

- `primary_quantity_of_interest`
- `validation_error`

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

- `bow_tie_laser_cavity.mph` (comsol_mph, 175948228 bytes)
- `bow_tie_laser_cavity.m` (matlab_livelink, 22561 bytes)
- `bow_tie_laser_cavity.java` (comsol_java, 17588 bytes)
- `bow_tie_laser_cavity_summary.json` (json, 1577 bytes)
- `models.roptics.bow_tie_laser_cavity.pdf` (pdf_document, 333592 bytes)
