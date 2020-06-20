# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangwuItem(scrapy.Item):
    # 房屋名称
    name = scrapy.Field()
    # 房屋id,方便房屋去重使用，唯一
    house_id = scrapy.Field()
    # 房屋来源
    source = scrapy.Field()
    # 房屋连接详情
    fangwu_src = scrapy.Field()

    address = scrapy.Field()
    # 所属区域
    district_name = scrapy.Field()
    city_name = scrapy.Field()
    # 距离优势，比如近西客站
    distance_tip = scrapy.Field()
    # 比如距离西客站直线2.3公里
    unit_infor = scrapy.Field()
    price = scrapy.Field()
    #经纬度
    longitude = scrapy.Field()
    latitude = scrapy.Field()


    # 从详情页面获取
    # 收藏人数
    favorite_count = scrapy.Field()
    # 出租类型
    house_type = scrapy.Field()

    # 几室几厅
    house_jishi = scrapy.Field()
    #房屋面积
    house_mianji = scrapy.Field()
    # 最多居住人数
    house_ren_count = scrapy.Field()
    # 房屋介绍
    # house_introduction = scrapy.Field()

    # 评论数量
    comment_count = scrapy.Field()
    # 总评分
    overall = scrapy.Field()
    # 卫生评分
    cleanliness = scrapy.Field()
    # 位置评分
    traffic= scrapy.Field()
    # 服务评分
    services= scrapy.Field()
    # 装修评分
    house_decoration= scrapy.Field()
    # 入住时间
    house_in = scrapy.Field()
    # 退房时间
    house_out = scrapy.Field()


    # 房东介绍
    #房东id
    fangdong_id = scrapy.Field()
    fangdong_tel = scrapy.Field()
    # 房东类型，是个人房东，企业房东，自营等
    fangdong_tags = scrapy.Field()
    #房东有几套房子
    fangdong_house_count = scrapy.Field()

    fangdong_nick_name = scrapy.Field()



