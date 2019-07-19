# -*- coding: utf-8 -*-


import pymysql
from poi.settings import DB_CONFIG


class DBHelper():
    """"
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
    def poiinsert(self, item):
        try:
            cursor = self.cursor
            sql = "insert into poi(name,province,city,district,code,phone_no,region,location,category,sub_category," \
                  "longitude,latitude) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            # 调用插入的方法
            self.db.ping(reconnect=True)
            cursor.execute(sql, (
                item["name"],
                item["province"],
                item["city"],
                item["district"],
                item["code"],
                item["phone_no"],
                item["region"],
                item["location"],
                item["category"],
                item["sub_category"],
                item['longitude'],
                item['latitude']
            )
                           )
            self.db.commit()

        except Exception as e:
            print('poi insert error', e)
            self.db.rollback()
        finally:
            self.db.close()

        return item

    def cityinsert(self, item):
        try:
            cursor = self.cursor
            sql = "insert into cities(name,level) values(%s,%s)"

            # 调用插入的方法
            self.db.ping(reconnect=True)
            cursor.execute(sql, (
                item["name"], item['level']
            )
                           )
            self.db.commit()

        except Exception as e:
            print('insert error', e)
            self.db.rollback()
        finally:
            self.db.close()

        return item

    def categoryinsert(self, item):
        try:
            cursor = self.cursor
            sql = "insert into category(name) values(%s)"

            self.db.ping(reconnect=True)
            cursor.execute(sql, (
                item["name"])
                           )

            self.db.commit()

        except Exception as e:
            print('category insert error', e)
            self.db.rollback()
        finally:
            self.db.close()
        return item

    def getcategory(self):
        try:
            cursor = self.cursor
            sql = "select * from category"

            self.db.ping(reconnect=True)
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print('category select error', e)
        finally:
            self.db.close()

    def getcity(self):
        try:
            cursor = self.cursor
            sql = "select * from cities"

            self.db.ping(reconnect=True)
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print('city select error', e)
        finally:
            self.db.close()
