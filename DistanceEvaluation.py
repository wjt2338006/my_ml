from math import sqrt

from DataSet.BuildData import getRedWine


def euclideanDistanceScore(obj1 ,obj2):
    """
    参数说明：
    :rtype: scope 归一化的相似度，越相近越接近1
    :param obj1:    对象1，应该是个字典
    :param obj2:    对象2，应该是个字典

    需要传入的项应该是一个字典，其中第一维度是对象，第二维度是特性
    传入两个对象名
    这里以电影评分举例
    有一个用户对电影评分的数据集dataSet
    {}
    |-"user_name_1"
        |- "The Lord of the Rings" = 5
        |- "Warcraft"  = 4
    |-"user_name_2"
        |- "The Lord of the Rings" = 6
        |- "Warcraft"  = 9
    | ......

    如果比较用户一和用户二的相似度，应该传入dataSet["user_name_1"] = "user_name_1" ,dataSet["user_name_2"]  = "user_name_2"
    """
    # 寻找出两个用户的共同评分
    coRating = []

    # 找出相同的项
    for key, value in obj1.items():
        if key in obj2:
            coRating.append(key)

    # 如果没有共同评分，则没有相似度
    if len(coRating) == 0:
        return 0.0

    # 计算所有差值的平方，就是两点在几何空间的距离
    differenceValueList = [pow(float(obj1[item]) - float(obj2[item]), 2) for item in coRating]
    print(differenceValueList)
    #求和
    sumSquares = sum(differenceValueList)

    # 开平方，归一化
    return 1/(1+sqrt(sumSquares))

def pearsonCorrelationScore(obj1,obj2):
    # 寻找出两个用户的共同评分
    coRating = []


    # 找出相同的项
    for key, value in obj1.items():
        if key in obj2:
            coRating.append(key)

    # 如果没有共同评分，则没有相似度
    if len(coRating) == 0:
        return 0
    sum1 = sum([float(obj1[i]) for i in coRating])
    sum2 = sum([float(obj2[i]) for i in coRating])

    sum1Sq = sum([pow(float(obj1[key]), 2) for key in coRating])
    sum2Sq = sum([pow(float(obj2[key]), 2) for key in coRating])

    pSum = sum([float(obj1[key]) * float(obj2[key]) for key in coRating])

    #皮尔逊评价度公式
    n = float(len(coRating))

    num = pSum - (sum1 * sum2/n)
    den = sqrt((sum1Sq - pow(sum1, 2)/n) * (sum2Sq - pow(sum2, 2)/n))
    if den == 0:
        return 0
    r = num/den
    return r



if __name__ == "__main__":
    dataSet = getRedWine()

    result1 = euclideanDistanceScore(dataSet["2"], dataSet["3"])
    result2 = pearsonCorrelationScore(dataSet["2"], dataSet["3"])
    print(result1)
    print(result2)