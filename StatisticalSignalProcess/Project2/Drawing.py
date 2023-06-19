import torch
import matplotlib.pyplot as plt
import os
from Initialize import PROJECTADDRESS
from typing import List

REPORTADDRESS = os.path.join(*[PROJECTADDRESS, 'Result'])
PICADDRESS = os.path.join(*[PROJECTADDRESS, 'Pics'])
fig = plt.figure(figsize=(6, 6))
data1 = torch.load(os.path.join(REPORTADDRESS, 'Playground1.oracleReport'))
data2 = torch.load(os.path.join(REPORTADDRESS, 'Playground1NOISE=2.oracleReport'))
data3 = torch.load(os.path.join(REPORTADDRESS, 'Apple3.oracleReport'))
data4 = torch.load(os.path.join(REPORTADDRESS, 'Playground1Window=2.oracleReport'))
data5 = torch.load(os.path.join(REPORTADDRESS, 'Playground1Window=5.oracleReport'))


def draw(drawingData: List[torch.tensor], saveAddress=None,):
    ax1 = fig.add_subplot(1, 1, 1)
    # set the title
    ax1.set_title('ROC')
    # 我们总是可以直接将所有都判给H1来获得一个Pd=Pfa=1的分类器
    ones = torch.ones((1, 2))
    # 同理，我们全都判给H0也可以轻松获得一个Pd=Pfa=0的分类器
    zeros = torch.zeros((1, 2))
    colors = 'rgbcym'
    for i in range(len(drawingData)):

        drawingData[i] = torch.cat((zeros, drawingData[i], ones))
        # plot the data as points
        ax1.scatter(drawingData[i][:, 1], drawingData[i][:, 0], alpha=0.3)
        ax1.plot(drawingData[i][:, 1], drawingData[i][:, 0], color=colors[i % len(colors)], alpha=0.7)
    ax1.set_xlabel('$P_{FA}$')
    ax1.set_ylabel('$P_{D}$')
    # set up the maximum and minimum for the whole graph?
    plt.ylim(ymin=-0.2, ymax=1.2)
    plt.xlim(xmin=-0.2, xmax=1.2)
    if saveAddress is None:
        plt.show()
    else:
        plt.savefig(saveAddress)


# # 当不同的力量容忍值被采用时
# raw=[]
# for i in range(1,10):
#     raw.append(data1[i,:])

# # 当不同的角度容忍值被采用时
# raw=[]
# for i in range(1,10):
#     raw.append(data1[:,i])
#
# for i in range(60, 300,20):
#     raw.append(data1[:, i])

# # 测试噪声对检测的影响
# raw=[]
# raw.append(data1[10,:])
# raw.append(data2[10,:])
# raw.append(data1[20,:])
# raw.append(data2[20,:])

# # 测试运动对检测的影响
# raw = []
# raw.append(data1[10, :])
# raw.append(data3[10, :])

# 测试窗口对检测的影响
raw = []
raw.append(data1[10,:])
raw.append(data4[10,:])
raw.append(data5[10,:])
draw(raw, os.path.join(PICADDRESS, 'Window.png'))
