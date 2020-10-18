from .connection import db
import mysql.connector
from mysql.connector import errorcode

class Project():
    def __init__(self):
        self.name=""
    
    def create_project(self, Createdby,DatasetId, Name, Description, Status, Role = ""):
        mycursor = db.cursor()

        mycursor.execute("INSERT INTO project (Createdby,DatasetId, Name, Description, Status, Role) VALUES (%s,%s,%s,%s,%s,%s)",(Createdby,DatasetId, Name, Description, Status, Role))
        db.commit()

    def get_project(self, id):
        mycursor = db.cursor(buffered=True)
        mycursor.execute(f"SELECT * FROM project where ProjectId = {id}")
        rows_affected = mycursor.rowcount

        if rows_affected == 1:
            data = []
            for x in mycursor:
                data.append(x)
            db.commit()
            columns = mycursor.column_names
            return data, columns
        else:
            data = columns = 0
            return data, columns
            

    
    def get_projects(self):
        mycursor = db.cursor(buffered=True)
        mycursor.execute("SELECT * FROM project")
        rows_affected = mycursor.rowcount
        if rows_affected > 0 :
            data = []
            for x in mycursor:
                data.append(x)
            db.commit()
            columns = mycursor.column_names
            return data, columns
        else:
            data = columns = 0
            return data, columns
    