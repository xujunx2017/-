#coding=utf-8

data = {
    "server_ip_port":["http://10.0.4.147","8080"],
    "topic":"MQ_TOPIC_KAFKA_PROFILE_SYSTEM",	
	#"siteNo_All":"",
    "item":{#01.黑名单获取
            "parms":{
    "dataSource":"001",
    "dataType":"jiguang",
    "bizType":"basetag",
    "userIp":"10.10.10.10",
    "collectTime":"1504680004",
    "sessionId":"1434564455445",
    "data":{
        "id_card":"110000000000000015",
        "phone_no":"13000000008",
        "name":"周海松",
        "request":"",
        "flag":"S",
        "code":"200",
        "flowNo":"deefea7220bc4855938778dfb23420ce",
        "msg":"请求成功",
        "response":{
            "req_id":"bugAJjidgLVR3",
            "code":2000,
            "data":{
                "CID_JID":"3664580822b351e98c966f0d0e6f358",
                "CPL_HHM_CHILD_HC":"有",
                "CPL_INDM_GEND_S":{
                    "value":"M",
                    "score":0.06
                },
                "CPL_INDM_MARRC2":"已婚",
                "CPL_INDM_NATI":"中国",
                "CPL_INDM_AGE_C5":{
                    "score":0.248,
                    "value":"3"
                },
                "CPL_HHM_CHILD_CHLI":"婴幼儿",
                "CID_MODEL":"Letv X500",
                "CPL_DVM_BRAD":"Letv",
                "CPL_DVM_HF":[
                    {
                        "name":"cpu数",
                        "value":"未知"
                    },
                    {
                        "name":"cpu型号",
                        "value":"AArch64Processorrev4(aarch64)"
                    }
                ],
                "CPL_DVM_ISP":"中国移动",
                "CPL_DVM_OS":"Andriod",
                "CPL_DVM_PUPR":"1000",
                "CPL_DVM_RESO":"1920*1080",
                "CPL_DVM_SCSIZE":"5.5英寸",
                "CPL_DVM_TIME":"2016年06月",
                "CPL_DVM_TYPE":"手机",
                "CPL_INDM_VEIC_VEID":"Y",
                "FIM_FISM_CONL_CIR":{
                    "value":"高",
                    "score":50
                },
                "FIM_FISM_INCL":{
                    "value":"高",
                    "score":50
                },
                "GBM_BHM_PURB_CONP":[
                    "服装",
                    "化妆品"
                ],
                "GBM_BHM_PURB_PREF":[
                    {
                        "name":"潮流",
                        "value":0.015
                    },
                    {
                        "name":"大众",
                        "value":0.985
                    }
                ],
                "SOM_OCM_CAREER":"白领",
                "GBM_HBM_S":[
                    {
                        "name":"购物狂",
                        "value":6
                    },
                    {
                        "name":"社交达人",
                        "value":5
                    }
                ],
                "GBM_BHM_APPP_APPR_S":[
                    {
                        "name":"综合新闻",
                        "value":1
                    },
                    {
                        "name":"投资",
                        "value":1
                    }
                ],
                "GBM_BHM_PURB_PURW":[
                    {
                        "name":"导购",
                        "value":0.25
                    },
                    {
                        "name":"团购",
                        "value":0.25
                    }
                ],
                "GBM_BHM_PURB_SUPR":[
                    "打⻋租⻋",
                    "订酒店",
                    "购物"
                ],
                "GBM_BHM_REAB_REAP":[
                    "交规学习",
                    "健身攻略"
                ],
                "APP_HOBY_BUS":{
                    "value":"公交",
                    "score":0.5
                },
                "APP_HOBY_TICKET":{
                    "value":"票务",
                    "score":0.5
                },
                "APP_HOBY_TRAIN":{
                    "value":"火车高铁",
                    "score":0.5
                },
                "APP_HOBY_FLIGHT":{
                    "value":"飞机",
                    "score":0.5
                },
                "APP_HOBY_TAXI":{
                    "value":"打车",
                    "score":0.5
                },
                "APP_HOBY_SPECIAL_DRIVE":{
                    "value":"专车",
                    "score":0.5
                },
                "APP_HOBY_HIGH_BUS":{
                    "value":"大巴",
                    "score":0.5
                },
                "APP_HOBY_OTHER_DRIVE":{
                    "value":"代驾",
                    "score":0.5
                },
                "APP_HOBY_RENT_CAR":{
                    "value":"租车",
                    "score":0.5
                },
                "APP_HOBY_STARS_HOTEL":{
                    "value":"星级酒店",
                    "score":0.5
                },
                "APP_HOBY_YOUNG_HOTEL":{
                    "value":"青年旅馆",
                    "score":0.5
                },
                "APP_HOBY_HOME_HOTEL":{
                    "value":"住宿",
                    "score":0.5
                },
                "APP_HOBY_CONVERT_HOTEL":{
                    "value":"快捷酒店",
                    "score":0.5
                },
                "APP_HOBY_BANK_UNIN":{
                    "value":"银联支付",
                    "score":0.5
                },
                "APP_HOBY_ALIPAY":{
                    "value":"支付宝支付",
                    "score":0.5
                },
                "APP_HOBY_THIRD_PAY":{
                    "value":"其他第三方支付",
                    "score":0.5
                },
                "APP_HOBY_INTERNET_BANK":{
                    "value":"网络银行",
                    "score":0.5
                },
                "APP_HOBY_FOREIGN_BANK":{
                    "value":"外资银行",
                    "score":0.5
                },
                "APP_HOBY_MIDDLE_BANK":{
                    "value":"股份制银行",
                    "score":0.5
                },
                "APP_HOBY_CREDIT_CARD":{
                    "value":"信用卡",
                    "score":0.5
                },
                "APP_HOBY_CITY_BANK":{
                    "value":"城市银行",
                    "score":0.5
                },
                "APP_HOBY_STATE_BANK":{
                    "value":"国有银行",
                    "score":0.5
                },
                "APP_HOBY_FUTURES":{
                    "value":"期货",
                    "score":0.5
                },
                "APP_HOBY_VIRTUAL_CURRENCY":{
                    "value":"虚拟货币",
                    "score":0.5
                },
                "APP_HOBY_FOREX":{
                    "value":"外汇",
                    "score":0.5
                },
                "APP_HOBY_NOBLE_METAL":{
                    "value":"贵金属",
                    "score":0.5
                },
                "APP_HOBY_FUND":{
                    "value":"基金",
                    "score":0.5
                },
                "APP_HOBY_COLLECTION":{
                    "value":"收藏品",
                    "score":0.5
                },
                "APP_HOBY_STOCK":{
                    "value":"股票",
                    "score":0.5
                },
                "APP_HOBY_ZONGHELICAI":{
                    "value":"综合理财",
                    "score":0.5
                },
                "APP_HOBY_CAR_LOAN":{
                    "value":"⻋贷",
                    "score":0.5
                },
                "APP_HOBY_DIVIDE_LOAN":{
                    "value":"分期贷",
                    "score":0.5
                },
                "APP_HOBY_STUDENT_LOAN":{
                    "value":"学生贷",
                    "score":0.5
                },
                "APP_HOBY_CREDIT_CARD_LOAN":{
                    "value":"信用卡贷",
                    "score":0.5
                },
                "APP_HOBY_CASH_LOAN":{
                    "value":"现金贷",
                    "score":0.5
                },
                "APP_HOBY_HOUSE_LOAN":{
                    "value":"房贷",
                    "score":0.5
                },
                "APP_HOBY_P2P":{
                    "value":"P2P",
                    "score":0.5
                },
                "APP_HOBY_LOAN_PLATFORM":{
                    "value":"综合贷款平台",
                    "score":0.5
                },
                "APP_HOBY_SPORT_LOTTERY":{
                    "value":"体彩",
                    "score":0.5
                },
                "APP_HOBY_WELFARE_LOTTERY":{
                    "value":"福利彩票",
                    "score":0.5
                },
                "APP_HOBY_DOUBLE_BALL":{
                    "value":"双色球",
                    "score":0.5
                },
                "APP_HOBY_LOTTERY":{
                    "value":"综合彩票平台",
                    "score":0.5
                },
                "APP_HOBY_FOOTBALL_LOTTERY":{
                    "value":"二次元",
                    "score":0.5
                },
                "APP_HOBY_STRANGER_SOCIAL":{
                    "value":"陌生人社交",
                    "score":0.5
                },
                "APP_HOBY_ANONYMOUS_SOCIAL":{
                    "value":"匿名社交",
                    "score":0.5
                },
                "APP_HOBY_CITY_SOCIAL":{
                    "value":"同城交友",
                    "score":0.5
                },
                "APP_HOBY_FANS":{
                    "value":"追星一族",
                    "score":0.5
                },
                "APP_HOBY_FIN":{
                    "value":"金融教育",
                    "score":0.5
                },
                "APP_HOBY_MIDDLE":{
                    "value":"中学教育",
                    "score":0.5
                },
                "APP_HOBY_IT":{
                    "value":"IT教育",
                    "score":0.5
                },
                "APP_HOBY_PRIMARY":{
                    "value":"小学教育",
                    "score":0.5
                },
                "APP_HOBY_BABY":{
                    "value":"胎儿教育",
                    "score":0.5
                },
                "APP_HOBY_ONLINE_STUDY":{
                    "value":"在线教育",
                    "score":0.5
                },
                "APP_HOBY_FOREIGN":{
                    "value":"外语学习",
                    "score":0.5
                },
                "APP_HOBY_DRIVE":{
                    "value":"驾考学习",
                    "score":0.5
                },
                "APP_HOBY_SERVANTS":{
                    "value":"公务员考试",
                    "score":0.5
                },
                "APP_HOBY_CHILD_EDU":{
                    "value":"儿童教育",
                    "score":0.5
                },
                "APP_HOBY_UNIVERSITY":{
                    "value":"大学教育",
                    "score":0.5
                },
                "APP_HOBY_CAR_SHOPPING":{
                    "value":"汽⻋专卖",
                    "score":0.5
                },
                "APP_HOBY_SECONDHAND_SHOPPING":{
                    "value":"二手闲置",
                    "score":0.5
                },
                "APP_HOBY_ZONGHE_SHOPPING":{
                    "value":"综合购物",
                    "score":0.5
                },
                "APP_HOBY_PAYBACK":{
                    "value":"优惠",
                    "score":0.5
                },
                "APP_HOBY_MARK_SIX":{
                    "score":77.777,
                    "value":"六合彩"
                },
                "APP_HOBY_CAR_PRO":{
                    "score":88.8888,
                    "value":"汽车养护"
                },
                "APP_HOBY_CONCEIVE":{
                    "score":99.999,
                    "value":"孕育指导"
                },
                "APP_HOBY_MAMA_SOCIAL":{
                    "score":12.12,
                    "value":"妈妈社区"
                },
                "APP_HOBY_DISCOUNT_MARKET":{
                    "value":"品牌折扣",
                    "score":0.5
                },
                "APP_HOBY_BABY_SHOPPING":{
                    "value":"母婴专卖",
                    "score":0.5
                },
                "APP_HOBY_WOMEN_SHOPPING":{
                    "value":"女性购物",
                    "score":0.5
                },
                "APP_HOBY_REBATE_SHOPPING":{
                    "value":"返利",
                    "score":0.5
                },
                "APP_HOBY_GROUP_BUY":{
                    "value":"团购",
                    "score":0.5
                },
                "APP_HOBY_GLOBAL_SHOPPING":{
                    "value":"海淘",
                    "score":0.5
                },
                "APP_HOBY_SHOPPING_GUIDE":{
                    "value":"导购资讯",
                    "score":0.5
                },
                "APP_HOBY_SEX_SHOPPING":{
                    "value":"情趣专卖",
                    "score":0.5
                },
                "APP_HOBY_SMOTE_OFFICE":{
                    "value":"移动办公",
                    "score":0.5
                },
                "CPL_INDM_EDU_LEVEL":"1",
                "CPL_INDM_UNDERG":{
                    "score":99.011,
                    "value":"1"
                }
            },
            "message":"success"
        }
    }
}},
    "end":"end"
}



