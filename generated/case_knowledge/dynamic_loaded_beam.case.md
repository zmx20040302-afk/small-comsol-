# dynamic_loaded_beam

- Case directory: `D:\桌面\codex\案例下载\COMSOL\承受动载荷的梁`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-06-29T03:10:03.855255+00:00`

## File Summary

- count: 8
- kinds: {'pdf_document': 2, 'comsol_java': 1, 'matlab_livelink': 1, 'comsol_mph': 2, 'text': 2}
- matlab_files: 1
- java_files: 1
- pdf_files: 2
- mph_files: 2
- csv_files: 0
- json_files: 0

## Extracted Parameters

- `SpanWidth` = `10[m]` - Width of one span
- `NumSpans` = `8` - Number of spans
- `TotLength` = `SpanWidth*NumSpans` - Total length of beam
- `BeamHeight` = `0.3[m]` - Beam height
- `LoadIntensity` = `0.1[MPa]` - Intensity of the pressure load
- `PulseWidth` = `2[m]` - Width of load pulse
- `PulseSpacing` = `20[m]` - Distance between load pulses
- `LoadSpeed` = `20[m/s]` - Velocity of the load pulse
- `Tstep1` = `1/(50*f0)` - Time step limit based on natural frequency
- `Tstep2` = `PulseWidth/LoadSpeed/2` - Time step limit based on load velocity
- `Tstep` = `min(Tstep1,Tstep2)` - Maximum time step
- `Tend` = `TotLength/LoadSpeed` - Time when first load pulse reaches beam end
- `ElemPerSpan` = `max(ceil(SpanWidth/PulseWidth*2),20)` - Number of elements along a span
- `CriticalSpeed` = `f0*2*SpanWidth` - Estimated critical speed
- `f0` = `sqrt(25e9[Pa]*BeamHeight^2/(12*2300[kg/m^3]*SpanWidth^4))*pi/2` - Estimate of first natural frequency

## Thoughts

- PDF documents should be used to understand the case purpose, modeling sequence, assumptions, and validation targets.
- MATLAB and Java files are executable evidence for the COMSOL model tree and should drive automated script generation.
- MPH files should be summarized through COMSOL with MATLAB before relying on internal model settings.
- Parameter text/script evidence can be converted into constraints and sweep variables.
- No training CSV was found, so numerical surrogate training requires a COMSOL parametric sweep export first.

## Learning Summary After This Case

- Summary: Learned 8 files for dynamic_loaded_beam; stage=modeling_logic_learning_ready; parameters=15.
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

- 15 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Theory and workflow evidence from PDF documents.
- Original MPH files for later COMSOL-side verification.

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 8 个案例文件；MATLAB=1，Java=1，PDF=2，MPH=2，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：traveling_load.java, traveling_load.m
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **3. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 15 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **4. 理论与模型来源判断**
  - Evidence: PDF 文档=2，MPH 模型=2。
  - Judgement: PDF 用于补充理论、假设和教程目标；MPH 作为权威模型文件，后续应通过 COMSOL/LiveLink 提取内部设置。
- **5. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **6. 记忆库补充**
  - Evidence: 案例标题为 dynamic_loaded_beam，训练阶段为 modeling_logic_learning_ready。
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

- `使用 Microsoft® Azure 运行 COMSOL® 软件` score=0.1229; fields=topic only; parameters=0
- `通过 Amazon EC2™ 运行 COMSOL® 软件` score=0.1081; fields=topic only; parameters=0
- `热执行器代理模型 App` score=0.0924; fields=physics, geometry, materials, boundary_conditions, mesh, solver, results; parameters=42

### Official Documentation Checks

- `COMSOL_ReferenceManual.pdf` page 1591; module=COMSOL_Multiphysics; score=0.1476
- `COMSOL_ReferenceManual.pdf` page 1597; module=COMSOL_Multiphysics; score=0.1419
- `COMSOL_ReferenceManual.pdf` page 1915; module=COMSOL_Multiphysics; score=0.1419

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

- `models.mph.traveling_load.pdf` (pdf_document, 392879 bytes)
- `models.mph.traveling_load.zh_CN.pdf` (pdf_document, 1050270 bytes)
- `traveling_load.java` (comsol_java, 20373 bytes)
- `traveling_load.m` (matlab_livelink, 23413 bytes)
- `traveling_load.mph` (comsol_mph, 65450946 bytes)
- `traveling_load.zh_CN.mph` (comsol_mph, 65491057 bytes)
- `traveling_load_parameters.txt` (text, 815 bytes)
- `traveling_load_parameters.zh_CN.txt` (text, 719 bytes)
