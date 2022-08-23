from flask import  Flask , request, jsonify

app = Flask(__name__)

@app.route('/abc',methods=['GET' , 'POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))
if __name__=='__main__'  :

    app.run()


def sql_connect():
    import mysql.connector as connection
    my_db = connection.connect(host="localhost", user="root", passwd="Rajbhatta1!#$")


