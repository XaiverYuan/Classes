from typing import List


def print2dArray(data):
    for x in range(len(data[0])):
        for y in range(len(data)):
            print("%3d" % data[x][y], end='')
        print()


countTable = []
for i in range(11):
    countTable.append([])
    for j in range(11):
        countTable[i].append(-1)
for i in range(1, 11):
    countTable[1][i] = 2
countTable[1][1] = 1
countTable[0] = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(11):
    countTable[i][0] = i
countTable[0][0] = -1

def anyUpTo(slots:int,maxCont:int=1000000):
    if maxCont>slots:
        maxCont=slots
    ans=0
    for x in range(1,maxCont):
        ans+=countTable[x][slots]
    return ans

def cal(x, y):
    if y==x:
        return 2
    if y - x == 1:
        return 4
    if y - x == 2:
        return 10
    answer = 0
    answer += anyUpTo(y-x-1) * 2  # 0001??????*2
    answer += anyUpTo(y-x-2)  * 2  # 10001?????*2
    for startPosition in range(2,y-x-1):
        leftCombination=anyUpTo(startPosition-1,x)
        rightCombination=anyUpTo(y-startPosition-x-1,x)
        answer+=leftCombination*rightCombination*2
    countTable[x][y]=answer
for y in range(2,6):
    for x in range(y,6):
        cal(x,y)


print2dArray(countTable)
