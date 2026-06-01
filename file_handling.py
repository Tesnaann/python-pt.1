#file here is not a keyword 
'''file=open("Student_details.txt","a") #w here means write, a means append
#file.write("Tesna")
file.write("\n Aswin")
file.close()'''
#this will create a new file called student details with Tesna in it
#if w is used again instead of a, old text will be replaced by new while append add without replacing the old text

'''file=open("Student_details.txt","a")
student_count=int(input("Enter how many students"))
for k in range(student_count):
    name=input("Enter student name ")
    age=int(input("Enter student age"))
    course=input("Enter student course")
    file.write(f"{name},{age},{course}\n")
file.close()'''


file=open("Student_details.txt","r") # to read
data=file.readlines() # readlines print line by line each list
for std in data:
    std_data=std.split(",") 
    print("Name:",std_data[0]) 
    print("Age:",std_data[1])
    print("Course:",std_data[2])
file.close()

          
 
file=open("filehandling.txt","w")
