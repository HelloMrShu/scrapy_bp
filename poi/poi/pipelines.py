# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from poi.db.dbhelper import DBHelper


class PoiPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.poiinsert(item)
        return item


class CityPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.cityinsert(item)
        return item


class CategoryPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        self.db.categoryinsert(item)
        return item

