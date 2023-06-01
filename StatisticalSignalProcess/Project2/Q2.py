from Initialize import *
from typing import Callable
import torch
import matplotlib.pyplot as plt


class Q2Answer:
    def __init__(self, TxFunction: Callable[[torch.Tensor], torch.Tensor]):
        self.function = TxFunction

    def drawTx(self):
        trainingTx = self.function(trainingData)
        fig = plt.figure()
        # add a subplot
        ax1 = fig.add_subplot(1, 1, 1)
        # set the title
        ax1.set_title('')
        # plot the data as points
        ax1.plot(x, y)
        ax1.set_xlabel(xaxis)
        ax1.set_ylabel(yaxis)
        # set up the maximum and minimum for the whole graph?
        plt.ylim(ymin=minmax[0], ymax=minmax[1])
