import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/huangyuepeng", echo=True)


class Mysql:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def query_all(self, table, cond=None):
        try:
            if cond:
                res = self.session.query(table).filter(*cond).all()
            else:
                res = self.session.query(table).all()
            return res
        except Exception as e:
            logging.error(f'{e}')
            self.session.rollback()

    def query_one(self, table, cond=None):
        try:
            if cond:
                res = self.session.query(table).filter(*cond).one()
            else:
                res = self.session.query(table).one()
            return res
        except Exception as e:
            logging.error(f'{e}')
            self.session.rollback()

    def insert(self, data):
        try:
            self.session.add_all(data)
            self.session.commit()
        except Exception as e:
            logging.error(f'{e}')
            self.session.rollback()

    def update(self, table, cond, data):
        try:
            self.session.query(table).filter(*cond).update(data)
            self.session.commit()
        except Exception as e:
            logging.error(f'{e}')
            self.session.rollback()

    def delete(self, table, cond):
        try:
            self.session.query(table).filter(*cond).delete()
            self.session.commit()
        except Exception as e:
            logging.error(f'{e}')
            self.session.rollback()



