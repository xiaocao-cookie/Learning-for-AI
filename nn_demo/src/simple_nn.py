import struct
import numpy as np
import gzip

def add(x, y):
    """一个简单的add函数，以便熟悉自动测试（pytest）

    Args:
        x (Python数字 或者 numpy array)
        y (Python数字 或者 numpy array)

    Return:
        x+y的和
    """
    return x + y


def parse_mnist(image_filename, label_filename):
    """ 读取 MNIST 格式的图像和标签文件。有关文件格式的说明，请参阅此页面：
    http://yann.lecun.com/exdb/mnist/。

    参数：
    image_filename（字符串）：MNIST 格式的 gzip 压缩图像文件的名称
    label_filename（字符串）：MNIST 格式的 gzip 压缩标签文件的名称

    返回：
    tuple (X,y)：
    x (numpy.ndarray[np.float32])：
    包含已加载数据的二维 numpy 数组。数据的维度应为 (num_examples x input_dim)，其中“input_dim”是数据的完整维度，
    例如，
    由于 MNIST 图像为 28x28，因此input_dim 为 784。
    值应为 np.float32 类型，并且数据应被归一化为最小值为 0.0，最大值为 1.0

    y (numpy.ndarray[dtype=np.uint8])：包含示例标签的一维 NumPy 数组。
    值应为 np.uint8 类型，对于 MNIST，将包含 0-9 的值。

    """

    # 读取图像文件
    with gzip.open(image_filename, 'rb') as f:
        # 读取文件头信息
        # 大端序：最高有效字节存储在最低的内存地址，例如12 34 56 78
        magic = int.from_bytes(f.read(4), byteorder='big')
        image_num = int.from_bytes(f.read(4), byteorder='big')
        row_num = int.from_bytes(f.read(4), byteorder='big')
        col_num = int.from_bytes(f.read(4), byteorder='big')

        # 读取图像数据
        data = f.read()
        images_data = np.frombuffer(data, dtype=np.uint8)
        images_data = images_data.reshape(image_num, row_num * col_num)

        X = images_data.astype(np.float32) / 255.


    # 读取标签文件
    with gzip.open(label_filename, 'rb') as f:
        magic = int.from_bytes(f.read(4), byteorder='big')
        label_num = int.from_bytes(f.read(4), byteorder='big')

        # 读取标签数据
        data = f.read()
        y = np.frombuffer(data, dtype=np.uint8)

    return X, y




def softmax_loss(Z, y):
    """ 返回 softmax 损失。

    参数：
    z (np.ndarray[np.float32])：形状为 (batch_size, num_classes) 的二维 NumPy 数组，
    包含每个类别的 对数概率 预测值 （softmax函数激活之前的值）。pred

    y (np.ndarray[np.uint8])：形状为 (batch_size, ) 的一维 NumPy 数组，包含每个样本的真实标签。

    返回：
    样本的平均 softmax 损失。
    """

    losses = np.log(np.sum(np.exp(Z), axis=1)) - Z[np.arange(len(y)), y]
    return np.mean(losses)


def softmax_regression_epoch(X, y, theta, lr = 0.1, batch=100):
    """ 使用步长 lr 和指定的批次大小，对数据运行单轮 小批量梯度下降 进行 softmax 回归。
    此函数会修改 θ 矩阵，并迭代 X 中的批次，但不对顺序进行随机化。

    参数：
    X (np.ndarray[np.float32])：大小为(num_examples x input_dim) 的二维输入数组。
    y (np.ndarray[np.uint8])：大小为 (num_examples,) 的一维类别标签数组。
    theta (np.ndarrray[np.float32])：softmax 回归的二维数组参数，形状为 (input_dim, num_classes)。
    lr (float)：SGD 的步长（学习率）。
    batch (int)：SGD 小批次的大小。

    返回：
    无
    """

    m = X.shape[0]
    classes_num = theta.shape[1]

    # 一共m个样本，每个批次的数量为batch
    for i in range(0, m, batch):
        # 取一个批次的样本数
        X_batch = X[i:i + batch]
        y_batch = y[i:i + batch]

        # 这里是为了解决样本数 / 批次数有余数的情况，如果使用batch,则梯度下降到最后一个批次的数量可能会错
        batch_size = X_batch.shape[0]

        # 将y转成独热编码
        y_onehot = np.eye(classes_num)[y_batch]

        # 计算梯度
        Z = np.exp(X_batch @ theta) / np.sum(np.exp(X_batch @ theta), axis=1, keepdims=True)     # m x k
        gradient = (X_batch.T @ (Z - y_onehot)) / batch_size    # input_dim x k

        # 更新权重
        theta -= lr * gradient




