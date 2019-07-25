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

