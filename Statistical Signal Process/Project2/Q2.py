from Initialize import *
from typing import Callable
import torch


class Q2Answer:
    def __init__(self, TxFunction: Callable[[torch.Tensor], torch.Tensor]):
        self.function = TxFunction

    def drawTx(self):
        trainingTx = self.function(trainingData)
