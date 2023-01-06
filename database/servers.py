from database.database import Database


class Servers:

    def __init__(self):
        self.__db = Database()

    def get_all(self):
        q = '''select name from Servers'''
        result = self.__db.get_results(q)
        return [i[0] for i in result] if result else []

    def add(self, name):
        q = '''insert into Servers (name) VALUES (?)'''
        self.__db.execute(q, name)
        self.__db.commit()
