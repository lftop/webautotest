import pymysql
from pymysql import connect
import GetConfig as e

print(e.getconfig("database", "host"))
print(e.getconfig("database", "user"))
print(e.getconfig("database", "password"))
print(e.getconfig("database", "db"))
print(e.getconfig("database", "charset"))


class database:
    def __init__(self):
        self.db = self.__create_db()

    def __create_db(self):
        try:
            db = pymysql.Connect(
                host=e.getconfig("database", "host"),
                user=e.getconfig("database", "user"),
                password=e.getconfig("database", "password"),
                database=e.getconfig("database", "db"),
                charset=e.getconfig("database", "charset")
            )
            print("Connect to the database Successfully")
            return db
        except Exception as e1:
            print(e1)

    def search_items(self,**kwargs):
        pass



if __name__ == "__main__":
    db = database()
