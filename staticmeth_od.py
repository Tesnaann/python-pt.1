#instead of using self decorator is used
class person:
    @staticmethod
    def is_adult(age):
        return age>=18
print(person.is_adult(17))

