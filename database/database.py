import sqlite3
import logging

logger = logging.getLogger(__name__)


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if not cls._instance.get(cls):
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.con = sqlite3.connect('db.sqlite3', check_same_thread=False)

    def execute(self, q, *args):
        cur = self.con.cursor()

        try:
            cur.execute(q, args)
        except sqlite3.Error as e:
            logger.error(e)
            self.con.rollback()

        cur.close()

    def get_results(self, query, *args):
        cur = self.con.cursor()

        try:
            cur.execute(query)
            return cur.fetchall()
        except sqlite3.Error as e:
            logger.error(e)

    def commit(self):
        self.con.commit()

    def rollback(self):
        self.con.rollback()
