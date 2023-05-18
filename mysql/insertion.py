import mysql.connector

mydb=mysql.connector.connect( host="localhost",user="root",passwd="1234",database="example")

mycursor=mydb.cursor()

mycursor.execute("insert into student values('4','payal','70','commerce')")

mydb.commit()
