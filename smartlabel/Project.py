from .connection import db

class Project():
    def __init__(self):
        self.name=""
    
    def create_project(self, name, description = ""):
        mycursor = db.cursor()

        mycursor.execute("INSERT INTO project (Createdby,DatasetId, Name, Description, Status, Role) VALUES (%s,%s,%s,%s,%s,%s)",(1, 20, name, description, 0, 0))
        db.commit()

    def get_project(self, id):
        mycursor = db.cursor()
        mycursor.execute(f"SELECT * FROM project where ProjectId = {id}")
        data = []
        for x in mycursor:
            data.append(x)
        db.commit()
        columns = mycursor.column_names
        return data, columns
    
    def get_projects(self):
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM project")
        data = []
        for x in mycursor:
           data.append(x)
        db.commit()
        columns = mycursor.column_names
        return data, columns