# ����Ҫ������ ' get_MNIST.py '�ļ���ȡTrain_x,Train_y,Test_x,Test_y
# ���ܽ�����һ���Ĳ���
#ɸѡ��0,1����
K = [0,1,2,3,4,5,6,7,8,9]
m,n = Train_x.shape
train_y = []
# ��K�е�������ѡ����
for i in range(0,len(K)):
    train_y.extend(Train_y[Train_y == K[i]])
train_y = np.array(train_y)
# ���о���
train_y = OFK(train_y,K)
train_x = []
for i in range(0,len(K)):
    train_x.extend(list(Train_x[Train_y == K[i],:]))
train_x = np.array(train_x)
# ���������Ƿǳ���˳��ģ�����������Կ���һ�´���˳��

W = train_lsc(train_x,train_y)

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
print(accuary)