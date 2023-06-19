from Initialize import *
from Drawing import draw
import torch
import matplotlib.pyplot as plt
testSet = readFile(os.path.join(DATAADDRESS, 'data2.csv'))
result = classifier(testSet, 10 / 3 * forceSigma, 10 / 3 * degreeSigma)
toDraw = torch.zeros((result.shape[0], 2))

toDraw[:,1] = result*1
toDraw[:, 0] = torch.arange(result.shape[0])

fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(1, 1, 1)
# set the title
ax1.set_title('Result')

# plot the data as points
ax1.scatter(toDraw[:,0],toDraw[:,1], alpha=0.3)
ax1.plot(toDraw[:,0],toDraw[:,1], alpha=0.7)

ax1.set_xlabel('Time')
ax1.set_ylabel('Stable')
# set up the maximum and minimum for the whole graph?
plt.ylim(ymin=-0.2, ymax=1.2)
# plt.show()
PICADDRESS = os.path.join(*[PROJECTADDRESS, 'Pics'])
plt.savefig(os.path.join(PICADDRESS, 'Final.png'))