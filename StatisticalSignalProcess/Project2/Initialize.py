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

def classifier(data: torch.tensor, forceGamma: float, degreeGamma: float) -> torch.tensor:
    """
    给定数据和门限，判断哪些数据符合所有条件
    :param data: 待鉴定数据
    :param forceGamma: 受力与g之间差距的极限容忍值
    :param degreeGamma: 最大角速度绝对值的极限容忍值
    :return: 一个布尔张量，测量了数据是否符合条件
    """
    # 判定受力是否符合条件
    forceAccept = torch.bitwise_and(data[:, 0] < g + forceGamma, data[:, 0] > g - forceGamma)
    # 获取最大角速度
    maxDegree = torch.max(torch.abs(data[:, 1:]), 1)[0]
    # 判定角速度是否符合条件
    degreeAccept = torch.bitwise_and(maxDegree < degreeGamma, maxDegree > -degreeGamma)
    return torch.bitwise_and(forceAccept, degreeAccept)

