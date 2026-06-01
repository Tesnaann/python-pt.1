class Employee:
    # Here company_name is class variable because all employees are part of same company 
    company_name = "TechSoft" 

    """init is a constructor in python it is a builtin method whcih get automaticaly called 
    when an object related to that class is created .
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)
    """
    company name was a class variable So inorder to change it we can use classmethod
    """
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def bonus(salary):
        return salary * 0.10


class Manager(Employee):

    def department(self):
        print(self.name, "is a Manager")


e1 = Employee("Arjun", 50000)
e1.display()

print("Bonus:", Employee.bonus(50000))

Employee.change_company("InfoTech")

print("\nAfter company change:")
e1.display()
"""
When Manager object m1 is created with values Rahul and 70000 has name and salary Employee init is called
 because Manager class inherits Employee class .

"""
m1 = Manager("Rahul", 70000)
m1.display()
m1.department()