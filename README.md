# LSC
LSC 最小二乘线性分类算法，在Python中是有机器学习包sklearn模块可以进行计算
## 'get_MNIST.py'
* get_MNIST.py 是用于获取数据，也在其中定义了关于算法所需要的函数:<br>
* loadImageSet(filename) : 获取二进制文件 train-images-idx3-ubyte 和 t10k-images-idx3-ubyte 的图像数据矩阵<br>
* loadLabelSet(filename) ： 获取二进制文件 train-labels-idx1-ubyte 和 t10k-labels-idx1-ubyte 的图像标签文件<br>
* train_lsc(train_x,train_y) : 从训练数据学习出参数 W <br>
* test_lsc(test_x,W) : 预测测试集的标签<br>
* OFK(y,K) ： 将标签向量转化为需要的标签矩阵<br>
* one_of_kind(y,K) ： 将测试集预测出来的标签向量转化为需要的标签矩阵<br>

## 'LSC.py'
LSC.py 是实现最小二乘线性分类算法的一个流程,其中 K 是可以更改的<br>
* K 表示选择mnist中的数据类别进行训练，K = [0,1] or K = [0,6,8]...<br>
* accuary 表示在测试集上的正确率，评估模型^V^

K = [0,1]<br>
accuary = 0.9974<br>

K = [0,6,8]<br>
accuary = 0.9848<br>

K = [0,1,2,3,4,5,6,7,8,9]<br>
accuary = 0.7206<br>
