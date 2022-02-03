class Dog():
    # Class object attribute
    # Same for any instances of a class
    species = 'Mammal'

    def __init__(self, breed, name): # Constructor,
        # Attributes
        # We take in the argument
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name

    # Operations/Actions ---> Methods
    def bark(self, number):
        print("Woof! My name is {} and the number is {}". format(self.name, number))


class Circle():
    # Class object attribute
    pi = 3.1416
    def __init__(self, radius=1.0):
        self.radius = radius
        self.area = radius*radius*self.pi#*Circle.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2.0

my_dog = Dog(breed='Beagle', name='Sammy')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
my_dog.bark(5)

my_circle = Circle(radius=2.6)
print(my_circle.pi)
print(my_circle.get_circumference())
print(my_circle.radius)
print(my_circle.area)