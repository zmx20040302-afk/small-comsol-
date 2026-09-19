# magnetic_gear_2d

- Case directory: `D:\桌面\codex\案例下载\电气\磁齿轮二维模型`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-08-16T10:35:21.709648+00:00`

## File Summary

- count: 4
- kinds: {'comsol_mph': 1, 'matlab_livelink': 1, 'comsol_java': 1, 'json': 1}
- matlab_files: 1
- java_files: 1
- pdf_files: 0
- pptx_files: 0
- mph_files: 1
- csv_files: 0
- json_files: 1

## Extracted Parameters

- `f0_ir` = `500[rpm]*2*pi[rad]` - Frequency of inner rotor
- `f0_or` = `200[rpm]*2*pi[rad]` - Frequency of outer rotor
- `L` = `100[mm]` - Length of rotors
- `Br` = `1.40[T]` - Remanent flux density of magnets
- `A_ir` = `2[mm]` - Airgap in inner rotor
- `A_or` = `2[mm]` - Airgap in outer rotor
- `A_ext` = `15[mm]` - Airgap exterior to outer rotor
- `SR_ir` = `5[mm]` - Shaft radius of inner rotor
- `IT_ir` = `13[mm]` - Iron thickness of inner rotor
- `IT_or` = `9[mm]` - Iron thickness of outer rotor
- `MT_ir` = `6[mm]` - Magnet thickness of inner rotor
- `MT_or` = `6[mm]` - Magnet thickness of outer rotor
- `T_sp` = `15[mm]` - Thickness of stationary poles
- `OR_ir` = `SR_ir+IT_ir+MT_ir` - Outer radius of inner rotor
- `IR_sp` = `OR_ir+A_ir` - Inner radius of stationary poles
- `OR_sp` = `IR_sp+T_sp` - Outer radius of stationary poles
- `IR_or` = `OR_sp+A_or` - Inner radius of outer rotor
- `OR_or` = `IR_or+MT_or+IT_or` - Outer radius of outer rotor

## 内容级读取结果

- 模型树证据数量: 32
- 理论关键词: 电磁
- geometry: c1 / Circle, c2 / Circle, c3 / Circle, c4 / Circle, geom1 / c1 / r, geom1 / c2 / r, geom1 / c3 / r, geom1 / c3 / angle
- mesh: mesh1
- studies: Stationary
- boundary_conditions: c1 / r, c2 / r, c3 / r, c3 / angle

### 文件内容证据

- `magnetic_gear_2d.java`: 参数=18, 几何=8, 物理场=0, 研究=1, 结果=0
- `magnetic_gear_2d.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `magnetic_gear_2d.m`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `magnetic_gear_2d_summary.json`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0

## PDF Summary and Physics Judgement

- Simple summary: magnetic_gear_2d 的 PDF 可用于理解案例目的、假设和操作步骤；当前证据还不足以唯一确定物理场，后续应结合 MATLAB/Java 中的 physics.create 或 COMSOL 模型树再确认。
- Primary physics: `needs_more_evidence`
- Study type: `Stationary`
- Judgement rule: 先根据 PDF 的核心物理量提出候选物理场，再用 MATLAB/Java/MPH 摘要中的 physics.create 做最终确认。

### Judgement Evidence

- 识别到的研究类型: Stationary
- 理论关键词: 电磁

## PDF Keywords to Geometry/Parameter/MATLAB Mapping

- Summary: 将 PDF 关键词、案例建模内容和 MATLAB/Java API 证据整理为可复用的几何与参数建模知识。
- PDF keywords: 电磁
- `f0_ir` -> Frequency of inner rotor; MATLAB: `model.param.set('f0_ir', value, description)`
- `f0_or` -> Frequency of outer rotor; MATLAB: `model.param.set('f0_or', value, description)`
- `L` -> Length of rotors; MATLAB: `model.param.set('L', value, description)`
- `Br` -> Remanent flux density of magnets; MATLAB: `model.param.set('Br', value, description)`
- `A_ir` -> Airgap in inner rotor; MATLAB: `model.param.set('A_ir', value, description)`
- `A_or` -> Airgap in outer rotor; MATLAB: `model.param.set('A_or', value, description)`
- `A_ext` -> Airgap exterior to outer rotor; MATLAB: `model.param.set('A_ext', value, description)`
- `SR_ir` -> Shaft radius of inner rotor; MATLAB: `model.param.set('SR_ir', value, description)`
- `IT_ir` -> Iron thickness of inner rotor; MATLAB: `model.param.set('IT_ir', value, description)`
- `IT_or` -> Iron thickness of outer rotor; MATLAB: `model.param.set('IT_or', value, description)`
- `MT_ir` -> Magnet thickness of inner rotor; MATLAB: `model.param.set('MT_ir', value, description)`
- `MT_or` -> Magnet thickness of outer rotor; MATLAB: `model.param.set('MT_or', value, description)`

### Geometry and Parameter Checks

- 先根据 PDF 关键词判断几何对象、控制变量和输出量，再用 MATLAB/Java 模型树证据确认。
- 全局参数应优先来自 model.param.set、inputParam 或案例参数表，缺失时用待确认占位参数。
- 几何应先参数化，再创建命名选择集，避免后续边界条件依赖不稳定的实体编号。
- MATLAB 建模应按 parameter -> geom.create/feature -> selection -> physics.create -> mesh -> study 的顺序生成。
- 已识别几何证据：c1 / Circle；c2 / Circle；c3 / Circle；c4 / Circle；geom1 / c1 / r；geom1 / c2 / r
- 已识别参数：f0_ir、f0_or、L、Br、A_ir、A_or、A_ext、SR_ir、IT_ir、IT_or、MT_ir、MT_or

