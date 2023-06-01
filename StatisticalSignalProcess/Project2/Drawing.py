import torch
import matplotlib.pyplot as plt
import os
from Initialize import PROJECTADDRESS, DEVICE

REPORTADDRESS = os.path.join(*[PROJECTADDRESS, 'Result'])
fig = plt.figure(figsize=(8, 8))
data = torch.load(os.path.join(REPORTADDRESS, 'Playground1.oracleReport'))

ax1 = fig.add_subplot(1, 1, 1)
# set the title
ax1.set_title('ROC')
# plot the data as points
drawingData = data[290, :]
print(drawingData[:, 0].max())
print(drawingData[:, 0].min())
print(drawingData[:, 1].max())
print(drawingData[:, 1].min())
ax1.scatter(drawingData[:, 1], drawingData[:, 0], alpha=0.3)
ax1.plot(drawingData[:, 1], drawingData[:, 0], color='r', alpha=0.7)
ax1.set_xlabel('$P_{FA}$')
ax1.set_ylabel('$P_{D}$')
# set up the maximum and minimum for the whole graph?
plt.ylim(ymin=-0.2, ymax=1.2)
plt.xlim(xmin=-0.2, xmax=1.2)
plt.show()
