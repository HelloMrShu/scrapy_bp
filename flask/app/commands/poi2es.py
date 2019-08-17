#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from app.models import Image, Article, db, Comment, Category, City, Poi


class PoiStorage(object):

    def get_data(self):
        result = Poi.query.all()
        return result


class ElasticObj(object):

    def __init__(self, index_name,index_type, ip ="127.0.0.1"):
        """
        :param index_name: 索引名称
        :param index_type: 索引类型
        """

        self.index_name = index_name
        self.index_type = index_type
        self.es = Elasticsearch([ip], http_auth=('elastic', 'password'), port=9200)

    def create_index(self, index_name='data', index_type="media_consume_table"):
        _index_mappings = {
            "mappings": {
                index_type: {  # 相当于数据库中的表名
                    "properties": {
                        "id": {
                          "type": "long",
                          "store": True,
                        },
                        "dt": {
                            "type": "date",
                            "store": True,
                            "format": "yyyy/MM/dd HH:mm:ss||yyyy/MM/dd||epoch_millis"
                        },
                        "product": {
                            "type": "keyword",
                            "index": True,
                        },
                        "meida": {
                            "type": "keyword",
                            "index": True,
                        },
                        "meida_sub_categorey": {
                            "type": "keyword",
                            "index": True,
                        },
                        "account": {
                            "type": "keyword",
                            "index": True,
                        },
                        "ad_campaign": {
                          "type": "text",
                          # "analyzer": "ik_max_word",
                          # "search_analyzer": "ik_max_word"
                        },
                        "ad_type": {
                            "type": "keyword",
                            "index": True,
                        },
                        "consume": {
                            "type": "keyword",
                            "store": True,
                        },
                        "shows": {
                            "type": "keyword",
                            "store": True,
                        },
                        "clicks": {
                            "type": "keyword",
                            "store": True,
                        },
                        "pay_downloads": {
                            "type": "keyword",
                            "store": True,
                        },
                        "publish_time": {
                              "type": "date",
                              "store": True,
                              "format": "yyyy/MM/dd HH:mm:ss||yyyy/MM/dd||epoch_millis"
                        },
                        "update_time": {
                              "type": "date",
                              "store": True,
                              "format": "yyyy/MM/dd HH:mm:ss||yyyy/MM/dd||epoch_millis"
                        },
                        "ad_group": {
                            "type": "string",  # 字符串
                            "store": True
                        },
                        "ad_case": {
                            "type": "string",
                            "store": True
                        }
                    }
                }
            }
        }
        if self.es.indices.exists(index=index_name) is not True:
            res = self.es.indices.create(index=index_name, body=_index_mappings)
            print res