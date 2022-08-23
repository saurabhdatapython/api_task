from flask import Flask,request,jsonify
import mysql.connector as conn

app = Flask(__name__)
@app.route("/test")
def test():
    name = request.args.get("name")
    mob_no = request.args.get("mob")
    email = request.args.get("email")
    return "this is my first programe to get {} {} {}".format(name,mob_no,email)

@app.route('/fatchall')
def fet_data():
    try:
        db = request.args.get("db")
        tb = request.args.get("tb")
        my_db = conn.connect(user = "root",passwd = "Rajbhatta1!#$",host = "localhost")
        cur = my_db.cursor(dictionary=True)
        cur.execute(f"select *from {tb}")
        data = cur.fetchall()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(str(data))







if __name__== "__main__":
    app.run(port= 5002)