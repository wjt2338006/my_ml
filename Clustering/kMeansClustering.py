from random import random

from DataSet.BuildData import getRedWine
from DataSet.myDataSet import dataMake, regularData
from DistanceEvaluation import pearsonCorrelationScore

def average(dataList):
    # 应该传入一个列表，中有每一个数据项，数据项是key:value的字典
    # 算法计算相同key值得均值，如果数据不是整齐的，那么突出的项值会非常的小
    returnData = {}
    for i in dataList:
        for key,value in i.items():
            if key in returnData:
                returnData[key] += value
            else:
                returnData[key] = value
    for key,value in returnData.items():
        returnData[key] = returnData[key]/float(len(dataList))
    return returnData



def kcluster(dataSet,k):
    # 确定每一种特性的最大和最小值
    ranges = {}
    for i in dataSet.values():       #对于每一条记录
        for (key,value) in i.items():    #遍历每一个特性

            if key in ranges:   #已经有这个特性的最大最小值元组
                if ranges[key][0] > value:  #如果小于最小值
                    ranges[key] = (value, ranges[key][1])     #则指定新的最小值
                if ranges[key][1] < value:   #如果大于最大值
                    ranges[key] = (ranges[key][0], value)     #则指定新的最大值
            else:
                ranges[key] = (value, value)
    print(ranges)
    # 对于每一种特性，为其随机一个中间值，构成一个随机的对象,作为聚类的中心。重复k次
    centers = []
    for i in range(k):
        tmp = {}
        for key,value in ranges.items():
            tmp[key] = random()*(value[1] - value[0]) + value[0]
        centers.append(tmp)
        print(tmp)

    # 现在已经生成了k个中心，下面需要把每一个对象与k个中心比较距离，选择最相近来聚类
    lastMatched = None
    for i in range(1000):
        bestMatches = [[] for i in range(k)] #最佳匹配的数组，每个数组中存放本中心节点匹配的周围的子节点

        # 对于每一个对象
        for objKey,objValue in dataSet.items():
            # 设立一个最近的中心默认是0
            singleBestMatch = 0
            singleBestDistance = 1.0 - pearsonCorrelationScore(objValue,centers[singleBestMatch])
            # 遍历每一个中心，如果发现新的最近中心，就将值singleBestMatch替换
            for centerKey in range(k):
                re = pearsonCorrelationScore(objValue,centers[centerKey])
                d = 1.0 - re
                if d < singleBestDistance:
                    singleBestMatch = centerKey
            bestMatches[singleBestMatch].append(objKey)

        if bestMatches == lastMatched:break # 两次聚集的结果（对象）相同，则跳出
        else:lastMatched = bestMatches      # 否则用lastMatched缓存本次结果
        print("一轮聚集结果",bestMatches)
        #从新计算中心
        print("")
        for i in range(k):
            if len(bestMatches[i]) <=0 :continue

            dataList = [dataSet[j] for j in bestMatches[i]] #获取中心聚合所有对象列表
            centerAverageData = average(dataList) #传入算平局值

            print("新中心：",str(i)," = ",centerAverageData)

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
    print(kcluster(dataSet,3))



