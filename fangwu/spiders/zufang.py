# -*- coding: utf-8 -*-
import scrapy
import json
from ..tujia_config import  *
from fangwu.items import FangwuItem
import logging

import pandas as pd
import numpy as np


class MyjobSpider(scrapy.Spider):

    # 1-58
    # 352-382

    name = 'tujia'
    allowed_domains = ['mpclient.tujia.com','m.tujia.com']
    page_index = 352
    page_size = 20
    house_id_list = []

    formdata = {
        "pageIndex": page_index,
        "pageSize": page_size,
        "conditions": [{
            "label": "济南",
            "type": 1,
            "value": "19",
            "hotRecommend": None,
            "pingYin": "jinan",
            "longitude": 117.12699890136719,
            "latitude": 36.65729904174805,
            "conditionType": -1,
            "redPoint": False,
            "selectedType": 0,
            "scope": 0,
            "pinYin": "jinan",
            "gType": 0
        }, {
            "label": "离店日期",
            "type": 3,
            "value": "2020-08-18",
            "hotRecommend": None,
            "longitude": 0,
            "latitude": 0,
            "conditionType": -1,
            "redPoint": False,
            "selectedType": 0,
            "scope": 0,
            "gType": 0
        }, {
            "label": "入住日期",
            "type": 2,
            "value": "2020-08-17",
            "hotRecommend": None,
            "longitude": 0,
            "latitude": 0,
            "conditionType": -1,
            "redPoint": False,
            "selectedType": 0,
            "scope": 0,
            "gType": 0
        }, {
            "label": "推荐排序",
            "type": 4,
            "value": "1",
            "hotRecommend": None,
            "longitude": 0,
            "latitude": 0,
            "conditionType": -1,
            "redPoint": False,
            "selectedType": 0,
            "scope": 0,
            "gType": 4,
            "selected": True
        }],
        "returnFilterConditions": False,
        "returnGeoConditions": False
    }

    def start_requests(self):
        try:
            csv = pd.read_csv('info.csv', usecols=[14], header=None)
            nparr = np.array(csv.stack())
            self.house_id_list = nparr.tolist()[1:]


        except:
            pass

        yield  scrapy.FormRequest(
            url=tujia_url,
            method="POST",
            headers = tujia_header,
            body =json.dumps(self.formdata),
            callback=self.parse,
            dont_filter=True,
            # meta={'proxy': proxyMeta}
        )




    def parse(self, response):

        try:

            item_list = json.loads(response.text).get("data").get('items')
            if(not item_list):
                logging.warning('=' * 100)
                logging.warning('item_list---请求列表失败' + str(self.page_index))
                logging.warning(response.text)

                return

            if(len(item_list)>0):
                for item in item_list:
                   # 1，使用全局列表保存，如果出现意外再保存在在本地存储一下id，进行比对去重。
                    house_id = str(item.get('unitId'))

                    if(house_id not in self.house_id_list):
                        self.house_id_list.append(house_id)
                        fangwu = FangwuItem()
                        fangwu["house_id"] = house_id
                        fangwu["name"] = item.get("unitName") if item.get("unitName") else ''
                        fangwu["source"] = "tujia"
                        fangwu["address"] = item.get("address") if item.get("address") else ''
                        fangwu["district_name"] = item.get("districtName") if item.get("districtName") else ''
                        fangwu["city_name"] = item.get("cityName")
                        fangwu["distance_tip"] = item.get("distanceTip") if item.get("distanceTip") else ''
                        fangwu["unit_infor"] = item.get("unitInfor") if item.get("unitInfor") else ''
                        fangwu["price"] = item.get("finalPrice") if item.get("finalPrice") else ''
                        fangwu["longitude"] = item.get("longitude") if item.get("longitude") else ''
                        fangwu["latitude"] = item.get("latitude") if item.get("latitude") else ''
                        fangwu["fangwu_src"] = 'https://www.tujia.com/detail/'+house_id+'.htm'

                        # print(fangwu)
                        tujia_detail_formdata = {
                            # "houseId": "11052679",
                            "houseId": house_id,
                            "preview": False
                        }
    #                     爬取详情页面
                        yield scrapy.Request(
                                    url=tujia_detail_url,
                                    headers=tujia_detail_header,
                                    method="POST",
                                    body=json.dumps(tujia_detail_formdata),
                                    callback=self.parse_detail,
                                    meta={'item': fangwu},
                                    # meta={'item': fangwu},
                                    dont_filter=True
                                )
                        # break
                    else:
                        print(str(house_id)+'已存在')
            #         请求下一页
                self.page_index += 1
                print('******************************************')
                self.formdata["pageIndex"] = self.page_index
                print(self.formdata.get("pageIndex"))
                # if(self.page_index>2):
                #     return
                yield scrapy.FormRequest(
                    url=tujia_url,
                    headers=tujia_header,
                    body=json.dumps(self.formdata),
                    callback=self.parse,
                    dont_filter=True,
                    meta={"now_index":self.page_index}
                )
            else:
                # 没有数据了
                print(response.text)
        except :
            pass






    def parse_detail(self,response):
        item = response.meta['item']

        detail = json.loads(response.text).get("data")
        item["favorite_count"] = detail.get("favoriteCount") if detail.get("favoriteCount") else ''

        houseSummarys = detail.get("houseSummarys")
        if(len(houseSummarys)>3):
            item["house_type"] = houseSummarys[0].get("title")
            item["house_jishi"] = houseSummarys[1].get("title")
            item["house_mianji"] = houseSummarys[2].get("title")
            item["house_ren_count"] = houseSummarys[3].get("title")

        landlordInfo = detail.get("landlordInfo")
        if(landlordInfo):
            item["fangdong_id"] = landlordInfo.get("hotelId")
            item["fangdong_tel"] = landlordInfo.get("encryptContactPhone") if landlordInfo.get("encryptContactPhone") else ''
            item["fangdong_nick_name"] = landlordInfo.get("hotelName")
            hotelTags = landlordInfo.get("hotelTags")
            # print(hotelTags)
            tags = ''
            for hotel_tag in hotelTags:
                tags += hotel_tag.get("text")+','
            if(',' in tags):
                item["fangdong_tags"] = tags[:-1]
            else:
                item["fangdong_tags"] =''


        houseCommentSummary = detail.get("houseCommentSummary")
        if(houseSummarys):
            item["comment_count"]=houseCommentSummary.get("totalCount")
            item["overall"] = houseCommentSummary.get("overall")
            item["cleanliness"] = houseCommentSummary.get("cleanliness")
            item["traffic"] = houseCommentSummary.get("traffic")
            item["services"] = houseCommentSummary.get("services")
            item["house_decoration"] = houseCommentSummary.get("houseDecoration")


        # 入住时间和退房时间
        checkInRules = detail.get("checkInRules")
        # print(checkInRules)
        if(len(checkInRules)>1 and checkInRules[0].get("title")=="入住时间" and checkInRules[1].get("title")=="退房时间"):
            if(checkInRules[0].get("items")):
                item["house_in"] = checkInRules[0].get("items")[0].get("introduction")
            if (checkInRules[1].get("items")):
                item["house_out"] = checkInRules[1].get("items")[0].get("introduction")

        yield item








