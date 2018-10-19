from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    img_url = db.Column(db.String(100))

    def __repr__(self):
        return '<Images %r>' % self.title