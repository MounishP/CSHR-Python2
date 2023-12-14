class Animal:
    def make_sound(self):
        print("animal class")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


cat = Cat()
cat.make_sound()
