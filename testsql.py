
import mysql.connector

def sql_connect():

   db_connection  = mysql.connector.connect(host="localhost",user="root",passwd= "Rajbhatta1!#$",database  = "task_api")

   my_database = db_connection .cursor()
   return  my_database
#sql_statement = "INSERT INTO api_sql (category,duration,level) values(%s,%s,%s)"
#values = ("Python","100 Hours","Advanced")

#my_database.execute(sql_statement,values)
#db_connection.commit()