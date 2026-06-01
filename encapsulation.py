class employee:
    def __innit__(self,name,salary):
        self.name=name
        self.__salary=salary # __ is used to show private attribute,_ is used for protect
emp=employee("Amal",20000)
print(emp.name)
print(emp.__salary)

