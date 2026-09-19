# COMSOL 建模代码与理论指导

- 需求: 二维煤层单孔水力压裂建模
- MATLAB 输出: `D:\桌面\codex\comsol1\comsol_training_small_model\generated\training_runs\twenty_tasks_20260810195111\generated_code\twenty_task_hydraulic_fracture.m`
- Java 输出: `D:\桌面\codex\comsol1\comsol_training_small_model\generated\training_runs\twenty_tasks_20260810195111\generated_code\TwentyTaskHydraulicFracture.java`

## 理论与建模指导

- 建模顺序应保持为：参数 -> 几何 -> 选择集 -> 材料 -> 物理场 -> 边界/初始条件 -> 网格 -> 研究/求解 -> 结果导出。
- 生成代码中的边界编号和选择集必须在 COMSOL 中复核；学习库只能提供案例模式和 API 结构，不能替代几何实体编号确认。
- 几何模型与参数指导：几何与参数应优先按“水力压裂单孔/裂隙几何”组织。 2D 平面应变优先；需要厚度效应或三维钻孔时再升为 3D
- 几何要点：矩形或正方形煤/岩体代表试验工作面或局部煤层；中心或指定位置圆形钻孔；可选预制裂缝、弱面或自然裂隙线；外边界用于施加地应力、围压或位移约束。
- 关键参数建议：square_side=300[mm]（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）；borehole_diameter=15[mm]（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）；stress_ratio_range=1.5~2.0（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）；initial_pressure=0.1[MPa]（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）；mean_elastic_modulus=35.1[GPa]（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）；mean_compressive_strength=152[MPa]（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）；principal_stress_direction_135=135[deg]（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）；principal_stress_direction_180=180[deg]（COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究）。
- 选择集与扫描建议：选择集=命名钻孔边界；命名外边界四边；命名裂缝/弱面边界；命名煤岩基体域；扫描变量=pinj、sigH、sigh、k_perm、rb。
- 材料与物性参数指导：材料与物性参数应优先按“结构力学材料 + 传热材料”配置。 Recognized material: Water.
- 必填物性：密度(rho, kg/m^3)；弹性模量(E, Pa)；泊松比(nu, 1)；导热系数(k, W/(m*K))；比热容(Cp, J/(kg*K))。
- 物性变化关系：弹性模量和强度可为空间随机场；复合材料或层状材料需要方向相关弹性矩阵。；导热系数、比热和密度可随温度变化；复合材料导热系数可能随方向变化。。
- 边界条件与初始条件指导：按当前需求，边界条件应优先按“水力压裂/孔压-应力耦合”来判断。
- 建议边界：外边界原位地应力、围压或位移约束；钻孔内壁注入压力或流量；煤层/岩体渗透率、孔隙率和初始孔隙压力；裂缝面压力、泄漏或损伤/相场边界。
- 建议初始条件：初始孔隙压力；初始地应力；初始位移为零或原位平衡状态；初始裂缝/损伤变量。
- 物理场复合场检查：该需求应按复合场判断，优先考虑：孔压-应力-裂缝耦合。 主物理场=Solid Mechanics；耦合物理场=Darcy's Law / Porous Media Flow、Fracture Flow、Phase Field or Cohesive Zone；多物理场节点=Poroelasticity、Fracture flow-stress coupling。
- 传热模型需要确认热源、温度边界、热通量或对流换热条件，并检查材料的导热系数、密度和热容。
- 结构力学模型需要确认固定约束、载荷、接触/对称条件和材料弹性参数；特征频率问题应使用 Eigenfrequency 研究。
- 已学习案例中的理论关键词包括：文章围绕煤层超高，压水力压裂数值模，研究不同地应力条，主应力方向，煤层非均匀性和天，然裂缝对单孔裂纹，起裂压力，扩展方向，损伤演化和裂缝长，度的影响，热传导，热膨胀。
- 本次生成优先参考以下已学习案例：COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究，已验证：二维热应力矩形模板，已验证：二维传热参数化与代理训练模板，已验证：二维固体力学矩形受载模板，热烧蚀除料建模6.2。

## 已学习案例证据

- `COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究`: 内容证据 0 条；物理场=solid mechanics damage evolution, pore/fluid pressure loading, hydraulic fracture propagation
- `已验证：二维热应力矩形模板`: 内容证据 0 条；物理场=HeatTransfer, SolidMechanics, ThermalExpansion
- `已验证：二维传热参数化与代理训练模板`: 内容证据 0 条；物理场=HeatTransfer
- `已验证：二维固体力学矩形受载模板`: 内容证据 0 条；物理场=SolidMechanics
- `热烧蚀除料建模6.2`: 内容证据 65 条；物理场=ht / HeatTransfer, dg / DeformedGeometry

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
- 根据需求和学习库，应补充或复核 `GeneralFormPDE` 物理接口。
- 可参考 `COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究` 中的物理场设置：solid mechanics damage evolution, pore/fluid pressure loading, hydraulic fracture propagation。
- 可参考 `COMSOL不同围压条件下单孔水力压裂裂纹的拓展规律研究` 中的研究设置：time-dependent pressure/damage evolution, parametric sweep over stress ratio and stress direction。

## 后续验证路径

- 在 COMSOL 中打开生成脚本，先不批量扫描，只运行一个基准模型。
- 核对所有选择集、边界编号和材料参数。
- 求解通过后，再添加参数扫描并导出 CSV。
- 把修正后的 MATLAB/Java 脚本重新放回案例库，继续学习和完善记忆库。
