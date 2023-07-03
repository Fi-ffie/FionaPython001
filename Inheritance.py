class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def speak(self):
            raise NotImplementedError("Child classes must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"

class Duck(Animal):
    def speak(self):
        return "Quacks"

dog = Dog("Bosco", "Black")
print(dog.name)
print(dog.color)
print(dog.speak())

cat = Cat("Whiskers", "White")
print(cat.name)
print(cat.color)
print(cat.speak())

duck = Duck("Feathers", "Brown")
print(duck.name)
print(duck.color)
print(duck.speak())