def nn_epoch(X, y, W1, W2, lr = 0.1, batch=100):
    """ 对由权重 W1 和 W2 定义的双层神经网络（无偏差项）运行一个 小批量梯度下降 迭代轮次：
    logits = ReLU(X * W1) * W2
    该函数应使用步长 lr 和指定的批次大小（并且同样，不随机化 X 的顺序）。它应修改 W1 和 W2 矩阵。

    参数：
    X (np.ndarray[np.float32])：大小为 (num_examples x input_dim) 的二维输入数组。
    y (np.ndarray[np.uint8])：大小为 (num_examples,) 的一维类别标签数组。
    W1 (np.ndarray[np.float32])：第一层权重的二维数组，形状为(input_dim, hidden_dim)
    W2 (np.ndarray[np.float32])：第二层权重的二维数组。形状(hidden_dim, num_classes)
    lr (float)：SGD 的步长（学习率）
    batch (int)：SGD 小批次的大小

    返回：
    无
    """
    m = X.shape[0]
    classes_num = W2.shape[1]


    for i in range(0, m, batch):
        X_batch = X[i:i+batch]
        y_batch = y[i:i+batch]
        batch_size = X_batch.shape[0]

        y_onehot = np.eye(classes_num)[y_batch]

        # 前向传播
        # a1代表第一层的线性组合值，z1代表激活后的值
        # a1 = X_batch @ W1
        a1 = np.dot(X_batch, W1)
        z1 = np.where(a1 > 0, a1, 0)           # samples x hidden_dim
        a2 = np.dot(z1 ,W2)


        # 反向传播
        exp2 = np.exp(a2)
        norm_a2  = exp2 / np.sum(exp2, axis=1, keepdims=True)       # 归一化a2
        G2 = norm_a2 - y_onehot
        G1 = (z1 > 0) * np.dot(G2, W2.T)       # samples x hidden_dim
        gw1 = np.dot(X_batch.T, G1) / batch_size
        gw2 = np.dot(z1.T, G2) / batch_size

        # 权重更新
        W1 -= lr * gw1
        W2 -= lr * gw2





### 下面的代码不用编辑，只是用来展示功能的

def loss_err(h,y):
    """ Helper funciton to compute both loss and error"""
    return softmax_loss(h,y), np.mean(h.argmax(axis=1) != y)


def train_softmax(X_tr, y_tr, X_te, y_te, epochs=10, lr=0.5, batch=100):
    """ 示例函数，用softmax回归训练 """
    theta = np.zeros((X_tr.shape[1], y_tr.max()+1), dtype=np.float32)
    print("| Epoch | Train Loss | Train Err | Test Loss | Test Err |")
    for epoch in range(epochs):
        softmax_regression_epoch(X_tr, y_tr, theta, lr=lr, batch=batch)
        train_loss, train_err = loss_err(X_tr @ theta, y_tr)
        test_loss, test_err = loss_err(X_te @ theta, y_te)
        print("|  {:>4} |    {:.5f} |   {:.5f} |   {:.5f} |  {:.5f} |"\
              .format(epoch, train_loss, train_err, test_loss, test_err))


def train_nn(X_tr, y_tr, X_te, y_te, hidden_dim = 500,
             epochs=10, lr=0.5, batch=100):
    """ 示例函数，训练神经网络 """
    n, k = X_tr.shape[1], y_tr.max() + 1
    np.random.seed(0)
    W1 = np.random.randn(n, hidden_dim).astype(np.float32) / np.sqrt(hidden_dim)
    W2 = np.random.randn(hidden_dim, k).astype(np.float32) / np.sqrt(k)

    print("| Epoch | Train Loss | Train Err | Test Loss | Test Err |")
    for epoch in range(epochs):
        nn_epoch(X_tr, y_tr, W1, W2, lr=lr, batch=batch)
        train_loss, train_err = loss_err(np.maximum(X_tr@W1,0)@W2, y_tr)
        test_loss, test_err = loss_err(np.maximum(X_te@W1,0)@W2, y_te)
        print("|  {:>4} |    {:.5f} |   {:.5f} |   {:.5f} |  {:.5f} |"\
              .format(epoch, train_loss, train_err, test_loss, test_err))



if __name__ == "__main__":
    X_tr, y_tr = parse_mnist("data/train-images-idx3-ubyte.gz",
                             "data/train-labels-idx1-ubyte.gz")
    X_te, y_te = parse_mnist("data/t10k-images-idx3-ubyte.gz",
                             "data/t10k-labels-idx1-ubyte.gz")

    print("Training softmax regression")
    train_softmax(X_tr, y_tr, X_te, y_te, epochs=10, lr = 0.1)

    print("\nTraining two layer neural network w/ 100 hidden units")
    train_nn(X_tr, y_tr, X_te, y_te, hidden_dim=100, epochs=20, lr = 0.2)