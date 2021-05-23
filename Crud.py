import mysql.connector                          
db=mysql.connector.connect(
	host="localhost",                   #connecting python and mysql
	user="venkat",
	passwd="root",
	database="mydatabase"
	)
	
cur=db.cursor()

cur.execute("CREATE TABLE STUDENT(name VARCHAR(30),age INT, stuid INT PRIMARYKEY AUTO_INCREAMENT")          #create table


sql="INSERT INTO STUDENT(name,age) VALUES(%s,%s)"                               #Insert Row to the table

val=[
	("venkat",23),
	("raja",29),
	("ravi",23),
	("ebis",22)
	]
cur.executemany(sql,val)

db.commit()

cur.execute("SELECT * FROM STUDENT")                             #Select and Display the values

result=cur.fetchall()


for x in myresult:
	print(x)
	
	
sql = "DELETE FROM STUDENT name = 'ravi' "

cur.execute(sql)                                                   #delete the row        

db.commit()

print(cur.rowcount, "record(s) deleted")


sql = "DROP TABLE IF EXISTS STUDENT"                               #delete the table

cur.execute(sql)                                                   

cursor.close()
connection.close()
