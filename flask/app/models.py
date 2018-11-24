from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
import datetime

db = SQLAlchemy()

#定义图片Model
class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    img_url = db.Column(db.String(100))

    def __repr__(self):
        return '<Images %r>' % self.title

#定义文章Model
class Article(db.Model):
	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, default = 0)
	title = db.Column(db.String(64))
	content = db.Column(db.Text())
	created_at = db.Column(db.DateTime, default=datetime.datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.datetime.now)