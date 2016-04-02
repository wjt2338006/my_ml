import csv
def getRedWine(path = "./DataSet/winequality-red.csv"):
    file = open(path, "r")
    dataSet = csv.reader(file)

    returnData = {}
    keys = []


    count = 0
    for i in dataSet:
        #print(i)
        if count == 0:
            i = i[0].split(";")
            for key in i:
                keys.append(key)
        else:
            single = {}
            j = 0
            i = i[0].split(";")
            while j < len(keys):
                single[keys[j]] = i[j]
                j += 1

            returnData[str(count)] = single

        count += 1
        if count > 30:break
    return returnData
    '''
    print(returnData)
    print(count)'''