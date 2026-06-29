# 管式反应器代理模型 App

- Case directory: `D:\桌面\codex\案例下载\COMSOL\管式反应器代理模型 App`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-06-29T08:48:57.428048+00:00`

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

- 模型树证据数量: 36
- 理论关键词: 传热, 流体
- geometry: r1 / Rectangle, geom1 / r1 / size
- physics: tds / DilutedSpecies, ht / HeatTransferInFluids, cb / CoefficientFormBoundaryPDE
- mesh: mesh1
- studies: std1 / stat / Stationary, std1
- boundary_conditions: r1 / size

### 文件内容证据

- `tubular_reactor_surrogate.java`: 参数=20, 几何=2, 物理场=3, 研究=2, 结果=0
- `tubular_reactor_surrogate.m`: 参数=20, 几何=2, 物理场=3, 研究=1, 结果=0
- `applications.tubular_reactor_surrogate.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `applications.tubular_reactor_surrogate.zh_CN.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.mph.tubular_reactor_surrogate.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `models.mph.tubular_reactor_surrogate.zh_CN.pdf`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `tubular_reactor_surrogate.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0
- `tubular_reactor_surrogate.zh_CN.mph`: 参数=0, 几何=0, 物理场=0, 研究=0, 结果=0

## Thoughts

- PDF 文档用于理解案例目的、建模顺序、理论假设和验证目标。
- MATLAB 和 Java 文件是 COMSOL 模型树的可执行证据，应驱动自动建模脚本生成。
- MPH 文件需要通过 COMSOL with MATLAB 导出摘要后，才能可靠使用内部模型设置。
- 参数文本和脚本证据可转换为约束和参数扫描变量。
- 已从案例内容中抽取到模型树证据，可用于学习几何、物理场、材料、网格、研究和结果设置。
- 未发现训练 CSV，因此数值代理模型训练前需要先导出 COMSOL 参数扫描数据。

## Learning Summary After This Case

- Summary: 已学习 管式反应器代理模型 App 的 8 个文件；训练阶段=modeling_logic_learning_ready；参数数量=26；内容证据=36 条。
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
- 36 条内容级模型树证据。

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 8 个案例文件；MATLAB=1，Java=1，PDF=4，MPH=2，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 内容级模型树抽取**
  - Evidence: 抽取到模型树证据 36 条；几何=2，物理场=3，材料=0，网格=1，研究=2，结果=0。
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
