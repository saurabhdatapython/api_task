from  flask import  Flask, request,jsonify
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://saurabhdata:Rajbhatta1!#$@saurabhdata.ckhjdot.mongodb.net/?retryWrites=true&w=majority")
database = client["tasksql"]
collections = database["task_table"]

@app.route("/insert/mongo",methods = ["POST"])
def insert_mongo():
    if request.method == "POST":
        name = request.json["name"]
        number = request.json["number"]
        collections.insert_one({name:number})
        return jsonify(str("sucessfully insert data"))


if __name__ == '__main__':
    app.run(port=5001)


