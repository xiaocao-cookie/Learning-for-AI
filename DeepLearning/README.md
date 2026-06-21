# Deep Learning

```text
DeepLearning/
├── examples/
│   ├── CNN_NumPy/
│   ├── nn_demo/
│   └── RNN_Numpy/
│
├── notebooks/
│   ├── cifar10_with_cnn.ipynb
│   ├── customize_normalize_layer.ipynb
│   ├── customize_train_loop.ipynb
│   ├── dnn_cifar10.ipynb
│   ├── gradient_descent_simulate_svc.ipynb
│   └── mnist_mlp.ipynb
│
│
└── README.md
```


## examples 文件夹

### CNN_NumPy

使用NumPy实现CNN（Convolution Nerual Network）中的卷积层和池化层，里面有相应的测试文件以及说明


### nn_demo 文件夹

此文件夹为神经网络（Neural Network）的demo，
这里，我在文件中使用了原生的Python/NumPy库，
构建一个基本的softmax回归算法和一个简单的两层神经网络，
不使用任何的Keras库的算法。
更详细的步骤参见此文件夹下的 *任务说明.ipynb* 文件


### RNN_Numpy

使用NumPy实现RNN（Recurrent Neural Network）和LSTM（Long Short-Term Memory）网络的前向传播过程，里面有相应的测试代码和公式推导



## notebooks 文件夹

### cifar10_with_cnn.ipynb

实验目标：使用带有残差块的CNN训练cifar10数据集

实验步骤：

- 将数据集分为8分类和2分类
- 在数据集8分类上预训练模型，之后迁移到2分类模型上训练


### customize_normalize_layer.ipynb

实验目标：实现归一化的自定义层

   - a. `build()` 方法应定义两个可训练的权重 α 和 β，它们的形状均为 `input_shape[-1:]`，数据类型为 `tf.float32`。α 应该用 1 初始化，而 β 必须用 0 初始化。
   - b. `call()` 方法应计算每个实例特征的均值和标准差，该函数应计算并返回
      $$
      \alpha \otimes \frac{(X-\mu)}{(\sigma+\epsilon)} + \beta
      $$
      其中 ε 是表示项精度的一个常量（避免被零除的小常数，例如 0.001）,$\otimes$表示逐个元素相乘
   - c. 确保自定义层产生与**tf.keras.layers.LayerNormalization**层相同（或几乎相同）的输出。


### customize_train_loop.ipynb

实验目标：自定义Train Loop

使用自定义训练循环，训练模型，来处理Fashion MNIST数据集：
   - a.显示每个轮次、迭代、平均训练损失和每个轮次的平均精度（在每次迭代中更新），以及每个轮次结束时的验证损失和精度。
   - b.尝试对上面的层和下面的层使用具有不同学习率的不同优化器。


### dnn_cifar10.ipynb

在CIFAR10图像数据集上练习训练深度神经网络：

CIFAR-10数据集包含60,000张32×32像素的彩色图像，分为10个不同的类别。这10个类别分别是飞机、汽车、鸟类、猫、鹿、狗、青蛙、马、船和卡车，每个类别有6,000张图片。

飞机、汽车、鸟类、猫、鹿、狗、青蛙、马、船和卡车 对应的分类编码是0，1，2，3，4，5，6，7，8，9


1. 构建一个DNN，使其包含20个隐藏层，每个隐藏层包含100个神经元。使用He初始化和Swish激活函数、使用Nadam优化和早停技术
3. 尝试添加批量归一化并比较学习曲线：收敛速度是否比以前快？会产生更好的模型吗？它如何影响训练速度？
4. 尝试用SELU替换批量归一化，并进行必要的调整以确保网络是自归一化的（即归一化输入特征，使用LeCun正态初始化，确保DNN仅仅包含一系列的密集层等）
5. 尝试使用Alpha dropout正则化模型。然后，在不重新训练模型的情况下，看看是否可以使用MC dropout获得更好的精度。
6. 使用1周期调度来重新训练模型，看看它是否可以提高训练速度和模型精度。


### gradient_descent_simulate_svc.ipynb

#### 1、实验目标

自定义SVC，把SVM的分类器（SVC）看成梯度下降来实现。随后将自定义的SVM分类用于 iris data(鸢尾花数据)； 
取花瓣长度 和 花瓣宽度特征， 分类 看是不是 分类2（Iris-Virginica）的花



#### 2、数据集

使用sklearn中datasets的IRIS数据集，数据集所在包：`from sklearn.datasets import load_iris`

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



#### 3、实现步骤
1. 加载数据集
2. 分离数据集
3. SVM分类器的原理阐释（公式推导，重要！！！）
4. 自定义SVC（使用梯度下降模拟，继承自sklearn的BaseEstimator）
5. 模型测试与评估
6. 绘制相关图像


### mnist_mlp.ipynb

在MNIST数据集上训练深度MLP。看看是否可以通过手动调整超参数获得98%以上的精度。

首先尝试搜索最佳学习率（即通过以指数方式增加学习率，根据学习率变化绘制训练损失，并找到损失激增的点）。

接下来，尝试使用Keras Tuner调整超参数——保存检查点，使用早停，并使用TensorBoard绘制学习曲线。

