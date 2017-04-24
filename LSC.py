# 这里要先运行 ' get_MNIST.py '文件获取Train_x,Train_y,Test_x,Test_y
# 才能进行下一步的操作，然后在运行LSC.py文件
#筛选出0,1数据
import random
K = [0,1,2,3,4,5,6,7,8,9]
m,n = Train_x.shape
train_y = []
# 将K中的数据挑选出来
for i in range(0,len(K)):
    train_y.extend(Train_y[Train_y == K[i]])
train_y = np.array(train_y)
# 进行矩阵化
train_y = OFK(train_y,K)
train_x = []
for i in range(0,len(K)):
    train_x.extend(list(Train_x[Train_y == K[i],:]))
train_x = np.array(train_x)
# 这里数据是非常有顺序的，或许这里可以考虑一下打乱顺序
L = np.arange(0,train_x.shape[0],1)
random.shuffle(L)
L = tuple(L)
# 结果发现打乱了顺序对结果也没有什么影响，这个模型本身就不受顺序影响^V^
W = train_lsc(train_x[L[0:len(L)],:],train_y[L[0:len(L)],:])

m,n = Test_x.shape
test_y = []
for i in range(0,len(K)):
    test_y.extend(Test_y[Test_y == K[i]])
test_y = np.array(test_y)
test_y = OFK(test_y,K)
test_x = []
for i in range(0,len(K)):
    test_x.extend(list(Test_x[Test_y == K[i],:]))
test_x = np.array(test_x)
pre_Y = test_lsc(test_x,W)
pre_Y = one_of_kind(pre_Y,K)

accuary = 1-sum(sum(abs(pre_Y - test_y)))/m
print('accuary = ',accuary)
