class Animal:                               # Parent class
    def __init__(self, name):
        self.name = name

    def set(self):
        print(f"{self.name} is eating")

class Dog(Animal):                          # Child class — inherits Animal
    def bark(self):
        print(f"{self.name} says Woof!")


d = Dog("tommy")
d.bark()                                    # ✅ Dog's own method
d.set()                                     # ✅ inherited from Animal
print(d.name)