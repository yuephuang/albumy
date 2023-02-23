from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee

db = SQLAlchemy()
whee = Whooshee

config = {}


def devlopConfig():
    # 数据库链接
    config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:123456@127.0.0.1:3306/huang?charset=utf8mb4'

    return config


Config = {
    'dev': devlopConfig()
}['dev']


def create_app():
    app = Flask(__name__)
    # 初始化数据库
    app.config.update(Config)
    db.init_app(app)
    # 全文搜索
    whee.init_app(app)
    return app
