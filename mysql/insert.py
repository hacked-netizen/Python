import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="hospital")

mycursor=mydb.cursor()
mycursor.execute("insert into inpatient values('P01','rishi','I01','Garvit')")
mydb.commit()
