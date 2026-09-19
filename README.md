# COMSOL 小型训练模型与自动建模工作台

这个目录提供一个本地可运行的小系统，用于：

- 阅读 COMSOL LiveLink for MATLAB 脚本 `.m`，提取参数、物理场、研究和结果设置。
- 用 JSON 描述建模限制和约束，生成新的 COMSOL LiveLink MATLAB 建模脚本。
- 读取 COMSOL 参数扫描导出的 CSV，训练一个小型代理模型，用输入参数预测仿真结果。
- 通过 MATLAB 辅助脚本读取 `.mph` 模型摘要。完整读取 `.mph` 需要 COMSOL + LiveLink/API。
- 通过本地网页或者 Windows 批处理脚本打开一个可操作界面。

## 快速启动网页

双击：

```text
start_windows.bat
```

启动脚本会启动网页和本地执行队列，并打开 `http://127.0.0.1:8880/`。网页可访问与 COMSOL 连接是两个独立状态：即使 `mphserver` 尚未启动，案例阅读、知识库检索和已验证代理模型预测仍可使用；只有执行真实 COMSOL 求解或参数扫描时才需要检查并启动许可证可用的 `mphserver`。

启动器在初始化较慢时可能显示 `ready=pending`，这表示后台服务仍在启动而非失败。稍候直接访问上述地址即可；只有服务进程提前退出时才会显示启动错误。

启动器会读取 `configs/execution_node.json`，先检查 `localhost:2036`，并在端口不可达时按配置启动 `comsolmphserver.exe`。启动日志写入 `generated/training_runs`；执行 Worker 还会写入 `generated/execution_jobs/worker_startup.log`。如果 2036 已被其他 COMSOL 进程占用，系统会复用该连接，不会重复启动服务器。

已验证代理模型只能在各自模型卡声明的几何、材料、边界条件和输入范围内作快速比较。超出范围时，网页会拒绝外推并要求补充真实 COMSOL 参数扫描。

已验证的本地模板包括一维传热、扩散、电热、二维固体力学与二维热应力；模板执行结果会保存为独立的 MPH 文件，并写入案例记忆库供后续中文建模需求检索。

候选案例评分和 CSV 扫描规划只会把已明确支持的单物理场，以及明确的电流-传热组合列为自动扫描候选。磁场、静电、粒子追踪、半导体、等离子体和其他复杂耦合案例必须先声明具体输出表达式并人工复核，不能根据案例名称猜测训练列。

任务中心中的“匹配已验证模板”可根据中英文需求优先选择可靠模板、提示必要参数，并自动进入 COMSOL 执行队列。

或者在 PowerShell 中运行：

```powershell
cd D:\桌面\codex\comsol1\comsol_training_small_model
python web_app.py --open
```

默认地址：

```text
http://127.0.0.1:8765
```

## 局域网联网运行

如果希望同一局域网内的其他电脑访问这个小模型，双击：

```text
start_network.bat
```

或手动运行：

```powershell
cd D:\桌面\codex\comsol1\comsol_training_small_model
python web_app.py --host 0.0.0.0 --port 8765
```

启动后终端会打印可访问地址，例如：

```text
http://192.168.x.x:8765
```

其他设备需要和本机处于同一局域网，并在浏览器中访问这个地址。如果 Windows 防火墙提示，请只允许 Python 在“专用网络/Private network”中通信。

安全提醒：联网模式会把文件读取、脚本生成、模型训练接口暴露给局域网，请只在可信网络中使用。公网访问需要额外认证、反向代理和防火墙配置，不建议直接暴露。

网页中可以完成：

- 使用类似 Codex 的对话界面输入需求，系统会在消息流中返回反馈。
- 输入自然语言指令，获得建模、约束、读取或训练建议。
- 输入文件路径阅读文件，或在浏览器中选择文件读取文本内容。
- 读取 MATLAB `.m` 建模文件。
- 载入和修改约束 JSON。
- 校验约束是否满足模板要求。
- 生成 COMSOL LiveLink `.m` 建模脚本。
- 在安装训练依赖后训练本地代理模型。

## 语言指令与文件阅读

网页左侧的“语言指令”区域可以输入类似：

```text
请读取这个 MATLAB 文件，判断是否能作为 COMSOL 自动建模模板。
```

