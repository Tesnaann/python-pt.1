from tkinter import *
import pymysql

window=Tk()
connection=pymysql.connect(user="root",host="localhost",password="12345",database="amazon_db")
cursor=connection.cursor()

def SaveCustomer():
    sql_query=f"INSERT INTO customer(name,place,dob) VALUES('{Customer_name.get()})','{place.get()}','{dob.get()}');"
    cursor.execute(sql_query)
    connection.commit()
    print("New customer added")



Label(window,text="Customer Name").grid(row=0,column=0)
Customer_name=Entry(window)
Customer_name.grid(row=0,column=1)

Label(window,text="place").grid(row=1,column=0)
place=Entry(window)
place.grid(row=1,column=1)

Label(window,text="Date of Birth").grid(row=2,column=0)
dob=Entry(window)
dob.grid(row=2,column=1)

Button(text="Register",command=SaveCustomer).grid(row=3,column=0,columnspan=2)

window.mainloop()
 

