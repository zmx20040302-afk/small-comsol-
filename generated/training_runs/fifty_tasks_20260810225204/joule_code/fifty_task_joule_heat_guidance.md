# COMSOL 建模代码与理论指导

- 需求: 二维焦耳热耦合模型
- MATLAB 输出: `D:\桌面\codex\comsol1\comsol_training_small_model\generated\training_runs\fifty_tasks_20260810225204\joule_code\fifty_task_joule_heat.m`
- Java 输出: `D:\桌面\codex\comsol1\comsol_training_small_model\generated\training_runs\fifty_tasks_20260810225204\joule_code\FiftyTaskJouleHeat.java`

## 理论与建模指导

- 建模顺序应保持为：参数 -> 几何 -> 选择集 -> 材料 -> 物理场 -> 边界/初始条件 -> 网格 -> 研究/求解 -> 结果导出。
- 生成代码中的边界编号和选择集必须在 COMSOL 中复核；学习库只能提供案例模式和 API 结构，不能替代几何实体编号确认。
- 几何模型与参数指导：几何与参数应优先按“传热几何与参数”组织。 先按几何厚度选择 2D 或 3D；薄板可用 2D，实体散热优先 3D
- 几何要点：矩形/块体热传导域；热源区域；冷却或对流边界；温度监测点或输出边界。
- 关键参数建议：L=9[cm]（母线板焦耳热基准模型）；rad_1=6[mm]（母线板焦耳热基准模型）；tbb=5[mm]（母线板焦耳热基准模型）；wbb=5[cm]（母线板焦耳热基准模型）；mh=3[mm]（母线板焦耳热基准模型）；htc=5[W/m^2/K]（母线板焦耳热基准模型）；Vtot=20[mV]（母线板焦耳热基准模型）；sigma=5.8e7[S/m]（电导率）。
- 选择集与扫描建议：选择集=命名热源域；命名固定温度边界；命名对流边界；命名输出点/面；扫描变量=Q0、hconv、L、W。
- 材料与物性参数指导：材料与物性参数应优先按“传热材料 + 电学材料”配置。
- 必填物性：密度(rho, kg/m^3)；导热系数(k, W/(m*K))；比热容(Cp, J/(kg*K))；电导率(sigma, S/m)。
- 物性变化关系：导热系数、比热和密度可随温度变化；复合材料导热系数可能随方向变化。；电导率常随温度变化；频域问题中介电常数和损耗因子可能随频率变化。。
- 边界条件与初始条件指导：按当前需求，边界条件应优先按“传热”来判断。
- 建议边界：固定温度/给定温度；热通量或热源；绝热/对称；对流换热；表面对表面或环境辐射。
- 建议初始条件：初始温度；初始热源状态；环境温度。
- 物理场复合场检查：该需求应按复合场判断，优先考虑：电-热耦合 / 焦耳热 + 热-结构耦合 / 热应力 + 非等温流动。 主物理场=Electric Currents；耦合物理场=Heat Transfer in Solids、Solid Mechanics、Heat Transfer in Fluids；多物理场节点=Joule Heating / Electromagnetic Heating、Thermal Expansion、Nonisothermal Flow。
- 传热模型需要确认热源、温度边界、热通量或对流换热条件，并检查材料的导热系数、密度和热容。
- 电流/电磁模型需要确认端子、电势、接地和绝缘边界；若与传热耦合，应把焦耳热或损耗项传递到热场。
- 结构力学模型需要确认固定约束、载荷、接触/对称条件和材料弹性参数；特征频率问题应使用 Eigenfrequency 研究。
- 已学习案例中的理论关键词包括：传热，电磁，电流守恒，焦耳热，能量守恒，多孔介质/裂隙，热传导，热膨胀，热应力。
- 本次生成优先参考以下已学习案例：母线板焦耳热基准模型，已验证：一维电热焦耳热模板，微执行器焦耳热 - 分布式参数版本，母线板装配的焦耳热，已验证：二维热应力矩形模板。

## 已学习案例证据

- `母线板焦耳热基准模型`: 内容证据 27 条；物理场=ec / ConductiveMedia, ht / HeatTransfer, Heat Transfer, Electric Currents
- `已验证：一维电热焦耳热模板`: 内容证据 0 条；物理场=ConductiveMedia, HeatTransfer
- `微执行器焦耳热 - 分布式参数版本`: 内容证据 19 条；物理场=ec / ConductiveMedia, ht / HeatTransfer, Heat Transfer
- `母线板装配的焦耳热`: 内容证据 71 条；物理场=ec / ConductiveMedia, ht / HeatTransfer, Heat Transfer, Electric Currents
- `已验证：二维热应力矩形模板`: 内容证据 0 条；物理场=HeatTransfer, SolidMechanics, ThermalExpansion

## 现有内容检查

- 未提供现有内容，本次按新建模型模板处理。

## 调整和完善建议

- 未提供现有脚本或模型摘要；本次输出为基于学习库的新建模型模板，可作为后续修正基线。
- 补充参数定义，并把关键尺寸、材料参数和载荷写成可扫描参数。
- 补充或替换几何构建段，优先复用相似案例中的几何序列。
- 补充物理场接口，并与需求和已学习案例中的物理场保持一致。
- 补充材料节点，至少包含密度、弹性参数、导热或电学参数等必要属性。
- 补充网格设置，并在孔、裂纹、边界层或高梯度区域局部加密。
- 补充研究/求解器设置，按稳态、瞬态、频域、特征频率或参数扫描选择。
- 补充结果导出，保存关键全局量、场图和用于训练的 CSV。
- 补充选择集或边界编号复核步骤，避免边界条件施加到错误实体。
- 根据需求和学习库，应补充或复核 `HeatTransfer` 物理接口。
- 可参考 `母线板焦耳热基准模型` 中的物理场设置：ec / ConductiveMedia, ht / HeatTransfer, Heat Transfer, Electric Currents。
- 可参考 `母线板焦耳热基准模型` 中的研究设置：std1 / stat / Stationary, std1, Stationary。

## 后续验证路径

- 在 COMSOL 中打开生成脚本，先不批量扫描，只运行一个基准模型。
- 核对所有选择集、边界编号和材料参数。
- 求解通过后，再添加参数扫描并导出 CSV。
- 把修正后的 MATLAB/Java 脚本重新放回案例库，继续学习和完善记忆库。