```text
根据这个 CSV 训练一个代理模型，用 k Q h L 预测 Tmax Tavg。
```

```text
读取 mph 文件并说明如何转成可训练数据。
```

“文件输入”区域支持两种方式：

- 填写一个或多个本地路径；多个路径时每行一个，也可以用英文分号 `;` 分隔。
- 点击“选择文件”，直接从浏览器选择 `.m`、`.csv`、`.json`、`.txt` 等文本文件；支持一次多选。

支持的读取反馈：

- `.m`：识别 COMSOL LiveLink 参数、物理场、研究类型和结果图组。
- `.java`：识别 COMSOL Java 导出代码中的参数、物理场、研究、结果、网格和材料线索。
- `.pdf`：识别 COMSOL 对应说明文档；安装依赖后，路径读取和浏览器二进制上传都会提取最多 50 页、约 5 万字符用于学习摘要。
- `.csv`：识别列名、行数和样例行，可用于训练代理模型。
- `.json`：识别 JSON 是否有效和顶层键，可作为约束配置或模型摘要。
- `.mph`：提示使用 COMSOL with MATLAB 的 `export_mph_summary.m` 导出摘要。

同时读取多个文件时，系统会生成一个文件集合摘要，统计 MATLAB、CSV、JSON、MPH 等文件数量，并把集合摘要带入对话反馈。例如可以同时读取：

```text
../acoustic_rectangular_cavity/build_acoustic_rectangular_cavity.m
examples/sample_comsol_data.csv
configs/thermal_constraints.json
```

点击“学习总结”后，系统会把 `.mph`、`.pdf`、`.m`、`.java`、`.csv`、`.json` 按用途分组：

- COMSOL 模型文件
- MATLAB 建模脚本
- Java 导出代码
- PDF 学习文档
- CSV 训练数据
- JSON 约束或元数据

并给出推荐实现路径：提取物理场、参数、几何、边界条件、网格、求解器和输出结果，然后校验约束、生成 LiveLink 脚本、运行 COMSOL 参数扫描、训练代理模型。

学习总结默认会写入 `generated/case_memory/case_memory.json`，并记录质量分与缺失证据。案例检索会优先使用物理场、几何、边界和来源证据更完整的条目。

分步工作流在退回某一步时会按审批意见重新生成该步方案并保留修订历史；完成审批后会输出 MATLAB、Java、理论指导和代码验证报告。验证报告中的 `ready_to_solve=false` 表示仍需在 COMSOL 中核对选择集或物理参数，不能把脚手架当成已求解模型。

新版页面布局：

- 左侧：会话入口和当前工作状态。
- 中间：对话消息流和底部输入框。
- 右侧：文件、MATLAB、约束、训练和原始响应工具区。

## 安装训练依赖

网页的 MATLAB 读取、约束校验、脚本生成不需要额外依赖。训练模型需要：

```powershell
cd D:\桌面\codex\comsol1\comsol_training_small_model
pip install -r requirements.txt
```

`scikit-learn` 用于小模型训练；没有 GPU 也可以运行。

## 命令行用法

### 0. 扫描 COMSOL 官方 PDF 文档并生成知识底座

如果本机安装了 COMSOL 官方 PDF 文档，可以扫描：

```powershell
python -m src.comsol_small_model.cli scan-comsol-docs --root D:\COMSOL64\Multiphysics\doc\pdf --output-dir generated
```

会生成：

```text
generated/comsol_pdf_catalog.json
generated/comsol_modeling_logic.md
```

其中：

- `comsol_pdf_catalog.json`：记录模块目录、PDF 文件、文档角色、模块领域归类。
- `comsol_modeling_logic.md`：总结 COMSOL 建模底层逻辑，包括问题定义、几何、材料、物理场、边界条件、网格、研究求解、结果验证、代理模型训练。

这两个文件是小模型理解 COMSOL 的底层知识底座。它们不会一次全文解析所有 PDF，而是先建立模块目录、文档角色和建模逻辑框架；需要深入某个模块时，再读取对应 PDF 内容。

### 0.1. 总结一个 COMSOL 案例并补充到案例知识库

```powershell
python -m src.comsol_small_model.cli summarize-case "D:\桌面\codex\案例下载\COMSOL\母线板装配几何系列教程" --title busbar_assembly_geometry --output-dir generated\case_knowledge
```

会生成：

