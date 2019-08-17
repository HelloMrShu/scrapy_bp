# -*- coding: utf-8 -*-

import pymysql
from image.settings import DB_CONFIG


class DBHelper(object):
    """
    读取settings中的配置，实现数据库操作
    """

    def __init__(self):

        self.db = pymysql.connect(
            host=DB_CONFIG['MYSQL_HOST'],
            db=DB_CONFIG['MYSQL_DBNAME'],
            user=DB_CONFIG['MYSQL_USER'],
            passwd=DB_CONFIG['MYSQL_PASSWD'],
            charset=DB_CONFIG['MYSQL_CHARSET'],
            port=DB_CONFIG['MYSQL_PORT']
        )

        self.cursor = self.db.cursor()

    # 插入数据库
    def insert(self, item):
        try:
            cursor = self.cursor
            sql = "insert into images(title,img_url) values(%s,%s)"
            # 调用插入的方法
            self.db.ping(reconnect=True)
            cursor.execute(sql, (
                item["title"], item['url']
            )
                           )
            self.db.commit()

        except Exception as e:
            print('insert error', e)
            self.db.rollback()
        finally:
            self.db.close()

        return item
