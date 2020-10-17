# TODO: Remove extra comments
from .connection import db

class Dataset():
    def __init__(self):
        self.name = ""
    
    def create_dataset(self, name, description = ""):
        """Create a new Data

        Args:
            name (str): Title of dataset
            description (str, optional): Description of the dataset. Helps in searching. Defaults to "".
        
        Returns:
            id (int): Id of the newly created dataset.
        """

        mycursor = db.cursor()


        #mycursor.execute("CREATE DATABASE smartlabels")
        #mycursor.execute("CREATE TABLE Labels (Label_id int PRIMARY KEY AUTO_INCREMENT, x1 FLOAT, y1 FLOAT)")
        mycursor.execute("INSERT INTO dataset (UserID, Name, Description) VALUES (%s,%s,%s)",(1, name, description))
        db.commit()

        # TODO: Return newly created dataset id

#Col names are not showing 
    def get_dataset(self, id):
        mycursor = db.cursor()


        #mycursor.execute("CREATE DATABASE smartlabels")
        #mycursor.execute("CREATE TABLE Labels (Label_id int PRIMARY KEY AUTO_INCREMENT, x1 FLOAT, y1 FLOAT)")
        #mycursor.execute("INSERT INTO dataset (UserID, Name, Description) VALUES (%s,%s,%s)",(1, name, description))
        mycursor.execute(f"SELECT * FROM dataset where DatasetId = {id}")

        for x in mycursor:
           
           thisdict = {
            "DatasetId": x[0],
            "UserID": x[1],
            "Name": x[2],
            "Description": x[3],
            "DateIn": x[4],
            "DateOut": x[5],
        }

        db.commit()
        return thisdict