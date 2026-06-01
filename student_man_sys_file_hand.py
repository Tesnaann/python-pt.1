
class StudetManagement:
    file="students.txt"
    def add_students(self):
        n=int(input("Enter how many student details you wish to store"))
        f=open(self.file,"a")
        for i in range(1,n+1):
            print("\nid:",i)
            name=input("Enter studet name:")
            age=int(input("Enter student age"))
            course=input("Enter student course")

            f.write(f"{name},{age},{course}")
        f.close()

    def search_by_id(self):
        id=int(input("Enter student id:"))
        f=open(self.file,"r")
        data=f.readlines()
        f.close()

        if id<= len(data):
            student=data[id-1].strip().split(",")
            print("\n id:",id)
            print("name:",student[0])
            print("Age;",student[1])
            print('course:',student[2])
        else:
            print("student not found")
s=StudetManagement()

while True:
    print("student Management system")
    print("1.add student")
    print("2.read student data")
    print("3.remove student")
    print("4.search by id")
    
    choice=int(input("Enter your choice"))
    if choice==1:
        s.add_students()
    elif choice==4:
        s.search_by_id()
    else:
        print("Invalid choice")
    cont=input("do you wish to continue:")
    if cont.lower()!="y":
        print("Exiting.........")
        break
