import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="example"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")