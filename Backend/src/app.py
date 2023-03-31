from flask import Flask,request,jsonify
from flask_cors import CORS
from DataBase import conection
from bson import json_util
from bson.objectid import  ObjectId


app = Flask(__name__)


### home ###
@app.route("/", methods=["GET"])
def home():
    return "Home"

### GETALL ###
@app.route("/Users", methods=["GET"])
def getAllmusician ():
    db = conection.dbConnection()
    users = list(db.Users.find())
    response = json_util.dumps(users)
    return response 

### GETONLY ###
@app.route("/User/<id>", methods=["GET"])
def getMusician(id):
    db = conection.dbConnection()
    user = db.Users.find_one({"_id" : ObjectId(id)})
    response = json_util.dumps(user)
    return response

### DELETE ###
@app.route("/User/<id>", methods=["DELETE"])   
def deleteMusician(id):
    db = conection.dbConnection()
    db.Users.delete_one({"_id": ObjectId(id)})
    response = jsonify({"message": "user" + id + "was deleted successfully"})
    return response

### POST ###
@app.route("/User", methods=["POST"])
def postInfomusician():
    # recive datos
    username = request.json["username"]
    years = request.json["years"]
    email = request.json["email"]
    #se mandan los datos
    if username and email and years:
        db = conection.dbConnection()

        id = db.Users.insert_one(
            {"username": username,"email": email,"years": years}
        )
        response = {
            "id": str(id.inserted_id),
            "username": username,
            "years": years,
            "email": email
        }
        return response
    else:
        return not_Found()
### PUT ###
@app.route("/user/<id>")
def putMusician (id):
    username = request.json["username"]
    years = request.json["years"]
    email = request.json["email"]
    if username and years and email:
        db = conection.dbConnection()
        db.Musicians.update_one({"_id": ObjectId(id)}, {"$set": {
            "username" : username,
            "years" : years,
            "email" : email    
        }})
        responde = jsonify({"message": "user" + id + "was updated successsfully"})
        return responde
    

# ERRORES
def not_Found(error=None):
    message = jsonify({
        "message" : "resource not found" + request.url,
        "status": 404
    })

#https://www.youtube.com/watch?v=D1W8H4Rkb9A



if __name__ == "__main__":
    app.run(debug=True, port=5000)