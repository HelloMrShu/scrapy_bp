#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from app import create_app
from flask_script import Manager, Command
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from app.models import db, Poi, Monitor
from urllib import parse
import logging
import time
import psutil


config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app
app = create_app(config_name)
app.config['DEBUG'] = True
taskManager = Manager(app)

@taskManager.command
def create_index(name='location', type="poi"):
    _index_mappings = {
        "mappings": {
            type: {
                "properties": {
                    "poi_id": {
                        "type": "long",
                    },
                    "name": {
                        "type": "text",
                    },
                    "province": {
                        "type": "text",
                    },
                    "city": {
                        "type": "text",
                    },
                    "district": {
                        "type": "text",
                    },
                    "code": {
                        "type": "text",
                    },
                    "phone_no": {
                        "type": "text",
                    },
                    "region": {
                        "type": "text",
                    },
                    "location": {
                        "type": "text",
                    },
                    "category": {
                        "type": "text",
                    },
                    "coordinate": {
                        "type": "geo_point",
                    }
                }
            }
        }
    }
    es = Elasticsearch(['127.0.0.1:9200'])
    if es and es.indices.exists(index=name) is not True:
        res = es.indices.create(index=name, body=_index_mappings)
        print(str(res) + "\ncreate index success！")
    else:
        print('create index failed！')


@taskManager.command
def insert_poi(name='location', type="poi"):
    start_time = time.time()
    es = Elasticsearch(['127.0.0.1:9200'])
    poi_id = 1000000
    while poi_id > 1:
        pois = Poi.query.filter(Poi.id < poi_id).order_by(Poi.id.desc()).limit(1000).all()
        if pois:
            actions = []
            for poi in pois:
                try:
                    result = resolve(poi.name)
                    poi_name = result[0] if result else ''
                    action = {
                        "_index": name,
                        "_type": type,
                        "_source": {
                            "poi_id": str(poi.id),
                            "name": str(poi_name),
                            "province": str(poi.province),
                            "city": str(poi.city),
                            "district": str(poi.district),
                            "code": str(poi.code),
                            "phone_no": str(poi.phone_no),
                            "region": str(poi.region),
                            "location": str(poi.location),
                            "category": str(poi.category),
                            "coordinate": {"lat": str(poi.latitude), "lon": str(
                                poi.longitude)}
                        }
                    }
                    actions.append(action)

                except Exception as ex:
                    print(ex)
                    continue

            # 批量处理
            success, _ = bulk(es, actions, index=name, chunk_size=100, raise_on_error=True)
            poi_id = pois[-1].id
            
    print('poi insert done(s)：' + str(time.time() - start_time))

# 处理name里的特殊字符
def resolve(poiname):
    parsestr = parse.unquote(poiname)
    pattern = r'[\u4e00-\u9fa5]+[A-Za-z]'
    match = re.compile(pattern)
    return match.findall(parsestr)

# 每隔1s取一次cpu占用率并写入文件
@taskManager.command
def cpu_monitor():
    while True:
        # 获取当前时间和cpu占有率
        t  = time.localtime()
        cur_date = '%d-%d-%d' %(t.tm_year, t.tm_mon, t.tm_mday)
        cur_time = '%d:%d:%d' %(t.tm_hour, t.tm_min, t.tm_sec)
        cpu_res = psutil.cpu_percent()
     
        # 保存到DB
        monitor = Monitor(date=str(cur_date), time=str(cur_time), cpu_load=str(cpu_res))

        try:
            db.session.add(monitor)
            db.session.commit()

        except:
            db.session.rollback()

        finally:
            time.sleep(1)



if __name__ == '__main__':
    taskManager.run()
