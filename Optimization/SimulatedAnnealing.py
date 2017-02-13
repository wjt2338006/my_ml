from random import randint, random

import math

from DataSet.warehouseData import getWarehouseData
from Optimization.RandomSearch import correctResult


def calCost(dataSet,items):
    nowCost = 0.0
    nowScore = 0.0
    print(items)
    for j in range(len(dataSet)):
        nowCost += dataSet[j][items[j]]["售价"]
        nowScore += dataSet[j][items[j]]["品质"]
    result = nowCost/nowScore
    return result

def annealingOptimize(dataSet, T = 1000.0, cool = 0.7,step = 1):
    randItem = []

    for i in dataSet:
        randValue  = randint(0,len(i)-1)
        randItem.append(randValue)

    print(randItem)
    randCost = calCost(dataSet,randItem)
    while T > 0.1:
        i = randint(0,len(dataSet)-1)
        #print(i)
        change = randint(-step,step)
        items = randItem[:]
        items[i]+=change
        #print(items)
        if items[i] < 0:items[i] = 0
        if items[i] > len(dataSet[i])-1: items[i] = len(dataSet[i])-1


        changeCost = calCost(dataSet,items)

        #如果更优，或者随机到容忍更大的概率中
        if changeCost < randCost \
            or random() < pow(math.e, -(changeCost - randCost)/T):
            randItem = items
            randCost = changeCost
        T = T*cool
    print("退火算法最佳 ")
    print(randItem)
    print(randCost)
    return randItem

if __name__ == "__main__":
    dataSet = getWarehouseData()
    annealingOptimize(dataSet)
    #correctResult(dataSet)