```text
generated/case_knowledge/busbar_assembly_geometry.case.json
generated/case_knowledge/busbar_assembly_geometry.case.md
generated/case_knowledge/case_knowledge_index.json
```

案例卡片会记录：

- 文件组成：PDF、MATLAB、Java、MPH、CSV、JSON、TXT
- 训练阶段判断：是否已有 CSV，是否可开始代理模型训练
- 提取到的参数、默认值、单位和说明
- 对案例的建模思考
- 缺口：例如缺少参数扫描 CSV、MPH 需要 LiveLink 摘要
- 实现路径：从案例阅读到约束、脚本、参数扫描和训练

### 1. 阅读 MATLAB 建模文件

```powershell
python -m src.comsol_small_model.cli inspect-matlab ..\acoustic_rectangular_cavity\build_acoustic_rectangular_cavity.m
```

输出包括：

- `model.param.set(...)` 参数
- `physics.create(...)` 物理场接口
- `study(...).create(...)` 研究类型
- `result.create(...)` 结果图组

### 2. 校验建模约束

```powershell
python -m src.comsol_small_model.cli validate configs\thermal_constraints.json
```

约束文件描述：

- 几何尺寸范围
- 材料参数范围
- 边界条件范围
- 网格尺寸范围
- 扫描参数范围
- 输出结果表达式

### 3. 根据约束生成 COMSOL LiveLink 脚本

```powershell
python -m src.comsol_small_model.cli generate-matlab configs\thermal_constraints.json generated_build_thermal.m
```

生成的 `.m` 文件需要在 COMSOL with MATLAB 环境中运行。

### 4. 训练小型代理模型

```powershell
python -m src.comsol_small_model.cli train examples\sample_comsol_data.csv model.joblib --inputs k Q h L --outputs Tmax Tavg
```

模型会保存为 `model.joblib`，并输出训练误差和测试误差。

训练器当前使用 `scikit-learn` 的 `MLPRegressor`，流程是：

```text
读取 CSV
检查输入/输出列
检查 NaN/inf
划分训练集和测试集
标准化输入 X
标准化输出 y
训练 MLP
反标准化预测结果
输出 RMSE、MAE、R2 和警告
保存 joblib 模型
```

性能注意点：

- 示例数据只有 15 行，只适合验证流程，不适合得到可靠工程模型。
- 小数据会自动使用较小网络 `(32, 32)`，避免过度复杂。
- 100 行以上数据会使用更大的默认网络 `(64, 64)`。
- 50 行以上启用 early stopping，减少过拟合。
- 如果输出不标准化，MLP 对 300K 量级温度会收敛很差；当前版本已经同时标准化 X 和 y。
- 如果报告中出现 `Dataset has only ... rows`，说明需要更多 COMSOL 参数扫描数据。

### 5. 用模型预测

```powershell
python -m src.comsol_small_model.cli predict model.joblib --inputs 16 80 35 0.045
```

### 6. 独立 COMSOL 留出集与模型发布门槛

网页“训练”区域中的“独立 COMSOL 验证训练”用于通用物理场数据集。它要求提供两份互不重叠的 CSV：训练扫描数据和未参与训练的新 COMSOL 留出集；再填写物理适用范围与最大相对误差阈值。

系统会用留出集选择候选代理模型，生成验证报告和模型卡，并登记到 `generated/surrogate_registry.json`：

- `validated_for_declared_scope`：独立 COMSOL 留出集满足用户填写的阈值，只能在模型卡声明的物理范围内快速比较。
- `needs_more_comsol_evidence`：未通过阈值、输出存在零值或证据不足，必须补充 COMSOL 数据或改用绝对误差判据。

该状态不是实验验证、规范认证或最终工程放行。几何、材料、边界、研究类型或输入范围发生变化时，仍须回到 COMSOL 重新求解。

通过状态的模型可在网页“查看已验证模型”中获取模型 ID，并使用“受控代理预测”输入与模型输入列一致的 JSON 对象。系统会再次检查注册状态和训练范围；未通过验证、缺少输入或输入越界时不会输出代理结果。

对已验证模型的越界输入，可使用“生成补充 COMSOL 工况”。它会写入 `generated/augmentation_plans`，给出需要由同一物理范围 COMSOL 模板求解的补充样本；补样后仍须使用新的、未参与重训的 COMSOL 留出集重新验证。

