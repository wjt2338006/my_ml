from random import random

from DataSet.BuildData import getRedWine
from DataSet.myDataSet import dataMake, regularData
from DistanceEvaluation import pearsonCorrelationScore


def average(dataList):
    # 应该传入一个列表，中有每一个数据项，数据项是key:value的字典
    # 算法计算相同key值得均值，如果数据不是整齐的，那么突出的项值会非常的小
    returnData = {}
    for i in dataList:
        for key, value in i.items():
            if key in returnData:
                returnData[key] += value
            else:
                returnData[key] = value
    for key, value in returnData.items():
        returnData[key] = returnData[key] / float(len(dataList))
    return returnData


def kcluster(dataSet, k):
    # 确定每一种特性的最大和最小值
    ranges = {}
    for i in dataSet.values():  # 对于每一条记录
        for (key, value) in i.items():  # 遍历每一个特性

            if key in ranges:  # 已经有这个特性的最大最小值元组
                if ranges[key][0] > value:  # 如果小于最小值
                    ranges[key] = (value, ranges[key][1])  # 则指定新的最小值
                if ranges[key][1] < value:  # 如果大于最大值
                    ranges[key] = (ranges[key][0], value)  # 则指定新的最大值
            else:
                ranges[key] = (value, value)
    print(ranges)
    # 对于每一种特性，为其随机一个中间值，构成一个随机的对象,作为聚类的中心。重复k次
    centers = []
    for i in range(k):
        tmp = {}
        for key, value in ranges.items():
            tmp[key] = random() * (value[1] - value[0]) + value[0]
        centers.append(tmp)
        print(tmp)

    # 现在已经生成了k个中心，下面需要把每一个对象与k个中心比较距离，选择最相近来聚类
    lastMatched = None  # 上次最佳匹配，用来比较是否有变化
    for i in range(1000):
        bestMatches = [[] for i in range(k)]  # 最佳匹配的数组，每个数组中存放本中心节点匹配的周围的子节点

        # 对于每一个对象
        for objKey, objValue in dataSet.items():
            # 设立一个最近的中心默认是0
            singleBestMatch = 0
            singleBestDistance = 1.0 - pearsonCorrelationScore(objValue, centers[singleBestMatch])
            # 遍历每一个中心，如果发现新的最近中心，就将值singleBestMatch替换
            for centerKey in range(k):
                re = pearsonCorrelationScore(objValue, centers[centerKey])
                d = 1.0 - re
                if d < singleBestDistance:
                    singleBestMatch = centerKey
                    singleBestDistance = d
            bestMatches[singleBestMatch].append((objKey, singleBestDistance))

        if bestMatches == lastMatched:
            break  # 两次聚集的结果（对象）相同，则跳出
        else:
            lastMatched = bestMatches  # 否则用lastMatched缓存本次结果
        print("一轮聚集结果", bestMatches)

        # 重新计算中心
        print("")
        for i in range(k):
            # 如果有空聚合，说明存在过度拟合
            if len(bestMatches[i]) <= 0:
                # 找到聚合项最多的集合
                maxLenCol = 0
                maxLenKey = 0
                for j in range(len(bestMatches)):
                    l = len(bestMatches[j])
                    if l > maxLenCol:
                        maxLenColKey = j
                        maxLenCol = l

                # 在这个聚合项最多的集合中找到距离最远的一个项
                maxDistanceKey = 0
                maxDistance = 0
                for j in bestMatches[maxLenColKey]:
                    if j[1] > maxDistance:
                        maxDistanceKey = j[0]
                        maxDistance = j[1]
                centers[i] = dataSet[maxDistanceKey]

                print("过度拟合修正，聚合%s为空，从聚合%s中抽出%s的值(距离为%s)作为其均值" % (
                str(i), str(maxLenKey), str(maxDistanceKey), str(maxDistance)))
            else:
                dataList = [dataSet[j[0]] for j in bestMatches[i]]  # 获取中心聚合所有对象列表
                centerAverageData = average(dataList)  # 传入算平局值

                print("新中心：", str(i), " = ", centerAverageData)

                centers[i] = centerAverageData
        print("")



    return bestMatches
if __name__ == '__main__':
    dataSet = regularData()#getRedWine("../DataSet/winequality-red.csv")
    '''for key,value in dataSet.items():
        print(key)
        for key2,value2 in value.items():
            print("+---",key2,"=",value2)
    '''
    data = kcluster(dataSet,3)
    print(data)



