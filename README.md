# Learning for AI

## datasets文件夹

此文件夹上面放置了此项目所用的数据集（会持续更新）



## AI-prepared 文件夹

此文件夹是完成AI项目必需的储备知识，包括Python，NumPy、pandas和docker这些部分



## log文件夹

此文件夹为TensorBoard产生的可视化日志文件



## models文件夹

此文件夹保存的是最佳模型的信息



## nn_demo 文件夹

此文件夹为神经网络（Neural Network）的demo，这里，我在文件中使用了原生的Python/NumPy库，构建一个基本的softmax回归算法和一个简单的两层神经网络，不使用任何的Keras库的算法。更详细的步骤参见此文件夹下的 *任务说明.ipynb* 文件



## yolo_demo 文件夹

一个基于TensorFlow、Keras和Flask的YOLO2的目标检测的Web应用



## RNN_Numpy 文件夹

使用NumPy实现RNN（Recurrent Neural Network）和LSTM（Long Short-Term Memory）网络的前向传播过程，里面有相应的测试代码和公式推导





## CNN_NumPy文件夹

使用NumPy实现CNN（Convolution Nerual Network）中的卷积层和池化层，里面有相应的测试文件以及说明





## 快速问答.txt

机器学习的一些常见问题



## student_mat_ml.ipynb

### 1、实验目标

使用线性回归、决策树回归和多项式回归预测学生期末成绩，并比较模型性能。。 



### 2、数据文件说明

**数据集为datasets中的"学生表现数据集"，student-mat.csv**

**字段说明：**

1. school-学生学校（二元：GP-Gabriel Pereira或MS-Mousinho da Silveira）
2. sex-学生性别（二元：“F”-女性或“M”-男性）
3. age-学生的年龄（数字：从15到22）
4. address-学生的家庭住址类型（二元：“U”-城市或“R”-农村）
5. famsize-家族规模（二元：“LE3”-小于或等于3或“GT3”-大于3）
6. Pstatus-父母的同居状态（二元：“T”-同居或“A”-分居）
7. Medu-母亲的教育（数字：0-无，1-小学教育（4年级），2-5至9年级，3-中等教育或4-高等教育）
8. Fedu-父亲的教育（数字：0-无，1-小学教育（4年级），2-5至9年级，3-中等教育或4-高等教育）
9. Mjob-母亲的工作（名义上：“教师”、“与医疗保健有关的”、“公务员”（如行政或警察）、“在家”或“其他”）
10.  Fjob-父亲的工作（名义上：“教师”、“与医疗保健有关的”、“公务员”（如行政或警察）、“在家”或“其他”）
11.  reason-选择这所学校的理由（名义上：靠近“家”、学校“声誉”、“课程”偏好或“其他”）
12. guardian-学生的监护人（名义：“母亲”、“父亲”或“其他”）
13. traveltime-从家到学校的旅行时间（数字：1-<15分钟，2-15-30分钟，3-30分钟-1小时，或4->1小时）
14. studytime-每周学习时间（数字：1-<2小时、2-2-2-5小时、3-5-10小时或4->10小时）
15. failures-过去的挂科次数（如果1<=n<3，则为n，否则为4）
16. schoolsup-额外教育支持（二元：是或否）
17. famsup-家庭教育支持（二元：是或否）
18. paid-额外付费数学或葡萄牙语课程（二元：是或否）
19. activities-课外活动（二元：是或否）
20. nursery-就读于托儿所（二元：是或否）
21.  higher-是否有升学意愿（二元：是或否）
22. internet-在家上网（二元：是或否）
23.  romantic-有浪漫关系（二元：是或否）
24. famrel-家庭关系质量（数字：从1-非常差到5-优秀）
25.  freetime-放学后的自由时间（数字：从1-非常低到5-非常高）
26.  goout-与朋友外出（数字：从1-非常低到5-非常高）
27.  Dalc-工作日饮酒量（数字：从1-非常低到5-非常高）
28. Walc-周末饮酒量（数字：从1-非常低到5-非常高）
29. health-当前健康状况（数字：从1-非常差到5-非常好）
30. absences-旷课次数（数字：从0到93）



**成绩**

