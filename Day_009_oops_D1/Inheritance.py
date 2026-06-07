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


class Vehicle:
    def __init__(self, speed, brand):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} moves at a speed of {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, speed, num_door):
        super().__init__(speed, brand)
        self.num_door = num_door

    def honk(self):
        print(f"{self.brand} car honks beep beep!")

class Bike(Vehicle):
    def __init__(self, brand, speed, has_carrier):
        super().__init__(speed, brand)
        self.has_carrier = has_carrier

    def wheelie(self):
        print(f"{self.brand} does a wheelie")

c = Car("Toyota", 120, 4)
c.move()     # Toyota is moving at 120 km/h
c.honk()     # Toyota goes Beep Beep!

b = Bike("Honda", 80, True)
b.move()     # Honda is moving at 80 km/h
b.wheelie()  # Honda does a wheelie!