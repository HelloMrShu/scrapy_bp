import os

# BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 定义配置基类
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'r_martisan'

    # 数据库公用配置
    # 无警告
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 发邮件 配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '1825514258@qq.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'lhyjeyaywqfdegeg'
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    MAIL_PORT = 465
    MAIL_USE_TLS = False

    # 文件上传的位置
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR, 'static/uploads')

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/scrapy?charset=utf8'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_ECHO = True

    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass
