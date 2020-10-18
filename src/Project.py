from .connection import db
import mysql.connector
from mysql.connector import errorcode

class Project():
    def __init__(self):
        self.name=""
    
    def create_project(self, name, description = ""):
        mycursor = db.cursor()

        mycursor.execute("INSERT INTO project (Createdby,DatasetId, Name, Description, Status, Role) VALUES (%s,%s,%s,%s,%s,%s)",(1, 20, name, description, 0, 0))
        db.commit()

    def get_project(self, id):
        try:
            mycursor = db.cursor()
            mycursor.execute(f"SELECT * FROM project where ProjectId = {id}")
            data = []
            for x in mycursor:
                data.append(x)
            db.commit()
            columns = mycursor.column_names
            return data, columns
        except mysql.connector.ProgrammingError as err:
            if errorcode.ER_NO_SUCH_TABLE == err.errno:
                 print("No table exists")
            else:
                print("Table exists")
                print(err)

        except mysql.connector.Error as err:
                print("Some other error")
                print(err)
    
    def get_projects(self):
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM project")
            data = []
            for x in mycursor:
                data.append(x)
            db.commit()
            columns = mycursor.column_names
            return data, columns
        except db.connector.ProgrammingError as err:
            print(err.errno)
            print(err.sqlstate)
            print(err.msg)
        except db.connector.Error as err:
            print(err)