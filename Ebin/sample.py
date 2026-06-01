class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"


print(Pen().use())
print(Eraser().use())