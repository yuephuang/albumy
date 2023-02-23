from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee

db = SQLAlchemy()
whooshee = Whooshee()

config = {}


def devlopConfig():
    # 数据库链接
    config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:123456@127.0.0.1:3306/alum?charset=utf8mb4'

    return config


Config = {
    'dev': devlopConfig()
}['dev']