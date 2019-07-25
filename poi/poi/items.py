# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# poi数据字段定义
class PoiItem(scrapy.Item):
    name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    code = scrapy.Field()
    phone_no = scrapy.Field()
    region = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()


# 城市数据字段定义
class CityItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()


# 类别数据字段定义
class CategoryItem(scrapy.Item):
    name = scrapy.Field()

