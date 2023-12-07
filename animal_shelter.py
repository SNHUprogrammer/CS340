from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self):
        USER = 'AACuser'
        PASS = 'letmein'
        HOST = 'nv-desktop-services.apporto.com'
        #PORT = 31580
        PORT = 31314 # this was the port I saw being used when connected manually in the terminal
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # The C in CRUD.
    # creates ONE
    def create(self, data):
        if data is not None:
            inserted = self.database.animals.insert_one(data)  # data should be dictionary
            
            return inserted != 0
        
        else:
            raise Exception("Nothing to create, because data parameter is empty")

    # The R in CRUD.
    # finds ALL
    def read(self, data):
        if data is not None:
            objects = self.database.animals.find(data, {"_id" : False})  # data should be dictionary
            
            for o in objects:
                print(o)

        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
    # The U in CRUD.
    # updates ONE
    def update(self, filt, data):
        if data is not None:
            self.database.animals.update_one(filt, data)  # data should be dictionary
            
            return 1        

        else:
            raise Exception("Nothing to update, because data parameter is empty")
    
    # The D in CRUD.
    # deletes FIRST ONE
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_one(data)  # data should be dictionary
            
            return 1

        else:
            raise Exception("Nothing to delete, because data parameter is empty")
