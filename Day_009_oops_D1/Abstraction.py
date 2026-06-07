from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def breath(self):
        print("breathing...")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")


d = Dog()
d.sound()

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, speed, num_door):
        super().__init__(brand, speed)
        self.num_door = num_door

    def honk(self):
        print(f"{self.brand} car honks beep beep!")

    def move(self):
        print(f"{self.brand} is a car which moves at a speed of {self.speed}")

    def fuel_type(self):
        print(f"{self.brand} is a Diesel fuel type car.")

class Bike(Vehicle):
    def __init__(self, brand, speed, has_carrier):
        super().__init__(brand, speed)
        self.has_carrier = has_carrier

    def wheelie(self):
        print(f"{self.brand} does a wheelie")

    def move(self):
        print(f"{self.brand} is a bike which move at a speed of {self.speed}")

    def fuel_type(self):
        print(f"{self.brand} is a Petrol fuel type car.")


c = Car("Toyota", 120, 4)
c.move()   # Toyota drives on road at 120 km/h
c.fuel_type()
b = Bike("Honda", 80, True)
b.move()   # Honda rides on road at 80 km/h doing wheelies!
b.fuel_type()
