from connection import db

class Project():
    def __init__(self):
        self.name=""
    
    def create_project(self, name, description = ""):
        mycursor = db.cursor()

        mycursor.execute("INSERT INTO project (Createdby,DatasetId, Name, Description, Status, Role) VALUES (%s,%s,%s,%s,%s,%s)",(1, 20, name, description, 0, 0))
        db.commit()

    def get_project(self, id):
        mycursor = db.cursor()
        smycursor.execute(f"SELECT * FROM project where ProjectId = {id}")

        for x in mycursor:
           print(x)
        db.commit()
