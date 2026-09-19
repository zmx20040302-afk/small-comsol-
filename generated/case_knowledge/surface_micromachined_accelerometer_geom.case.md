# surface_micromachined_accelerometer_geom

- Case directory: `D:\桌面\codex\案例下载\电气\表面微机械加速度计`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-08-22T04:45:27.915296+00:00`

## File Summary

- count: 6
- kinds: {'comsol_mph': 1, 'matlab_livelink': 1, 'comsol_java': 1, 'json': 1, 'pdf_document': 2}
- matlab_files: 1
- java_files: 1
- pdf_files: 2
- pptx_files: 0
- mph_files: 1
- csv_files: 0
- json_files: 1

## Extracted Parameters

- `acceleration` = `0` - Acceleration (g)
- `VtestL` = `0[V]` - Test voltage, left side
- `VtestR` = `0[V]` - Test voltage, right side
- `tSi` = `2[um]` - Silicon thickness
- `tOx` = `1.6[um]` - Oxide thickness
- `l_PM` = `448[um]` - Proof mass length
- `w_PM` = `100[um]` - Proof mass width
- `n_st` = `3` - Number of self test fingers
- `n_f` = `21` - Number of sense fingers
- `w_f` = `4[um]` - Finger width
- `l_f` = `114[um]` - Finger length
- `g_f` = `1[um]` - Finger gap
- `g_st` = `3[um]` - Self test finger gap
- `x_st` = `3[um]+1*(w_f+g_st)` - Self test finger starting position
- `x_f` = `(l_PM-(n_f-1)*3*(w_f+g_f)-w_f)/2` - Sense finger starting position
- `w_eh` = `4[um]` - Etch hole size
- `p_eh` = `18[um]` - Etch hole period
- `l_sp` = `280[um]` - Spring length
- `w_sp` = `2[um]` - Spring width
- `g_sp` = `1[um]` - Spring gap
- `w_sp_conn` = `4[um]` - Spring connection width
- `l_anch_base` = `17[um]` - Anchor base length
- `w_anch_base` = `17[um]` - Anchor base width
- `r_anch` = `3[um]` - Anchor radius
- `x_anch` = `12[um]` - Anchor position
- `l_e_s` = `120[um]` - Short electrode length
- `l_e_l` = `140[um]` - Long electrode length
- `l_p` = `16[um]` - Pad length
- `w_p` = `8[um]` - Pad width
- `r_an` = `3[um]` - Electrode anchor radius
- `l_ovrlp` = `104[um]` - Finger overlap length
- `l_spAssm` = `l_anch_base+2*(w_f+w_sp)+3*g_sp` - Spring assembly length
- `l_polySi` = `l_PM+2*l_spAssm` - Total length
- `hw_polySi` = `w_PM/2+l_f+l_p+l_e_l-l_ovrlp` - Total half width

## 内容级读取结果

- 模型树证据数量: 34
- 理论关键词: 电磁, 流体, 结构力学
- physics: Solid Mechanics, Electrostatics
- mesh: mesh1
- studies: Stationary

### 文件内容证据

- `surface_micromachined_accelerometer_geom.java`: 参数=20, 几何=0, 物理场=0, 研究=0, 结果=0
- `surface_micromachined_accelerometer_geom.m`: 参数=8, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.mems.surface_micromachined_accelerometer.pdf`: 参数=0, 几何=0, 物理场=2, 研究=1, 结果=0
- `surface_micromachined_accelerometer_geom_summary.json`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `surface_micromachined_accelerometer_geom.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.mems.surface_micromachined_accelerometer_geom.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0

## 每个 PDF 文件的简单总结

- `models.mems.surface_micromachined_accelerometer.pdf`: models.mems.surface_micromachined_accelerometer.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果，主要物理场线索为 Solid Mechanics、Electrostatics，研究类型线索为 Stationary；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；using the Electromechanics interface. The example is based on the case study in Ref. 1. The
- `models.mems.surface_micromachined_accelerometer_geom.pdf`: models.mems.surface_micromachined_accelerometer_geom.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；Geometry

## PDF Summary and Physics Judgement

- Simple summary: surface_micromachined_accelerometer_geom 主要研究流动速度、压力或输运过程，PDF 用来说明问题目标、基本假设和求解对象；从核心内容看，建模时应优先选择 Solid Mechanics，并采用 Stationary 研究。
- Primary physics: `Solid Mechanics`
- Study type: `Stationary`
- Judgement rule: 若 PDF 的核心量和方程关键词指向 Solid Mechanics，并且脚本/文本中出现同类接口，就把它作为主物理场；研究类型可由 Stationary 确认。

### Judgement Evidence

- PDF: Model created in COMSOL Multiphysics 6.4
- PDF: using the Electromechanics interface. The example is based on the case study in Ref. 1. The
- PDF: model also demonstrates the use of linked subsequences. A collection of geometric
- PDF: of the geometry for faster computation. The three geometric building blocks are the proof
- 脚本/文本识别到的物理场: Solid Mechanics, Electrostatics
- 识别到的研究类型: Stationary
- 理论关键词: 电磁, 流体, 结构力学

## PDF Keywords to Geometry/Parameter/MATLAB Mapping

- Summary: 将 PDF 关键词、案例建模内容和 MATLAB/Java API 证据整理为可复用的几何与参数建模知识。
- PDF keywords: 电磁, 流体, 结构力学, models.mems.surface_micromachined_accelerometer.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果，主要物理场线索为 Solid Mechanics、Electrostatics，研究类型线索为 Stationary；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；using the Electromechanics interface. The example is based on the case study in Ref. 1. The, models.mems.surface_micromachined_accelerometer_geom.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：Model created in COMSOL Multiphysics 6.4；Geometry
- `acceleration` -> Acceleration (g); MATLAB: `model.param.set('acceleration', value, description)`
- `VtestL` -> Test voltage, left side; MATLAB: `model.param.set('VtestL', value, description)`
- `VtestR` -> Test voltage, right side; MATLAB: `model.param.set('VtestR', value, description)`
- `tSi` -> Silicon thickness; MATLAB: `model.param.set('tSi', value, description)`
- `tOx` -> Oxide thickness; MATLAB: `model.param.set('tOx', value, description)`
- `l_PM` -> Proof mass length; MATLAB: `model.param.set('l_PM', value, description)`
- `w_PM` -> Proof mass width; MATLAB: `model.param.set('w_PM', value, description)`
- `n_st` -> Number of self test fingers; MATLAB: `model.param.set('n_st', value, description)`
- `n_f` -> Number of sense fingers; MATLAB: `model.param.set('n_f', value, description)`
- `w_f` -> Finger width; MATLAB: `model.param.set('w_f', value, description)`
- `l_f` -> Finger length; MATLAB: `model.param.set('l_f', value, description)`
- `g_f` -> Finger gap; MATLAB: `model.param.set('g_f', value, description)`

### Geometry and Parameter Checks

- 先根据 PDF 关键词判断几何对象、控制变量和输出量，再用 MATLAB/Java 模型树证据确认。
- 全局参数应优先来自 model.param.set、inputParam 或案例参数表，缺失时用待确认占位参数。
- 几何应先参数化，再创建命名选择集，避免后续边界条件依赖不稳定的实体编号。
- MATLAB 建模应按 parameter -> geom.create/feature -> selection -> physics.create -> mesh -> study 的顺序生成。
- 已识别物理场证据：Solid Mechanics；Electrostatics
- 已识别参数：acceleration、VtestL、VtestR、tSi、tOx、l_PM、w_PM、n_st、n_f、w_f、l_f、g_f

## Modeling Principles Learned

- Readiness: `modeling_principles_ready`

### core_sequence

- 先定义全局参数和单位，再建立几何与选择集。
- 随后配置材料、物理场接口、边界条件、网格、研究/求解器和结果导出。
- 自动建模时必须保持 COMSOL 模型树顺序一致，避免先创建依赖后创建上游对象。
- 本案例已提取 34 个参数，可作为约束 JSON 和参数扫描变量。

### physics_reasoning

- 物理场接口来自 MATLAB/Java/摘要中的 physics.create 证据，应作为自动建模的主约束。
- 识别到物理场证据：Solid Mechanics
- 识别到物理场证据：Electrostatics
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
- Transfer recognized physics interfaces to similar requirements: Solid Mechanics, Electrostatics.
- Use the learned study types as solver starting points: Stationary.

### extension_questions

- Which parameters control geometry size, material response, boundary loading, and solver stability?
- Which output quantities can be converted into CSV columns for surrogate-model training?
- Can the same physics be tested under steady, transient, eigenfrequency, or parametric-sweep studies?
- How do the theory keywords change governing equations, assumptions, or validation targets: 电磁, 流体, 结构力学?
- Can COMSOL/LiveLink export a model-tree summary from the MPH file to verify selections and boundary IDs?

### new_model_directions

- Extend to load-case comparison, stress concentration analysis, and displacement safety checks.
- Build a corrected model workflow that separates geometry repair, material assignment, constraints, and load verification.
- Extend to inlet/outlet sensitivity, pressure-drop prediction, and flow-uniformity analysis.
- Add coupled transport, porous media, or nonisothermal flow when concentration or temperature fields are involved.

### parameter_sweep_ideas

- Sweep `acceleration` around the learned value `0` and export target outputs to CSV.
- Sweep `VtestL` around the learned value `0[V]` and export target outputs to CSV.
- Sweep `VtestR` around the learned value `0[V]` and export target outputs to CSV.
- Sweep `tSi` around the learned value `2[um]` and export target outputs to CSV.
- Sweep `tOx` around the learned value `1.6[um]` and export target outputs to CSV.
- Sweep `l_PM` around the learned value `448[um]` and export target outputs to CSV.
- Sweep `w_PM` around the learned value `100[um]` and export target outputs to CSV.
- Sweep `n_st` around the learned value `3` and export target outputs to CSV.
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

- PDF 文档用于理解案例目的、建模顺序、理论假设和验证目标。
- MATLAB 和 Java 文件是 COMSOL 模型树的可执行证据，应驱动自动建模脚本生成。
- MPH 文件需要通过 COMSOL with MATLAB 导出摘要后，才能可靠使用内部模型设置。
- 参数文本和脚本证据可转换为约束和参数扫描变量。
- 已从案例内容中抽取到模型树证据，可用于学习几何、物理场、材料、网格、研究和结果设置。
- 未发现训练 CSV，因此数值代理模型训练前需要先导出 COMSOL 参数扫描数据。

## Learning Summary After This Case

- Summary: 已学习 surface_micromachined_accelerometer_geom 的 6 个文件；训练阶段=modeling_logic_learning_ready；参数数量=34；内容证据=34 条。
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

- 34 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Theory and workflow evidence from PDF documents.
- Original MPH files for later COMSOL-side verification.
- 34 条内容级模型树证据。

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 6 个案例文件；MATLAB=1，Java=1，PDF=2，MPH=1，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 内容级模型树抽取**
  - Evidence: 抽取到模型树证据 34 条；几何=0，物理场=2，材料=0，网格=1，研究=1，结果=0。
  - Judgement: 模型已读取案例内容并抽取 COMSOL 模型树结构，可用于后续自动建模和代码生成。
- **3. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：surface_micromachined_accelerometer_geom.m, surface_micromachined_accelerometer_geom.java
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **4. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 34 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **5. 理论与模型来源判断**
  - Evidence: PDF 文档=2，MPH 模型=1。
  - Judgement: PDF 用于补充理论、假设和教程目标；MPH 作为权威模型文件，后续应通过 COMSOL/LiveLink 提取内部设置。
- **6. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **7. 记忆库补充**
  - Evidence: 案例标题为 surface_micromachined_accelerometer_geom，训练阶段为 modeling_logic_learning_ready。
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

- `acceleration`
- `VtestL`
- `VtestR`
- `tSi`
- `tOx`
- `l_PM`
- `w_PM`
- `n_st`
- `n_f`
- `w_f`
- `l_f`
- `g_f`
- `g_st`
- `x_st`
- `x_f`
- `w_eh`
- `p_eh`
- `l_sp`
- `w_sp`
- `g_sp`
- `w_sp_conn`
- `l_anch_base`
- `w_anch_base`
- `r_anch`
- `x_anch`
- `l_e_s`
- `l_e_l`
- `l_p`
- `w_p`
- `r_an`

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

- `surface_micromachined_accelerometer_geom.mph` (comsol_mph, 9773810 bytes)
- `surface_micromachined_accelerometer_geom.m` (matlab_livelink, 32093 bytes)
- `surface_micromachined_accelerometer_geom.java` (comsol_java, 31229 bytes)
- `surface_micromachined_accelerometer_geom_summary.json` (json, 1725 bytes)
- `models.mems.surface_micromachined_accelerometer.pdf` (pdf_document, 909176 bytes)
- `models.mems.surface_micromachined_accelerometer_geom.pdf` (pdf_document, 105463 bytes)
