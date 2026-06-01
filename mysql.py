import pymysql
connection=pymysql.connect(user="root",host="localhost",passwd="admin",database="amazon_db")

my_cursor=connection.cursor()
name=input("Enter your name:")
place=input("Enter your place")
dob=input("Enter date of birth in YYYY-MM-DD format:")

my_cursor.execute(f"INSERT INTO customers(name,place,dob)VALUES('{name})',' {place}','{dob}',' ")

connection.commit()