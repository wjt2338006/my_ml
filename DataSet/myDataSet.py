from random import random


def dataMake():
    data = {}
    keys = ["魔兽世界","全面战争","死亡空间","GTA5","猎魔人3","刺客信条诸代记"]
    mans = ["Tom","Rio","Angular","Mosta","Helson","Lion","Nuse"]
    for j in mans:
        data[j] = {}
        for i in keys:

            data[j][i] = random()*10.00
    return data

def regularData():
    return {
        "魔幻1，讨厌日系":{
            "魔兽世界":9,
            "指环王":8,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":8,
            "光环":1,
            "星球大战":3
        },
         "魔幻2,讨厌枪战":{
            "魔兽世界":8,
            "指环王":10,
            "最终幻想":0,
            "生化危机":1,
            "上古卷轴":8,
            "光环":0,
            "星球大战":0
        },
         "魔幻3，讨厌日系":{
            "魔兽世界":10,
            "指环王":8,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":8,
            "光环":2,
            "星球大战":3
        },
         "魔幻4，讨厌日系":{
            "魔兽世界":9,
            "指环王":8,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":10,
            "光环":2,
            "星球大战":1
        },
         "魔幻5，讨厌日系":{
            "魔兽世界":10,
            "指环王":8,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":8,
            "光环":2,
            "星球大战":2
        },
         "魔幻6，讨厌日系":{
            "魔兽世界":10,
            "指环王":10,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":8,
            "光环":2,
            "星球大战":2
        },
         "魔幻7,其余的还好":{
            "魔兽世界":9,
            "指环王":9,
            "最终幻想":2,
            "生化危机":2,
            "上古卷轴":9,
            "光环":3,
            "星球大战":3
        },
         "日系1,其余的还好":{
            "魔兽世界":3,
            "指环王":3,
            "最终幻想":9,
            "生化危机":9,
            "上古卷轴":3,
            "光环":3,
            "星球大战":3
        },
         "日系2,娘炮讨厌魔幻":{
            "魔兽世界":0,
            "指环王":1,
            "最终幻想":10,
            "生化危机":9,
            "上古卷轴":0,
            "光环":0,
            "星球大战":0
        },
         "日系3,娘炮讨厌魔幻":{
            "魔兽世界":0,
            "指环王":1,
            "最终幻想":9,
            "生化危机":9,
            "上古卷轴":0,
            "光环":0,
            "星球大战":0
        },
        "日系4,娘炮讨厌魔幻":{
            "魔兽世界":0,
            "指环王":0,
            "最终幻想":10,
            "生化危机":9,
            "上古卷轴":0,
            "光环":0,
            "星球大战":0
        },
        "日系5,娘炮讨厌魔幻":{
            "魔兽世界":0,
            "指环王":0,
            "最终幻想":9,
            "生化危机":9,
            "上古卷轴":0,
            "光环":0,
            "星球大战":0
        },
        "枪战1,讨厌日系":{
            "魔兽世界":2,
            "指环王":3,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":2,
            "光环":9,
            "星球大战":9
        }, "枪战2,讨厌日系":{
            "魔兽世界":2,
            "指环王":3,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":2,
            "光环":10,
            "星球大战":9
        },
         "枪战3,讨厌日系":{
            "魔兽世界":3,
            "指环王":3,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":2,
            "光环":9,
            "星球大战":10
        },
         "枪战4,讨厌日系":{
            "魔兽世界":3,
            "指环王":3,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":3,
            "光环":10,
            "星球大战":9
        },
         "枪战5,讨厌日系":{
            "魔兽世界":2,
            "指环王":3,
            "最终幻想":0,
            "生化危机":0,
            "上古卷轴":3,
            "光环":10,
            "星球大战":9
        },
        "枪战6,爱魔幻":{
            "魔兽世界":5,
            "指环王":4,
            "最终幻想":1,
            "生化危机":2,
            "上古卷轴":5,
            "光环":9,
            "星球大战":9
        }

    }