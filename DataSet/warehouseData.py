def getWarehouseData():
    #1品质 == 5.00售价
    #10-20 / 3-9 油漆 0.2 0.5 1.2 0.3
    data1 = [
                {
                    "售价":15.00,
                    "品质":3.2
                },

                {
                    "售价":25.000,
                    "品质":5.5,
                },
                 {
                    "售价":35.000,
                    "品质":8.2
                },
                {
                    "售价":45.00,
                    "品质":9.3
                }
            ]
    #0-18 /1-8 壁纸 0.1 0.3 0.7 0.2
    data2 = [

            {
                "售价":5.0,
                "品质":1.1
            },

                {
                    "售价":15.00,
                    "品质":3.3
                },

                {
                    "售价":30.00,
                    "品质":6.7,
                },

                {
                    "售价":40.00,
                    "品质":8.2
                }
            ]
    #18-72 / 5-16 地板 0.1 0.33 1.2 0.2
    data3 = [
            {
                "售价":25.0,
                "品质":5.1
            },

                {
                    "售价":50.00,
                    "品质":10.33,
                },

                {
                    "售价":65.00,
                    "品质":14.2
                },

                {
                    "售价":80.00,
                    "品质":16.2
                }
            ]
    #15-60 / 2-15 厨卫  0.3 0.4 2.0 0.1
    data4 = [
            {
                "售价":10.0,
                "品质":2.3
            },

                {
                    "售价":40.00,
                    "品质":8.4,
                },

                {
                    "售价":60.00,
                    "品质":14
                },

                {
                    "售价":75.00,
                    "品质":15.1
                }
            ]
    #30-120 / 10-25 家具 0 1 2 1
    data5 = [
            {
                "售价":55.0,
                "品质":11.00
            },

                {
                    "售价":95.00,
                    "品质":20.00,
                },

                {
                    "售价":115.00,
                    "品质":25
                },

                {
                    "售价":125.00,
                    "品质":26.00
                }
            ]
    #10-30 / 0-9  装饰 0  0.2  0.7  -1
    data6 = [{
                "售价":10.0,
                "品质":2.0
            },

                {
                    "售价":35.00,
                    "品质":7.2,
                },

                {
                    "售价":40.00,
                    "品质":8.7
                },

                {
                    "售价":50.00,
                    "品质":9.0
                }
            ]


    #10-30 / 0-9  家电 0  0.2  0.7  -1
    data7 = [{
                "售价":10.0,
                "品质":2.0
            },

                {
                    "售价":35.00,
                    "品质":7.2,
                },

                {
                    "售价":40.00,
                    "品质":8.7
                },

                {
                    "售价":50.00,
                    "品质":9.0
                }
            ]
    #10-30 / 0-9  灯饰  0  0.2  0.7  -1
    data8 = [{
                "售价":10.0,
                "品质":2.0
            },

                {
                    "售价":35.00,
                    "品质":7.2,
                },

                {
                    "售价":40.00,
                    "品质":8.7
                },

                {
                    "售价":50.00,
                    "品质":9.0
                }
            ]
    #10-30 / 0-9  其他 0  0.2  0.7  -1
    data9 = [{
                "售价":10.0,
                "品质":2.0
            },

                {
                    "售价":35.00,
                    "品质":7.2,
                },

                {
                    "售价":40.00,
                    "品质":8.7
                },

                {
                    "售价":50.00,
                    "品质":9.0
                }
            ]
    #return {"乳胶漆":data1,"壁纸":data2,"地板":data3,"厨卫":data4,"家具":data5,"装饰":data6}
    return [data1,data2,data3,data4,data5,data6,data7,data8,data9]
