class Animal():
    def __init__(self):
        print("Animal created!")
    def who_am_i(self):
        print("I am an animal!")
    def eat(self):
        print("I am eating!")

class Dog(Animal):

    species = 'Mammal'

    def __init__(self):
        Animal.__init__(self)
        print("Dog created!")
    def who_am_i(self):
        print("I am dog!")
    def eat(self):
        print("I am a dog eating!")
    def bark(self):
        print("WOOF !!")

myanimal  = Animal()
mydog = Dog()
mydog.eat()
mydog.who_am_i()
myanimal.who_am_i()
mydog.bark()


#--------------------------------Polymorphism--------------------------------#
class AnimalPolymorphism():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
'''
myanimal1 = AnimalPolymorphism("Fred")
myanimal1.speak()
-> raise NotImplementedError("Subclass must implement this abstract method")
    NotImplementedError: Subclass must implement this abstract method
'''

class DogPoly(AnimalPolymorphism):
    def speak(self):
        return self.name + " says WOOF!!"

class CatPoly(AnimalPolymorphism):
    def speak(self):
        return self.name + " says MEOW!!"

fido = DogPoly("Fido")
isis = CatPoly("Isis")

print(fido.speak())
print(isis.speak())