### 7. 审计已注册代理模型

每次新增、重训或迁移代理模型包后，运行统一的运行时审计：

```powershell
python scripts\audit_registered_surrogate_runtime.py --simulate-relocation
```

审计会检查注册表中的模型、模型卡和独立验证报告是否存在，只对 `validated_for_declared_scope` 模型执行范围中点预测，并核对预测输出列。`--simulate-relocation` 还会在临时目录中模拟原绝对路径和训练 CSV 失效，验证复制后的模型包能否离线使用。报告写入：

```text
generated/models/surrogate_runtime_audit.json
```

命令退出码为 `0` 表示所有已验证模型均可预测、验证证据完整且迁移模拟通过。报告同时保存注册表 SHA-256 指纹；健康接口 `/api/health` 的 `surrogate_runtime` 字段会读取最近一次报告，不会在每次页面刷新时重新加载全部模型。注册表在审计后发生变化时，接口会返回 `state=stale`，直到重新运行审计。

`NumPy 2.5` 与 `joblib 1.5.x` 组合会在读取数组时产生重复的 `DeprecationWarning`。运行时只精确过滤这条已知的 joblib shape 提示，审计则在 `compatibility_notices` 中保留环境风险；其他模型与 sklearn 警告仍会正常记录。新部署环境通过 `requirements.txt` 使用 `NumPy <2.5`，当前环境可继续运行，无须改写已验证模型。

当后续已验证模型明确替代早期训练尝试时，应保留旧模型的原验证状态和证据，并登记模型谱系：

```powershell
python scripts\mark_surrogates_superseded.py <replacement_id> <old_model_id> --reason "替代依据"
python scripts\audit_registered_surrogate_runtime.py --simulate-relocation
```

替代模型必须已经通过独立 COMSOL 验证。该操作不会删除旧模型；闭环审计会把它归入历史替代模型，不再算作活动证据缺口。

正式注册表统一为 `generated/models/surrogate_registry.json`。旧版本创建的 `generated/surrogate_registry.json` 仅作为只读兼容来源；新训练不会再写入旧路径。如果旧注册表包含正式注册表没有或内容冲突的模型，`/api/health` 会返回 `surrogate_runtime.state=registry_split`，需要先核对并合并，不能让旧副本覆盖正式记录。

可先执行安全预检，再合并 legacy 独有且无冲突的条目：

```powershell
python scripts\consolidate_surrogate_registries.py --dry-run
python scripts\consolidate_surrogate_registries.py
python scripts\audit_registered_surrogate_runtime.py --simulate-relocation
```

同 ID 内容不一致时，合并命令会返回非零退出码且不修改正式注册表。网页完成一次独立 COMSOL 验证训练并注册模型后，会自动重新执行带迁移模拟的运行时审计，健康状态无需人工刷新报告。

## 读取 `.mph` 的现实限制

`.mph` 是 COMSOL 专有模型文件。Python 可以做文件级记录，但不能可靠还原完整模型树。要读取 `.mph` 的参数、组件、物理场和研究，推荐在 COMSOL with MATLAB 中运行：

```matlab
summary = export_mph_summary('your_model.mph', 'your_model_summary.json');
```

脚本位置：

```text
matlab/export_mph_summary.m
```

## Portable Reference Workchains

Saved physics-reference reports can be passed to other local tools without the web UI. A package copies the selected reports into its own `reports/` folder and writes a relative-path `manifest.json`.

```powershell
python -m src.comsol_small_model.cli list-reference-reports --output-dir generated\reference_reports
python -m src.comsol_small_model.cli package-reference-reports generated\reference_reports\reference_example.json --output-dir generated\workchain_packages --title pipe-validation
python -m src.comsol_small_model.cli validate-workchain generated\workchain_packages\workchain_<id>\manifest.json
python -m src.comsol_small_model.cli archive-workchain generated\workchain_packages\workchain_<id>\manifest.json --output-dir generated\workchain_archives
python -m src.comsol_small_model.cli validate-workchain-archive generated\workchain_archives\workchain_<id>.zip
```

Package validation checks file presence, report schemas, and report IDs. It validates traceability only; it does not certify a COMSOL model or engineering result.

这条路线最稳：Python 负责网页、训练、约束和自动化组织；COMSOL/MATLAB 负责真正创建、读取和求解模型。
