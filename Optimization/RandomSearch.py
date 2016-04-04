from random import randint

from DataSet.warehouseData import getWarehouseData


def randomSearch(dataSet):


    bestFS = 99999.0
    bestItem = {}
    for i in range(5000):
        projectItem = []
        score = 0.0
        fee = 0.0
        for i in dataSet:
            randValue = randint(0, len(i)-1)
            projectItem.append(randValue)
            fee += i[randValue]["售价"]
            score += i[randValue]["品质"]
        result = fee/score
        if result < bestFS:
            bestItem = projectItem
            bestFS = result
            print("发现更优解：",bestFS," -|- ",projectItem)

    print("最佳匹配：",bestItem)
    print("每一分品质价格：",bestFS)
def correctResult(dataSet):
    colMaxCalTime = [len(i) for i in dataSet]

    #递归每一列函数
    def rowCal(list,lastItems,rowNumber,colMaxCalTimeList):
        if rowNumber == 0:
            list.append(lastItems)
            return

        nowRow = len(colMaxCalTimeList)-rowNumber
        colMaxCalTime = colMaxCalTimeList[nowRow]
        for i in range(colMaxCalTime):
            items = lastItems[:]
            items.append(i)
            rowCal(list,items,rowNumber-1,colMaxCalTimeList)


    bestPro = []
    bestFS = 900000
    allList = []
    rowCal(allList,[],len(colMaxCalTime),colMaxCalTime)

    for i in allList:
        scope = 0
        fee = 0
        for j in range(len(i)):
            fee += dataSet[j][i[j]]["售价"]
            scope += dataSet[j][i[j]]["品质"]
        if fee/scope < bestFS:
            bestFS = fee/scope
            bestPro = i
    #print(allList)
    #print(len(allList))
    print(bestFS)
    print(bestPro)



if __name__ == "__main__":
    dataSet = getWarehouseData()
    randomSearch(dataSet)
    correctResult(dataSet)
