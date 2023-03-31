from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"

def dbConnection():
    try:
        cliente = MongoClient(MONGO_URI)
        db = cliente.Users
    except ConnectionError:
        print("error de conexion con la bdd")
    return db
       
###                                            ###         