1. G1-第一学期成绩（数字：从0到20）
2. G2-第二学期成绩（数字：从0到20）
3. G3-最终成绩（数字：从0到20，输出目标）



### 3、实现步骤：

1. 将数据加载到Pandas DataFrame
2. 分离特征(X)和目标变量(y)
3. 按80-20划分训练测试集(random_state=42)
4. 使用StandardScaler标准化特征
5. 训练以下模型：
   - 线性回归
   - 决策树回归
   - 多项式回归(degree=2)
6. 计算各模型的MSE分数
7. 输出评估指标



## titanic-ml.ipynb

### 1、实验目标

目标是训练一个可以根据其他列预测Survived（是否存活）列的分类器

### 2、数据文件说明

- 泰坦尼克号数据集 titanic.tgz，这将提供两个CSV文件，train.csv和test.csv

- test_augmented.csv是测试模型评估好坏的文件

- test_predict.csv是通过模型预测test.csv中的数据生成的文件



**字段说明**

- PassengerId  ：  每位乘客的唯一标识符
- Survived         ：     是否幸存（1：幸存，0：未幸存）
- Pclass             ：  乘客的舱位等级（1-一等舱，2-二等舱，3-三等舱）
- Name             ：  姓名
- Sex                  ：  性别，male,female
- Age                  :   年龄
- SibSp              ：  与乘客一起旅行的兄弟姐妹或配偶的数量
- Parch              ：  与乘客一起旅行的父母或儿童人数
- Ticket              ：  票证号
- Fare                ：  票价
- Cabin              ：  乘客所住的客舱编号
- Embarked      ：  乘客登船的港口（C-瑟堡（法国），Q-皇后镇（爱尔兰），S-南安普顿（英格兰））



### 3、实现步骤

1. 数据加载
2. 对数据集做预处理（独热编码、缺失值填充、标准缩放）
3. 使用以下模型训练：
   - 逻辑回归
   - 决策树分类
   - KNN分类
4. 模型评估：计算每个模型的准确率和F1分数



### 4、一些有趣的尝试

- 男性和女性的存活率谁更高
- 成年、未成年和老年的存活率是否不同
- 根据乘客随行人员的类别和数量来看存活率是否不同



## softmax_without_sklearn.ipynb

### 1、实验目标

​			在不使用sklearn的情况下，仅使用Numpy，为softmax回归实现批量梯度下降（需带早停策略和 $\ell_2$ 正则化），将它用于分类任务，使用鸢尾花数据集

### 2、数据集

​	使用sklearn中datasets的IRIS数据集，数据集所在包：`from sklearn.datasets import load_iris`

​	

**样本数**：150

**特征数**：4

**特征名**：

- sepal length in cm  花萼长度
- sepal width in cm   花萼宽度
- petal length in cm   花瓣长度
- petal width in cm     花瓣宽度

**类别——样本数**：

- Setosa  -- 50
- Versicolour -- 50
- Virginica -- 50





### 3、实现步骤

​	1.加载数据集（从sklearn库中）

​	2.分离数据集（shuffle + split ）

​	3.实现softmax的损失函数（交叉熵损失）

​	4.计算梯度

​	5.实现批量梯度下降算法

​	6.绘制相关图像（包含损失值关于迭代次数的变化，以及决策边界）





## wine_svm.ipynb

### 1、实验目标

训练一个分类模型，该模型能够根据葡萄酒的化学分析预测种植者。



### 2、数据集

使用的是sklearn库中的葡萄酒数据集，使用`from sklearn.datasets import load_wine`来加载



**样本数**：178

**特征数**：13

**特征名**：

- Alcohol
- Malic acid
- Ash
- Alcalinity of ash
- Magnesium
- Total phenols
- Flavanoids
- Nonflavanoid phenols
- Proanthocyanins
- Color intensity
- Hue
- OD280/OD315 of diluted wines
- Proline



**类别——样本数:**

- class_0 -- 59
- class_1 -- 71
- class_2 -- 48





### 3、实现步骤

1.加载数据集

2.分离数据集

3.数据集预处理（填充缺失值、标准化等操作）

4.使用流水线去拟合数据

5.分类模型评估：计算模型的准确率





## gradient_descent_simulate_svc.ipynb

