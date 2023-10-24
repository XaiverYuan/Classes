import random
from typing import Callable,Dict
from tqdm import trange
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc("font",family='KaiTi')
from math import pi,e

class Coins:
    def __init__(self):
        self.data = []
        for i in range(200):
            self.data.append(random.random() > 0.5)
        assert len(self.data) == 200

    def q1(self) -> int:
        return sum(self.data)
    def q2(self)->int:
        maxV=1
        curr=1
        for i in range(1,200):
            if self.data[i]==self.data[i-1]:
                curr+=1
            else:
                maxV=max(maxV,curr)
                curr=1
        maxV=max(maxV,curr)
        return maxV

class Draw:
    def __init__(self):
        self.data:Dict[int,int]={}

    def addRecord(self,key:int):
        if key in self.data.keys():
            self.data[key]+=1
        else:
            self.data[key]=1
    def draw(self,func:Callable[[float],float]=None,xlabel:str=''):
        plt.bar(self.data.keys(),self.data.values(),label='实验结果')
        if func is not None:
            x=np.linspace(min(self.data.keys()),max(self.data.keys()),100)
            y=func(x)
            plt.plot(x,y,label='预期结果',color='red')
        plt.legend()
        plt.xlabel(xlabel)
        plt.ylabel('次数')
        plt.show()

def normalDistribution(mean:float,std:float,amplify:int)->Callable[[float],float]:
    c=1/((2*pi)**0.5*std)*amplify
    return lambda x:c*e**(-(x-mean)**2/2/std/std)

def generateQ1():
    table=Draw()
    for _ in trange(10000):
        table.addRecord(Coins().q1())
    table.draw(normalDistribution(100,50**0.5,10000),'和')
def generateQ2():
    table=Draw()
    for _ in trange(10000):
        table.addRecord(Coins().q2())
    table.draw(None,'最大连续数')
def theoryQ2():


if __name__ == '__main__':
    generateQ2()