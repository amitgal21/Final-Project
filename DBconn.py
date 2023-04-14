import mysql.connector

def connectToDB():
    myConn = mysql.connector.connect(host='localhost',user='root',password='Shitrit1!',port = '3306',
                                     database ='final_project_db')


