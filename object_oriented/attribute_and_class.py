class Dog:
    # Class object attribute
    # same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # Operations/Actions -----> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {} ".format(self.name, number))


my_dog = Dog('lab', 'frank')

print(Dog.species)
print(my_dog.bark(3))


class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=5):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())





