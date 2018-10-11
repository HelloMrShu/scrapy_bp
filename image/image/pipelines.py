# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from image.db.dbhelper import DBHelper

class ImagePipeline(object):
	def __init__(self):
		#self.file = open('data.json', 'wb')
		self.db = DBHelper()

	def process_item(self, item, spider):
		#存文件
		#line = json.dumps(dict(item)) + "\n"
		#self.file.write(line.encode())

		#存数据库试试
		self.db.insert(item)
		return item