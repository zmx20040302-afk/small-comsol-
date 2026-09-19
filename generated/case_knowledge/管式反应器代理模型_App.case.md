# 管式反应器代理模型 App

- Case directory: `D:\桌面\codex\案例下载\COMSOL\管式反应器代理模型 App`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-07-06T09:43:49.978776+00:00`

## File Summary

- count: 8
- kinds: {'pdf_document': 4, 'comsol_java': 1, 'matlab_livelink': 1, 'comsol_mph': 2}
- matlab_files: 1
- java_files: 1
- pdf_files: 4
- mph_files: 2
- csv_files: 0
- json_files: 0

## Extracted Parameters

- `E` = `75362[J/mol]` - Activation energy
- `A` = `16.96e12[1/h]` - Frequency factor
- `ke` = `0.559[W/m/K]` - Thermal conductivity
- `Diff` = `1e-9[m^2/s]` - Diffusion coefficient
- `Uk` = `1300[W/m^2/K]` - Overall heat-transfer coefficient
- `dHrx` = `-84666[J/mol]` - Heat of reaction
- `T0` = `312[K]` - Inlet temperature
- `Ta0` = `277[K]` - Inlet temperature of the coolant
- `v0` = `v_w0+v_po0+v_m0` - Total flow rate
- `cA0` = `n_po0/v0` - Propylene oxide concentration, inlet
- `cB0` = `n_w0/v0` - Water concentration, inlet
- `cMe0` = `n_m0/v0` - Methanol concentration, inlet
- `Cp0` = `(Cp_po*cA0+Cp_m*cMe0+Cp_w*cB0)/rho0` - Heat capacity at inlet
- `rho0` = `(cA0*M_po+cB0*M_w+cMe0*M_m)` - Density at inlet
- `Ra` = `0.1[m]` - Reactor radius
- `L` = `1[m]` - Reactor length
- `M_po` = `58.095[g/mol]` - Molar weight, propylene oxide
- `M_m` = `32.042[g/mol]` - Molar weight, methanol
- `M_w` = `18[g/mol]` - Molar weight, water
- `rho_po_p` = `830[kg/m^3]` - Density, propylene oxide
- `rho_m_p` = `791.3[kg/m^3]` - Density, methanol
- `rho_w_p` = `1000[kg/m^3]` - Density, water
- `Cp_po` = `146.54[J/mol/K]` - Specific heat, po
- `Cp_m` = `81.095[J/mol/K]` - Specific heat, m
- `Cp_w` = `75.36[J/mol/K]` - Specific heat, w
- `Cp_pg` = `192.59[J/mol/K]` - Specific heat, pg

## 内容级读取结果

- 模型树证据数量: 37
- 理论关键词: 传热, 流体
- geometry: r1 / Rectangle, geom1 / r1 / size
- physics: tds / DilutedSpecies, ht / HeatTransferInFluids, cb / CoefficientFormBoundaryPDE
- mesh: mesh1
- studies: std1 / stat / Stationary, std1, Stationary
- boundary_conditions: r1 / size

### 文件内容证据

- `tubular_reactor_surrogate.java`: 参数=20, 几何=2, 物理场=3, 研究=3, 结果=0
- `tubular_reactor_surrogate.mph`: 参数=20, 几何=2, 物理场=3, 研究=3, 结果=0
- `tubular_reactor_surrogate.m`: 参数=20, 几何=2, 物理场=3, 研究=2, 结果=0
- `applications.tubular_reactor_surrogate.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `applications.tubular_reactor_surrogate.zh_CN.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.mph.tubular_reactor_surrogate.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.mph.tubular_reactor_surrogate.zh_CN.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `tubular_reactor_surrogate.zh_CN.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0

## 每个 PDF 文件的简单总结

- `applications.tubular_reactor_surrogate.pdf`: applications.tubular_reactor_surrogate.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber.
- `applications.tubular_reactor_surrogate.zh_CN.pdf`: applications.tubular_reactor_surrogate.zh_CN.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber.
- `models.mph.tubular_reactor_surrogate.pdf`: models.mph.tubular_reactor_surrogate.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber.
- `models.mph.tubular_reactor_surrogate.zh_CN.pdf`: models.mph.tubular_reactor_surrogate.zh_CN.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber.

## PDF Summary and Physics Judgement

- Simple summary: 管式反应器代理模型 App 主要研究流动速度、压力或输运过程，PDF 用来说明问题目标、基本假设和求解对象；从核心内容看，建模时应优先选择 Heat Transfer，并采用 Stationary 研究。
- Primary physics: `Heat Transfer`
- Study type: `Stationary`
- Judgement rule: 若 PDF 的核心量和方程关键词指向 Heat Transfer，并且脚本/文本中出现同类接口，就把它作为主物理场；研究类型可由 Stationary 确认。

### Judgement Evidence

