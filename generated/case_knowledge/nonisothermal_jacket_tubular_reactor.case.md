# nonisothermal_jacket_tubular_reactor

- Case directory: `D:\桌面\codex\案例下载\COMSOL\带非等温冷却夹套的管式反应器`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-06-29T03:10:25.055882+00:00`

## File Summary

- count: 13
- kinds: {'pdf_document': 4, 'comsol_java': 1, 'matlab_livelink': 1, 'comsol_mph': 3, 'text': 4}
- matlab_files: 1
- java_files: 1
- pdf_files: 4
- mph_files: 3
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

## Thoughts

- PDF documents should be used to understand the case purpose, modeling sequence, assumptions, and validation targets.
- MATLAB and Java files are executable evidence for the COMSOL model tree and should drive automated script generation.
- MPH files should be summarized through COMSOL with MATLAB before relying on internal model settings.
- Parameter text/script evidence can be converted into constraints and sweep variables.
- No training CSV was found, so numerical surrogate training requires a COMSOL parametric sweep export first.

## Learning Summary After This Case

- Summary: Learned 13 files for nonisothermal_jacket_tubular_reactor; stage=modeling_logic_learning_ready; parameters=26.
- Training readiness: modeling_logic_ready_but_needs_comsol_sweep_csv
- Reusable confidence: high

### Learned Modeling Logic

- Case files were treated as one COMSOL evidence package: documentation, scripts, binary model files, parameters, and data.
- The model tree should be reconstructed in this order: parameters, geometry, selections, materials, physics, mesh, study, results, and exports.
- MATLAB/Java scripts provide reusable COMSOL API call patterns for automated model construction.
- PDF documentation provides modeling purpose, assumptions, theoretical context, and validation targets.
- MPH files are remembered as authoritative model artifacts, but detailed internal settings require COMSOL/LiveLink extraction.
- Detected parameters can seed a constraints JSON and later become sweep variables for surrogate-model training.

### Reusable Assets

- 26 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Theory and workflow evidence from PDF documents.
- Original MPH files for later COMSOL-side verification.

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 13 个案例文件；MATLAB=1，Java=1，PDF=4，MPH=3，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：tubular_reactor.java, tubular_reactor.m
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **3. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 26 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **4. 理论与模型来源判断**
  - Evidence: PDF 文档=4，MPH 模型=3。
  - Judgement: PDF 用于补充理论、假设和教程目标；MPH 作为权威模型文件，后续应通过 COMSOL/LiveLink 提取内部设置。
- **5. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **6. 记忆库补充**
  - Evidence: 案例标题为 nonisothermal_jacket_tubular_reactor，训练阶段为 modeling_logic_learning_ready。
  - Judgement: 该案例的文件摘要、参数、建模逻辑和下一步动作会写入案例知识库，并可被后续自动建模方案检索复用。

### Next Actions

- Read the PDF, MATLAB, Java, MPH, TXT, JSON, and CSV evidence as one case package.
- Extract model purpose, geometry sequence, parameters, selections, and model-tree features.
- Convert detected parameters into a constraints JSON with units and valid ranges.
- Use MATLAB/Java evidence to generate or adapt a LiveLink MATLAB builder.
- Run a COMSOL parametric sweep over selected parameters.
- Export a CSV containing input parameters and target outputs.
- Train the local surrogate model after the CSV exists.
- After the geometry/modeling logic is verified, run COMSOL parameter sweeps and export CSV training data.

## External Knowledge Alignment


### Similar Master Cases

- `管式反应器代理模型 App` score=0.2026; fields=physics, geometry, materials, boundary_conditions, mesh, solver, results, applicability; parameters=86
- `使用 Microsoft® Azure 运行 COMSOL® 软件` score=0.0997; fields=topic only; parameters=0
- `通过 Amazon EC2™ 运行 COMSOL® 软件` score=0.0881; fields=topic only; parameters=0

### Official Documentation Checks

- `COMSOL_ReferenceManual.pdf` page 1597; module=COMSOL_Multiphysics; score=0.1276
- `COMSOL_ReferenceManual.pdf` page 1591; module=COMSOL_Multiphysics; score=0.1274
- `COMSOL_ProgrammingReferenceManual.pdf` page 1196; module=COMSOL_Multiphysics; score=0.1273

### Training Improvements

- 将单案例摘要升级为：本地案例证据 + 总案例库相似案例 + 官方文档校对的三层学习结果。
- 学习完成后先判断证据字段是否覆盖 geometry、materials、physics、boundary_conditions、mesh、solver、results。
- 优先对齐相似案例中已有证据的参数、物理场、网格、求解器和结果导出设置。
- 生成或修改 LiveLink MATLAB/Java API 前，使用官方文档索引核对接口和节点含义。
- 没有 CSV 时只完成建模逻辑学习；需要先完成 COMSOL 参数扫描、导出 CSV，再训练代理模型。

## Implementation Path

- Read the PDF, MATLAB, Java, MPH, TXT, JSON, and CSV evidence as one case package.
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

- `applications.tubular_reactor.pdf` (pdf_document, 446217 bytes)
- `applications.tubular_reactor.zh_CN.pdf` (pdf_document, 2252435 bytes)
- `models.mph.tubular_reactor.pdf` (pdf_document, 475876 bytes)
- `models.mph.tubular_reactor.zh_CN.pdf` (pdf_document, 784185 bytes)
- `tubular_reactor.java` (comsol_java, 19045 bytes)
- `tubular_reactor.m` (matlab_livelink, 24797 bytes)
- `tubular_reactor.mph` (comsol_mph, 5792923 bytes)
- `tubular_reactor.zh_CN (1).mph` (comsol_mph, 9334129 bytes)
- `tubular_reactor.zh_CN.mph` (comsol_mph, 5809961 bytes)
- `tubular_reactor_parameters.txt` (text, 1477 bytes)
- `tubular_reactor_parameters.zh_CN.txt` (text, 1343 bytes)
- `tubular_reactor_variables.txt` (text, 329 bytes)
- `tubular_reactor_variables.zh_CN.txt` (text, 292 bytes)
