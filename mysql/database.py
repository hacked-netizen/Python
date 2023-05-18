import mysql.connector

mydb=mysql.connector.connect( host="localhost",user="root",passwd="1234",database="example")

mycursor=mydb.cursor()

mycursor.execute("create table student(roll_no int,name varchar(12),marks int,stream varchar(10))")

mydb.commit()