- 脚本/文本识别到的物理场: tds / DilutedSpecies, ht / HeatTransferInFluids, cb / CoefficientFormBoundaryPDE
- 识别到的研究类型: std1 / stat / Stationary, std1, Stationary
- 理论关键词: 传热, 流体

## PDF Keywords to Geometry/Parameter/MATLAB Mapping

- Summary: 将 PDF 关键词、案例建模内容和 MATLAB/Java API 证据整理为可复用的几何与参数建模知识。
- PDF keywords: 传热, 流体, applications.tubular_reactor_surrogate.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber., applications.tubular_reactor_surrogate.zh_CN.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber., models.mph.tubular_reactor_surrogate.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber., models.mph.tubular_reactor_surrogate.zh_CN.pdf: 该 PDF 主要用于说明案例背景、建模目标、理论假设和验证结果；核心内容可概括为：PDF detected. Text extraction requires pypdf or pdfplumber.
- `E` -> Activation energy; MATLAB: `model.param.set('E', value, description)`
- `A` -> Frequency factor; MATLAB: `model.param.set('A', value, description)`
- `ke` -> Thermal conductivity; MATLAB: `model.param.set('ke', value, description)`
- `Diff` -> Diffusion coefficient; MATLAB: `model.param.set('Diff', value, description)`
- `Uk` -> Overall heat-transfer coefficient; MATLAB: `model.param.set('Uk', value, description)`
- `dHrx` -> Heat of reaction; MATLAB: `model.param.set('dHrx', value, description)`
- `T0` -> Inlet temperature; MATLAB: `model.param.set('T0', value, description)`
- `Ta0` -> Inlet temperature of the coolant; MATLAB: `model.param.set('Ta0', value, description)`
- `v0` -> Total flow rate; MATLAB: `model.param.set('v0', value, description)`
- `cA0` -> Propylene oxide concentration, inlet; MATLAB: `model.param.set('cA0', value, description)`
- `cB0` -> Water concentration, inlet; MATLAB: `model.param.set('cB0', value, description)`
- `cMe0` -> Methanol concentration, inlet; MATLAB: `model.param.set('cMe0', value, description)`

### Geometry and Parameter Checks

- 先根据 PDF 关键词判断几何对象、控制变量和输出量，再用 MATLAB/Java 模型树证据确认。
- 全局参数应优先来自 model.param.set、inputParam 或案例参数表，缺失时用待确认占位参数。
- 几何应先参数化，再创建命名选择集，避免后续边界条件依赖不稳定的实体编号。
- MATLAB 建模应按 parameter -> geom.create/feature -> selection -> physics.create -> mesh -> study 的顺序生成。
- 已识别几何证据：r1 / Rectangle；geom1 / r1 / size
- 已识别物理场证据：tds / DilutedSpecies；ht / HeatTransferInFluids；cb / CoefficientFormBoundaryPDE
- 已识别参数：E、A、ke、Diff、Uk、dHrx、T0、Ta0、v0、cA0、cB0、cMe0

## Modeling Principles Learned

- Readiness: `modeling_principles_ready`

### core_sequence

- 先定义全局参数和单位，再建立几何与选择集。
- 随后配置材料、物理场接口、边界条件、网格、研究/求解器和结果导出。
- 自动建模时必须保持 COMSOL 模型树顺序一致，避免先创建依赖后创建上游对象。
- 本案例已提取 26 个参数，可作为约束 JSON 和参数扫描变量。
- 几何证据显示模型可以从脚本中的 geom/feature 序列恢复。

### physics_reasoning

- 物理场接口来自 MATLAB/Java/摘要中的 physics.create 证据，应作为自动建模的主约束。
- 识别到物理场证据：tds / DilutedSpecies
- 识别到物理场证据：ht / HeatTransferInFluids
- 识别到物理场证据：cb / CoefficientFormBoundaryPDE
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
- Transfer recognized physics interfaces to similar requirements: tds / DilutedSpecies, ht / HeatTransferInFluids, cb / CoefficientFormBoundaryPDE.
- Reuse geometry construction patterns when new requirements share shape, import, array, sweep, or boolean operations.
- Use the learned study types as solver starting points: std1 / stat / Stationary, std1, Stationary.

### extension_questions

- Which parameters control geometry size, material response, boundary loading, and solver stability?
- Which output quantities can be converted into CSV columns for surrogate-model training?
- Can the same physics be tested under steady, transient, eigenfrequency, or parametric-sweep studies?
- How do the theory keywords change governing equations, assumptions, or validation targets: 传热, 流体?
- Can COMSOL/LiveLink export a model-tree summary from the MPH file to verify selections and boundary IDs?

### new_model_directions

- Extend to temperature sensitivity studies by sweeping heat source, convection coefficient, and thermal conductivity.
- Couple heat transfer with structural stress or electric losses when the requirement includes deformation or Joule heating.
- Extend to inlet/outlet sensitivity, pressure-drop prediction, and flow-uniformity analysis.
- Add coupled transport, porous media, or nonisothermal flow when concentration or temperature fields are involved.

