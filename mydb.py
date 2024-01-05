import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jesus458%',
)
# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a Database

cursorObject.execute("CREATE DATABASE Kordi")

print("All done")
