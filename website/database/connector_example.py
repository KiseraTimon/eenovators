import mysql.connector

#Establishing SQL Connection
def dbconnector():
    return mysql.connector.connect(
        host='',
        user='',
        password='',
        database=''
    )