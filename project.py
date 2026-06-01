'''student={}
def addstudent():
    student_id=int(input("Enter student id"))
    student_name=(input("Enter student name"))
    student_age=int(input("Enter student age"))

    marks={}
    subcount=int(input("Enter how many subjects"))
    for k in range(subcount):
        sub_name=(input("enter subject"))
        sub_mark=int(input("Enter mark"))
    marks[sub_name]=sub_mark

    std_detail={}
    std_detail["name"]=student_name
    std_detail["age"]=student_age
    std_detail["mark"]=sub_mark # creating key & value 

    student[student_id]=std_detail
def showstudents():
    for k in student:
        print("id:",student)
        print("name:",student[k]["name"])#first name is key and sec is value
        print("age:",student[k]["age"])
        print("marks:",student[k]["marks"])

def removestudent():
    std_id=int(input("Enter student id"))
    student.pop(std_id)
    print("Item removed sucessfully")
while True:
    print("1.Add student\n 2.view all students\n 3.remove student\n 4. exiting")
    choice=int(input("Enter the choice"))
    if choice ==1:
        addstudent()
    elif choice==2:
        showstudents()
    elif choice==3:
        removestudent()
    elif choice ==4:
        print("exiting")
        break'''


    
student={}
def addstudent():
    student_id=int(input("Enter student id"))
    student_name=input("Enter student name")
    student_age=int(input("Enter student age"))
    mark={}
    sub_count=int(input("Enter how many subject"))
    for k in range(sub_count):
     sub_name=input("Enter subject")
     sub_mark=int(input("Enter subject mark"))
     mark[sub_name]=sub_mark

    studentdetails={}
    studentdetails["name"]=student_name
    studentdetails["age"]=student_age
    studentdetails['mark']=sub_mark
    student[id]=studentdetails
def showstudent():
        for k in student:
            print("id:",student)
            print("name",student[k],"name")
            print("age",student[k],"age")
            print("marks",student[k],"mark")
def removestudent():
        student_id=int(input("Enter id"))
        student.pop(student_id)
        print("Item removd")
while True:
    print("1.add student\n 2.view all student\n 3.remove student\n 4. exiting")
    choice=int(input("Enter choice"))
    if choice==1:
        addstudent()
    elif choice==2:
        showstudent()
    elif choice==3:
        removestudent()
    elif choice==4:
        print("Exiting")
        