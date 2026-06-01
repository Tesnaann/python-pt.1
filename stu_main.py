from student_utils. marks import calculate_total,calculate_average
from student_utils.grade import get_grade

name=input("Enter name:")
marks=[]
print("Enter marks of 5 subjects")
for i in range(5):
    mark=int(input(f"subject{i+1}:")) #sub1:,sub2:
    marks.append(mark)

total=calculate_total(marks)
avaerage=calculate_average(marks)
grade=get_grade(avaerage)

print("student Name",name)
print("Total marks",total)
print("Average",avaerage)
print("Grade",grade)