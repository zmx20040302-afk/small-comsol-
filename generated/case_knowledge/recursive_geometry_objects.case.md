# recursive_geometry_objects

- Case directory: `D:\桌面\codex\案例下载\COMSOL\递归和递归定义的几何对象`
- Training stage: `modeling_logic_learning_ready`
- Created at: `2026-06-29T03:10:38.636447+00:00`

## File Summary

- count: 6
- kinds: {'comsol_java': 2, 'matlab_livelink': 2, 'comsol_mph': 2}
- matlab_files: 2
- java_files: 2
- pdf_files: 0
- mph_files: 2
- csv_files: 0
- json_files: 0

## Extracted Parameters

- `mslevel` = `2` - Menger sponge level

## Thoughts

- MATLAB and Java files are executable evidence for the COMSOL model tree and should drive automated script generation.
- MPH files should be summarized through COMSOL with MATLAB before relying on internal model settings.
- Parameter text/script evidence can be converted into constraints and sweep variables.
- No training CSV was found, so numerical surrogate training requires a COMSOL parametric sweep export first.

## Learning Summary After This Case

- Summary: Learned 6 files for recursive_geometry_objects; stage=modeling_logic_learning_ready; parameters=1.
- Training readiness: modeling_logic_ready_but_needs_comsol_sweep_csv
- Reusable confidence: medium

### Learned Modeling Logic

- Case files were treated as one COMSOL evidence package: documentation, scripts, binary model files, parameters, and data.
- The model tree should be reconstructed in this order: parameters, geometry, selections, materials, physics, mesh, study, results, and exports.
- MATLAB/Java scripts provide reusable COMSOL API call patterns for automated model construction.
- MPH files are remembered as authoritative model artifacts, but detailed internal settings require COMSOL/LiveLink extraction.
- Detected parameters can seed a constraints JSON and later become sweep variables for surrogate-model training.

### Reusable Assets

- 1 extracted parameters with values/descriptions.
- LiveLink MATLAB or COMSOL Java script structure.
- Original MPH files for later COMSOL-side verification.

### Learning Process and Evidence

- **1. 文件证据读取**
  - Evidence: 共读取 6 个案例文件；MATLAB=2，Java=2，PDF=0，MPH=2，CSV=0。
  - Judgement: 这些文件被合并为一个 COMSOL 案例证据包，用于同时学习建模流程、参数和训练可行性。
- **2. 建模脚本识别**
  - Evidence: 检测到可复用的 MATLAB/Java 建模脚本：menger_sponge.java, menger_sponge.m, sierpinski_carpet.java, sierpinski_carpet.m
  - Judgement: 脚本中的 COMSOL API 调用可用于恢复模型树顺序，并辅助生成 LiveLink MATLAB 自动建模脚本。
- **3. 参数与约束提取**
  - Evidence: 从文本、MATLAB 或 Java 证据中提取到 1 个参数。
  - Judgement: 这些参数可转成约束 JSON，并作为后续 COMSOL 参数扫描和代理模型训练的输入变量。
- **4. 理论与模型来源判断**
  - Evidence: PDF 文档=0，MPH 模型=2。
  - Judgement: MPH 是权威模型文件，但缺少 PDF 时理论背景和验证目标需要从脚本、文件名或后续人工说明补充。
- **5. 训练阶段判断**
  - Evidence: CSV 训练数据文件数量为 0。
  - Judgement: 当前完成的是建模逻辑学习；还需要运行 COMSOL 参数扫描并导出 CSV，才能进行数值代理模型训练。
- **6. 记忆库补充**
  - Evidence: 案例标题为 recursive_geometry_objects，训练阶段为 modeling_logic_learning_ready。
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

- `使用 Microsoft® Azure 运行 COMSOL® 软件` score=0.1305; fields=topic only; parameters=0
- `通过 Amazon EC2™ 运行 COMSOL® 软件` score=0.1135; fields=topic only; parameters=0
- `热执行器代理模型 App` score=0.0893; fields=physics, geometry, materials, boundary_conditions, mesh, solver, results; parameters=42

### Official Documentation Checks

- `COMSOL_ReferenceManual.pdf` page 1591; module=COMSOL_Multiphysics; score=0.1736
- `COMSOL_ReferenceManual.pdf` page 1597; module=COMSOL_Multiphysics; score=0.1724
- `COMSOL_ProgrammingReferenceManual.pdf` page 1196; module=COMSOL_Multiphysics; score=0.1667

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

- `menger_sponge.java` (comsol_java, 232750 bytes)
- `menger_sponge.m` (matlab_livelink, 204667 bytes)
- `menger_sponge.mph` (comsol_mph, 1007614 bytes)
- `sierpinski_carpet.java` (comsol_java, 1375 bytes)
- `sierpinski_carpet.m` (matlab_livelink, 1918 bytes)
- `sierpinski_carpet.mph` (comsol_mph, 695604 bytes)
