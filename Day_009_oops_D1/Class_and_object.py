class Dog:
    def __init__(self, name, age):      # Constructor
        self.name= name                 # Attribute
        self.age= age                   # Attribute

    def bark(self):                     # Class Method
        print(f"{self.name} says Woof!")

# Created a object with the name d
d = Dog("Tommy", 12)

# calling class method assign to the object d
d.bark()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"{self.name}! \nhi how you doing!"

    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

shivam = Person("Shivam", 26)
print(shivam.greet())
print(shivam.is_adult())