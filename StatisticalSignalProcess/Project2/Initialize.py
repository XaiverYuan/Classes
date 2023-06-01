import os
import torch
import numpy as np

# OracleData文件夹位置
ADDRESS = r"OracleData"

# 2060实测可以
DEVICE = 'cuda'


def readFile(fileAddress: str, device: str = DEVICE) -> torch.Tensor:
    data = torch.tensor(np.loadtxt(open(fileAddress, 'rb'), delimiter=',', skiprows=1), device=device)
    # 直接把第一列变成力的模长，后三列一样
    answer = torch.zeros((data.shape[0], 4))
    answer[:,1:] = data[:,3:]
    answer[:,0] = (data[:, 0] ** 2 + data[:, 1] ** 2 + data[:, 2] ** 2) ** 0.5
    return answer


# 读取文件
data1 = readFile(os.path.join(ADDRESS, 'data1.csv'))
data2 = readFile(os.path.join(ADDRESS, 'data2.csv'))

# 计算重力加速度，也可以手工设置
g = data1[:,0].mean()
print('G = %.2f' % g)

# 计算sigma
forceSigma = data1[:,0].std()
degreeSigma = data1[:, 1:].std()
print('Force Std  = %.4f' % forceSigma)
print('degree Std = %.4f' % degreeSigma)

# 分开数据，一半用作测试集，一半用作训练集，考虑到物理世界的连续性，所以不随机选，而是间隔一个选一个
dataAnon = data2.reshape(data2.shape[0] // 2, 8)
trainingData = dataAnon[:, :4]
testingData = dataAnon[:, 4:]
del dataAnon, data2

# 蒙特卡洛仿真
torch.normal(0,forceSigma)

