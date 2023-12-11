class Dog:
    def __init__(self, age):  # Parameterised Constructor -> if you want to add values while creating the object
        self.name = "Mounish"
        self.age = age

    def bark(self):
        self.name = "Tarun"
        print(self.name)
        print("Woof!")


gr = Dog(3)
gr.bark()