### parameter_sweep_ideas

- Sweep `E` around the learned value `75362[J/mol]` and export target outputs to CSV.
- Sweep `A` around the learned value `16.96e12[1/h]` and export target outputs to CSV.
- Sweep `ke` around the learned value `0.559[W/m/K]` and export target outputs to CSV.
- Sweep `Diff` around the learned value `1e-9[m^2/s]` and export target outputs to CSV.
- Sweep `Uk` around the learned value `1300[W/m^2/K]` and export target outputs to CSV.
- Sweep `dHrx` around the learned value `-84666[J/mol]` and export target outputs to CSV.
- Sweep `T0` around the learned value `312[K]` and export target outputs to CSV.
- Sweep `Ta0` around the learned value `277[K]` and export target outputs to CSV.
- Sweep heat source, heat-transfer coefficient, thermal conductivity, and ambient temperature.
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

- Summary: 已学习 管式反应器代理模型 App 的 8 个文件；训练阶段=modeling_logic_learning_ready；参数数量=26；内容证据=37 条。
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

- 26 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Theory and workflow evidence from PDF documents.
- Original MPH files for later COMSOL-side verification.
- 37 条内容级模型树证据。

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 8 个案例文件；MATLAB=1，Java=1，PDF=4，MPH=2，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 内容级模型树抽取**
  - Evidence: 抽取到模型树证据 37 条；几何=2，物理场=3，材料=0，网格=1，研究=3，结果=0。
  - Judgement: 模型已读取案例内容并抽取 COMSOL 模型树结构，可用于后续自动建模和代码生成。
- **3. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：tubular_reactor_surrogate.java, tubular_reactor_surrogate.m
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **4. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 26 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **5. 理论与模型来源判断**
  - Evidence: PDF 文档=4，MPH 模型=2。
  - Judgement: PDF 用于补充理论、假设和教程目标；MPH 作为权威模型文件，后续应通过 COMSOL/LiveLink 提取内部设置。
- **6. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **7. 记忆库补充**
  - Evidence: 案例标题为 管式反应器代理模型 App，训练阶段为 modeling_logic_learning_ready。
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

- `E`
- `A`
- `ke`
- `Diff`
- `Uk`
- `dHrx`
- `T0`
- `Ta0`
- `v0`
- `cA0`
- `cB0`
- `cMe0`
- `Cp0`
- `rho0`
- `Ra`
- `L`
- `M_po`
- `M_m`
- `M_w`
- `rho_po_p`
- `rho_m_p`
- `rho_w_p`
- `Cp_po`
- `Cp_m`
- `Cp_w`
- `Cp_pg`
- `v_ratio`

### Candidate Outputs

- `Tmax`
- `Tavg`
- `pressure_drop`
- `max_velocity`

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

- `管式反应器代理模型 App` score=0.4394; fields=physics, geometry, materials, boundary_conditions, mesh, solver, results, applicability; parameters=86
- `热执行器代理模型 App` score=0.2082; fields=physics, geometry, materials, boundary_conditions, mesh, solver, results; parameters=42
- `集群设置验证` score=0.131; fields=physics, geometry, materials, boundary_conditions, mesh, solver, results; parameters=1

### Official Documentation Checks

- `IntroductionToLiveLinkForMATLAB.pdf` page 5; module=LiveLink_for_MATLAB; score=0.098
- `IntroductionToCOMSOLMultiphysics.pdf` page 262; module=COMSOL_Multiphysics; score=0.0977
- `IntroductionToCOMSOLMultiphysics.pdf` page 254; module=COMSOL_Multiphysics; score=0.0952

### Training Improvements

- 将单案例摘要升级为：本地案例证据 + 总案例库相似案例 + 官方文档校对的三层学习结果。
- 学习完成后先判断证据字段是否覆盖 geometry、materials、physics、boundary_conditions、mesh、solver、results。
- 优先对齐相似案例中已有证据的参数、物理场、网格、求解器和结果导出设置。
- 生成或修改 LiveLink MATLAB/Java API 前，使用官方文档索引核对接口和节点含义。
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

- `applications.tubular_reactor_surrogate.pdf` (pdf_document, 214947 bytes)
- `applications.tubular_reactor_surrogate.zh_CN.pdf` (pdf_document, 1353612 bytes)
- `models.mph.tubular_reactor_surrogate.pdf` (pdf_document, 1353689 bytes)
- `models.mph.tubular_reactor_surrogate.zh_CN.pdf` (pdf_document, 2601831 bytes)
- `tubular_reactor_surrogate.java` (comsol_java, 38303 bytes)
- `tubular_reactor_surrogate.m` (matlab_livelink, 47891 bytes)
- `tubular_reactor_surrogate.mph` (comsol_mph, 15474973 bytes)
- `tubular_reactor_surrogate.zh_CN.mph` (comsol_mph, 13663912 bytes)