## Modeling Principles Learned

- Readiness: `modeling_principles_ready`

### core_sequence

- 先定义全局参数和单位，再建立几何与选择集。
- 随后配置材料、物理场接口、边界条件、网格、研究/求解器和结果导出。
- 自动建模时必须保持 COMSOL 模型树顺序一致，避免先创建依赖后创建上游对象。
- 本案例已提取 18 个参数，可作为约束 JSON 和参数扫描变量。
- 几何证据显示模型可以从脚本中的 geom/feature 序列恢复。

### physics_reasoning

- 边界条件和选择集需要复核边界编号；自动生成代码时应标注人工确认点。
- 理论关键词可用于判断控制方程、变量含义和验证目标。

### automation_evidence

- MATLAB/Java 文件可直接提供 COMSOL API 调用顺序，是自动建模最可靠的文本证据。
- MPH 文件被视为权威模型来源；若存在同名 MATLAB/Java/JSON 摘要，系统会读取这些旁路证据。
- 网格节点已识别，后续应将网格尺寸或网格序列写入可复用模板。

### verification_logic

- 生成模型后先运行基准算例，再做网格无关性和参数扫描。
- 若需要训练代理模型，必须导出包含输入参数和目标输出的 CSV。
- 训练后用未参与训练的 COMSOL 结果复核 RMSE、MAE、R2 和物理趋势。

## Thinking and Extension

- Readiness: `ready_for_reasoning_and_extension`

### transferable_knowledge

- Reuse the learned COMSOL order: parameters -> geometry -> selections -> materials -> physics -> mesh -> study -> results.
- Treat extracted parameters as future constraint variables and parametric sweep inputs.
- Reuse geometry construction patterns when new requirements share shape, import, array, sweep, or boolean operations.
- Use the learned study types as solver starting points: Stationary.

### extension_questions

- Which parameters control geometry size, material response, boundary loading, and solver stability?
- Which output quantities can be converted into CSV columns for surrogate-model training?
- Can the same physics be tested under steady, transient, eigenfrequency, or parametric-sweep studies?
- How do the theory keywords change governing equations, assumptions, or validation targets: 电磁?
- Can COMSOL/LiveLink export a model-tree summary from the MPH file to verify selections and boundary IDs?

### new_model_directions

- Create a similar baseline model, then add one controlled extension at a time: geometry, material, boundary condition, study type, or output target.

### parameter_sweep_ideas

- Sweep `f0_ir` around the learned value `500[rpm]*2*pi[rad]` and export target outputs to CSV.
- Sweep `f0_or` around the learned value `200[rpm]*2*pi[rad]` and export target outputs to CSV.
- Sweep `L` around the learned value `100[mm]` and export target outputs to CSV.
- Sweep `Br` around the learned value `1.40[T]` and export target outputs to CSV.
- Sweep `A_ir` around the learned value `2[mm]` and export target outputs to CSV.
- Sweep `A_or` around the learned value `2[mm]` and export target outputs to CSV.
- Sweep `A_ext` around the learned value `15[mm]` and export target outputs to CSV.
- Sweep `SR_ir` around the learned value `5[mm]` and export target outputs to CSV.
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

- MATLAB 和 Java 文件是 COMSOL 模型树的可执行证据，应驱动自动建模脚本生成。
- MPH 文件需要通过 COMSOL with MATLAB 导出摘要后，才能可靠使用内部模型设置。
- 参数文本和脚本证据可转换为约束和参数扫描变量。
- 已从案例内容中抽取到模型树证据，可用于学习几何、物理场、材料、网格、研究和结果设置。
- 未发现训练 CSV，因此数值代理模型训练前需要先导出 COMSOL 参数扫描数据。

## Learning Summary After This Case

- Summary: 已学习 magnetic_gear_2d 的 4 个文件；训练阶段=modeling_logic_learning_ready；参数数量=18；内容证据=32 条。
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
- 32 条内容级模型树证据。

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 4 个案例文件；MATLAB=1，Java=1，PDF=0，MPH=1，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 内容级模型树抽取**
  - Evidence: 抽取到模型树证据 32 条；几何=8，物理场=0，材料=0，网格=1，研究=1，结果=0。
  - Judgement: 模型已读取案例内容并抽取 COMSOL 模型树结构，可用于后续自动建模和代码生成。
- **3. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：magnetic_gear_2d.m, magnetic_gear_2d.java
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
  - Evidence: 案例标题为 magnetic_gear_2d，训练阶段为 modeling_logic_learning_ready。
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

- `f0_ir`
- `f0_or`
- `L`
- `Br`
- `A_ir`
- `A_or`
- `A_ext`
- `SR_ir`
- `IT_ir`
- `IT_or`
- `MT_ir`
- `MT_or`
- `T_sp`
- `OR_ir`
- `IR_sp`
- `OR_sp`
- `IR_or`
- `OR_or`

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

- `magnetic_gear_2d.mph` (comsol_mph, 80531304 bytes)
- `magnetic_gear_2d.m` (matlab_livelink, 61111 bytes)
- `magnetic_gear_2d.java` (comsol_java, 59839 bytes)
- `magnetic_gear_2d_summary.json` (json, 1424 bytes)
