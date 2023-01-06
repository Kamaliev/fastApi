from database.database import Database


class Operators:
    def __init__(self):
        self.__db = Database()


    def hello(self):
        print('hello')