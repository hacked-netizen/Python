import mysql.connector

mydb=mysql.connector.connect( host="localhost",user="root",passwd="1234",database="example")

mycursor=mydb.cursor()

mycursor.execute("select * from student order by stream ")

x= mycursor.fetchall()

print(x)

