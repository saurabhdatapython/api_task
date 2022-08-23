import  mysql.connector as conn
import sqlalchemy
from flask import request,jsonify,Flask

app = Flask(__name__)

my_db = conn.connect(user = "root",passwd = 'Rajbhatta1!#$',host = "localhost")

cursor = my_db.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table if not exists tasksql.task_table(name varchar(30), number int)")

@app.route('/insert',methods = ['POST'])
def insert():
    if request.method == 'POST':
       name = request.json["name"]
       number = request.json["number"]
       cursor.execute("insert into tasksql.task_table values(%s , %s )",(name , number))
       my_db.commit()
       return jsonify(str("succesfully inserted"))

@app.route('/update',methods = ["POST"])
def update_table():
    if request.method == 'POST':
        get_name = request.json["get_name"]
        cursor.execute("update  tasksql.task_table set number  = number+1001 where name = %s ",(get_name,))
        my_db.commit()
        return jsonify(str("upadate table sucessfully"))

@app.route('/delete',methods = ["POST"])
def _delete():
    if request.method == 'POST':
        name_delete = request.json["name_delete"]
        cursor.execute("delete from tasksql.task_table where name = %s",(name_delete,))
        my_db.commit()
        return jsonify(str("delete table sucessful"))

@app.route("/fatch", methods = ["POST","GET"])
def fatch_data():
    cursor.execute("select * from tasksql.task_table")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))



if __name__ == '__main__':
    app.run()