### 1、实验目标

​		自定义SVC，把SVM的分类器（SVC）看成梯度下降来实现。随后将自定义的SVM分类用于 iris data(鸢尾花数据)； 取花瓣长度 和 花瓣宽度特征， 分类 看是不是 分类2（Iris-Virginica）的花



### 2、数据集

使用sklearn中datasets的IRIS数据集，数据集所在包：`from sklearn.datasets import load_iris`

​	

**样本数**：150

**特征数**：4

**特征名**：

- sepal length in cm  花萼长度
- sepal width in cm   花萼宽度
- petal length in cm   花瓣长度
- petal width in cm     花瓣宽度

**类别——样本数**：

- Setosa  -- 50
- Versicolour -- 50
- Virginica -- 50



### 3、实现步骤

1.加载数据集

2.分离数据集

3.SVM分类器的原理阐释（公式推导，重要！！！）

4.自定义SVC（使用梯度下降模拟，继承自sklearn的BaseEstimator）

5.模型测试与评估

6.绘制相关图像





## decision_tree_demo.ipynb

决策树demo，并使用决策树模拟随机森林



## mnist_mlp.ipynb

在MNIST数据集上训练深度MLP。看看是否可以通过手动调整超参数获得98%以上的精度。

首先尝试搜索最佳学习率（即通过以指数方式增加学习率，根据学习率变化绘制训练损失，并找到损失激增的点）。

接下来，尝试使用Keras Tuner调整超参数——保存检查点，使用早停，并使用TensorBoard绘制学习曲线。





## dnn_cifar10.ipynb

在CIFAR10图像数据集上练习训练深度神经网络：

CIFAR-10数据集包含60,000张32×32像素的彩色图像，分为10个不同的类别。这10个类别分别是飞机、汽车、鸟类、猫、鹿、狗、青蛙、马、船和卡车，每个类别有6,000张图片。

飞机、汽车、鸟类、猫、鹿、狗、青蛙、马、船和卡车 对应的分类编码是0，1，2，3，4，5，6，7，8，9


1. 构建一个DNN，使其包含20个隐藏层，每个隐藏层包含100个神经元。使用He初始化和Swish激活函数、使用Nadam优化和早停技术
3. 尝试添加批量归一化并比较学习曲线：收敛速度是否比以前快？会产生更好的模型吗？它如何影响训练速度？
4. 尝试用SELU替换批量归一化，并进行必要的调整以确保网络是自归一化的（即归一化输入特征，使用LeCun正态初始化，确保DNN仅仅包含一系列的密集层等）
5. 尝试使用Alpha dropout正则化模型。然后，在不重新训练模型的情况下，看看是否可以使用MC dropout获得更好的精度。
6. 使用1周期调度来重新训练模型，看看它是否可以提高训练速度和模型精度。





## customize_normalize_layer.ipynb

实验目标：实现归一化的自定义层

   - a. `build()` 方法应定义两个可训练的权重 α 和 β，它们的形状均为 `input_shape[-1:]`，数据类型为 `tf.float32`。α 应该用 1 初始化，而 β 必须用 0 初始化。
   - b. `call()` 方法应计算每个实例特征的均值和标准差，该函数应计算并返回
      $$
      \alpha \otimes \frac{(X-\mu)}{(\sigma+\epsilon)} + \beta
      $$
      其中 ε 是表示项精度的一个常量（避免被零除的小常数，例如 0.001）,$\otimes$表示逐个元素相乘
   - c. 确保自定义层产生与**tf.keras.layers.LayerNormalization**层相同（或几乎相同）的输出。





## customize_train_loop.ipynb

实验目标：自定义Train Loop

使用自定义训练循环，训练模型，来处理Fashion MNIST数据集：
   - a.显示每个轮次、迭代、平均训练损失和每个轮次的平均精度（在每次迭代中更新），以及每个轮次结束时的验证损失和精度。
   - b.尝试对上面的层和下面的层使用具有不同学习率的不同优化器。





## cifar10_with_cnn.ipynb

实验目标：使用带有残差块的CNN训练cifar10数据集

实验步骤：

- 将数据集分为8分类和2分类
- 在数据集8分类上预训练模型，之后迁移到2分类模型上训练









