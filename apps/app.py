from flask import Flask

from config.config import db, Config, whooshee


def create_app():
    app = Flask(__name__)
    # 初始化数据库
    app.config.update(Config)
    db.init_app(app)
    # 全文搜索
    whooshee.init_app(app)
    return app
