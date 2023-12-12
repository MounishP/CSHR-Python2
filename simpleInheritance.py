# Simple Inheritance

class Animal:  # Parent class or Super
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speak called in Animal class")


class Dog(Animal):  # Child class or subclass
    def __init__(self, name, food):
        super().__init__(name)
        self.dogFood = food


denver = Dog("Denver", "Pedigree")
print(denver.name)
print(denver.dogFood)


# Multiple Inheritance
# Parent -> Child1
#        -> Child2

class Cat(Animal):
    pass


cat = Cat("snowbell")
cat.speak()
