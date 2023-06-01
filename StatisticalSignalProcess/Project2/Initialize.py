import os
import torch
import numpy as np

PROJECTADDRESS='D:\WINDOWS_DOCUMENTS\GitHub\Classes\StatisticalSignalProcess\Project2'

# OracleData文件夹位置
DATAADDRESS = os.path.join(PROJECTADDRESS, 'OracleData')

# 2060实测可以
DEVICE = 'cuda'


def readFile(fileAddress: str, device: str = DEVICE) -> torch.Tensor:
    data = torch.tensor(np.loadtxt(open(fileAddress, 'rb'), delimiter=',', skiprows=1), device=device)
    # 直接把第一列变成力的模长，后三列一样
    answer = torch.zeros((data.shape[0], 4))
    answer[:, 1:] = data[:, 3:]
    answer[:, 0] = (data[:, 0] ** 2 + data[:, 1] ** 2 + data[:, 2] ** 2) ** 0.5
    return answer


# 读取文件
data1 = readFile(os.path.join(DATAADDRESS, 'data1.csv'))

# 计算重力加速度，也可以手工设置
g = data1[:, 0].mean()
print('G = %.8f' % g)

# 计算sigma
forceSigma = data1[:, 0].std()
degreeSigma = data1[:, 1:].std()
print('Force Std  = %.8f' % forceSigma)
print('degree Std = %.8f' % degreeSigma)

