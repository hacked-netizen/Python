import mysql.connector

mydb=mysql.connector.connect( host="localhost",user="root",passwd="1234",database="example")

mycursor=mydb.cursor()

mycursor.execute("select stream, sum(marks) from student group by stream")

x= mycursor.fetchall()

print(x)

