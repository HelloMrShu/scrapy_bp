#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from app import create_app
from flask_script import Manager, Command
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from app.models import Poi

config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app
app = create_app(config_name)
app.config['DEBUG'] = True
taskManager = Manager(app)


@taskManager.command
def create_index(name='location', type="poi"):
    print('create_index')
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
        print(res)
        print('success')
    else:
        print('failed')


@taskManager.command
def insert_poi(name='location', type="poi"):
    es = Elasticsearch(['127.0.0.1:9200'])
    poi_id = 1000000
    while True:
        print('dealing poi id:' + str(poi_id))
        pois = Poi.query.filter(Poi.id < poi_id).order_by(Poi.id.desc()).limit(100).all()
        if pois:
            actions = []
            for poi in pois:
                action = {
                    "_index": name,
                    "_type": type,
                    "_id": str(poi.id),
                    "_source": {
                        "poi_id": str(poi.id),
                        "name": str(poi.name).replace("-", "/"),
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

                # 批量处理
                actions.append(action)
                success, _ = bulk(es, actions, index=name, raise_on_error=True)
            poi_id = pois[-1].id
        else:
            print('poi insert done!')


if __name__ == '__main__':
    taskManager.run()
