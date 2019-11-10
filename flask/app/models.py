from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey

db = SQLAlchemy()


# 定义图片Model
class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    img_url = db.Column(db.String(100))

    def __repr__(self):
        return '<Images %r>' % self.title


# 定义文章Model
class Article(db.Model):
    __tablename = 'article'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=0)
    title = db.Column(db.String(64))
    content = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    comments = relationship('Comment', backref='Comment')


# 定义文章评论Model
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=0, nullable=True)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
    detail = db.Column(db.String(1024))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


# 定义poi类别model
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), default='', nullable=False)
    pinyin = db.Column(db.String(32), default='', nullable=False)


# 定义poi城市model
class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), default='', nullable=False)
    level = db.Column(db.Integer, default=0, nullable=False)


# 定义poi model
class Poi(db.Model):
    __tablename__ = 'poi'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), default='', nullable=False)
    province = db.Column(db.String(64), default='', nullable=False)
    city = db.Column(db.String(64), default='', nullable=False)
    district = db.Column(db.String(64), default='', nullable=False)
    code = db.Column(db.String(16), default='', nullable=False)
    phone_no = db.Column(db.String(64), default='', nullable=False)
    region = db.Column(db.String(64), default='', nullable=False)
    location = db.Column(db.String(256), default='', nullable=False)
    category = db.Column(db.String(64), default='', nullable=False)
    sub_category = db.Column(db.String(64), default='', nullable=False)
    longitude = db.Column(db.String(64), default=0, nullable=False)
    latitude = db.Column(db.String(64), default=0, nullable=False)


# 定义cpu load model
class Monitor(db.Model):
    __tablename__ = 'cpu_monitor'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(16), default='', nullable=True)
    time = db.Column(db.String(16), default=0, nullable=True)
    cpu_load = db.Column(db.DECIMAL(10,2), default=0, nullable=False)