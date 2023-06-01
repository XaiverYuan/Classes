from typing import Callable
import torch
import matplotlib.pyplot as plt
import h5py
import numpy as np

# 设置一些基本常数
g = 9.82872200
forceSigma = 1.20829213
degreeSigma = 0.01193243

# 获取数据
# 从这个网站上搞来的数据 （动数据）
# https://www.cvl.isy.liu.se/research/datasets/gopro-imu-dataset/
file = h5py.File(
    r'C:\Users\96585\Documents\GitHub\Classes\StatisticalSignalProcess\Project2\OracleData\playground1\imu.h5', 'r')
# 依据h5格式数据的获取方式获取数据
# https://zhuanlan.zhihu.com/p/150126263
rawDataForce = torch.tensor(np.array(file['acc'][:])).T
rawDataDegree = torch.tensor(np.array(file['gyro'][:])).T
movingData = torch.zeros((rawDataDegree.shape[0], 4))
# 处理数据，将三个力直接合成力的模长
movingData[:, 0] = (rawDataForce[:, 0] ** 2 + rawDataForce[:, 1] ** 2 + rawDataForce[:, 2] ** 2) ** 0.5
movingData[:, 1:] = rawDataDegree
del rawDataDegree, rawDataForce
# 考虑到视频中有一部分是静止的，所以将前后部分信息截去
movingData = movingData[10000:20000]  # 由于已经是真实数据，就不再仿真了

# 蒙特卡洛10000个数据（基于data1的sigma）
rawDataForce = torch.normal(g, forceSigma, (10000, 1))
rawDataDegree = torch.normal(0, degreeSigma, (10000, 3))
stableData = torch.zeros((rawDataDegree.shape[0], 4))
stableData[:, 0] = rawDataForce[0]
stableData[:, 1:] = rawDataDegree
del rawDataDegree, rawDataForce

# 开始画图
fig = plt.figure()
imu = fig.add_subplot(2, 2, 1)


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
classifier(stableData,1.5,0.04)

records = torch.zeros(60, 60, 2)
for i in range(60):
    for j in range(60):
        forceGamma = i / 20 * forceSigma
        degreeGamma = i / 20 * degreeSigma
        Pd = classifier(data=stableData, forceGamma=forceGamma, degreeGamma=degreeGamma).sum() / 10000
        Pfa = 10000 - classifier(data=movingData, forceGamma=forceGamma, degreeGamma=degreeGamma).sum() / 10000
        records[i][j][0] = Pd
        records[i][j][1] = Pfa
print(records)
