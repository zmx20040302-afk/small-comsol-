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
- `.pdf`：识别 COMSOL 对应说明文档；如果本机安装 `pypdf` 或 `pdfplumber`，会提取前几页文本用于学习摘要。
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

## 读取 `.mph` 的现实限制

`.mph` 是 COMSOL 专有模型文件。Python 可以做文件级记录，但不能可靠还原完整模型树。要读取 `.mph` 的参数、组件、物理场和研究，推荐在 COMSOL with MATLAB 中运行：

```matlab
summary = export_mph_summary('your_model.mph', 'your_model_summary.json');
```

脚本位置：

```text
matlab/export_mph_summary.m
```

这条路线最稳：Python 负责网页、训练、约束和自动化组织；COMSOL/MATLAB 负责真正创建、读取和求解模型。
