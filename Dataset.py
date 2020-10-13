from connection import db

class Dataset():
    def __init__(self):
        self.name = ""
    
    def create_dataset(self, name, description = ""):
        mycursor = db.cursor()


        #mycursor.execute("CREATE DATABASE smartlabels")
        #mycursor.execute("CREATE TABLE Labels (Label_id int PRIMARY KEY AUTO_INCREMENT, x1 FLOAT, y1 FLOAT)")
        mycursor.execute("INSERT INTO dataset (UserID, Name, Description) VALUES (%s,%s,%s)",(1, name, description))
        db.commit()


    def get_dataset(self, id):
        # @TODO
        # Return a dictionary containing information of dataset
        pass
