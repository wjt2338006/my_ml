from DataSet.BuildData import getRedWine
from DistanceEvaluation import pearsonCorrelationScore

def printTree(node,prefix="|"):
    prefix+="--"
    if node.key!=None:
        print(prefix+"叶节点"+str(node.id)+"|叶Key "+str(node.key)+str(node.data))

    else:
        print(prefix+"枝干子距离："+str(node.distance))

    if node.left!=None:
        printTree(node.left,prefix)
    if node.right!=None:
        printTree(node.right,prefix)
    return


class node:
    def __init__(self, key=None, data =None ,left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.key = key
        self.data = data
        self.id = id
        self.distance = distance

# 距离计算缓存器
class DistanceManage:
    def __init__(self):
        self.distanceCollection = {}
    def getDistance(self,i,j):
        #print("")
        #print("")
        if (i.id, j.id) in self.distanceCollection:
            #print("已有的距离")
            #print(self.distanceCollection[(i.id,j.id)])
            return self.distanceCollection[(i.id,j.id)]
        else:
            #print(i.data)
            #print(j.data)
            result = 1.0 - pearsonCorrelationScore(i.data, j.data)
            if result <= 0.0: result = 0.0
            #print(result)

            self.distanceCollection[(i.id,j.id)] = result
            return self.distanceCollection[(i.id,j.id)]

# 平均值
def average(obj1,obj2):
    returnData = {}
    for key in obj1.keys():
        if key in obj2.keys():
            returnData[key] = (float(obj2[key]) + float(obj1[key]))/2.0

    return returnData

# 分级聚类
def hierarchicalClustering(dataSet):
    count = 0
    cluster = []
    distanceColletion = {}

    for (key, value) in dataSet.items():
        cluster.append(node(key, value, id = count))
        count += 1


    distance = DistanceManage()
    #lastClosestPair  = (cluster[0],cluster[1])
    while len(cluster) > 1:
        print(count)

        closestPair = (cluster[0],cluster[1])
        closestDisitance = distance.getDistance(closestPair[0], closestPair[1])

        for i in cluster:
            for j in cluster:
                if i == j:
                    continue

                d = distance.getDistance(i,j)
                # 如果相关距离更加短
                if d < closestDisitance:
                    print(i.id,"==|==",j.id)
                    print("@@@@@@@@@@发现更短距离：",d,"@@@@@@@@@@@原来距离",closestDisitance)
                    closestDisitance = d
                    closestPair = (i, j)


        averageClosePair = average(closestPair[0].data,closestPair[1].data)

        newNode = node(data = averageClosePair,left = closestPair[0], right = closestPair[1] ,distance = closestDisitance, id = count)
        cluster.append(newNode)
        count += 1
        cluster.remove(closestPair[0])
        cluster.remove(closestPair[1])

        '''if lastClosestPair[0] in closestPair:
            lastClosestPair = (cluster[0], lastClosestPair[1])
        if lastClosestPair[1] in closestPair:
            lastClosestPair = (lastClosestPair[1],cluster[0] )'''





    return cluster[0]
# 测试函数
if __name__ == "__main__":
    dataSet = getRedWine("../DataSet/winequality-red.csv")
    print(dataSet)
    #hierarchicalClustering(dataSet)
    printTree(hierarchicalClustering(dataSet))