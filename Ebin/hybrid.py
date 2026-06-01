class Animal:
    def speak(self):
        print("animal speak")
class Mammal(Animal):
    def give_birth(self):
        print("Mamal give birth")
class Bird(Animal):
    def lay_eggs(self):
        print("bird lay eggs")
class Platypus(Mammal,Bird):
    pass
plat=Platypus()
plat.speak()
plat.lay_eggs()
plat.give_birth()
