class Animal:
    def sound(self):
        print("Some Sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

animals = [Dog(), Cat(), Dog()]
for animal in animals:
    animal.sound()


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} moves at a speed of {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, speed, num_door):
        super().__init__(brand, speed)
        self.num_door = num_door

    def honk(self):
        print(f"{self.brand} car honks beep beep!")

    def move(self):
        print(f"{self.brand} is a car which moves at a speed of {self.speed}")

class Bike(Vehicle):
    def __init__(self, brand, speed, has_carrier):
        super().__init__(brand, speed)
        self.has_carrier = has_carrier

    def wheelie(self):
        print(f"{self.brand} does a wheelie")

    def move(self):
        print(f"{self.brand} is a bike which move at a speed of {self.speed}")

c = Car("Toyota", 120, 4)
c.move()   # Toyota drives on road at 120 km/h

b = Bike("Honda", 80, True)
b.move()   # Honda rides on road at 80 km/h doing wheelies!

v = Vehicle("Generic", 50)
v.move()   # Generic moves at 50 km/h