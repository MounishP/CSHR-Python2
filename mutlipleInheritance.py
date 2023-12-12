"""
Multilevel Inheritance:
Grandparent
Parent
Child
"""


class Grandparent:
    def land(self):
        print("grandparent's land")


class Parent(Grandparent):
    def house(self):
        print("parent's house")


class Child(Parent):
    def mobile(self):
        print("Child's mobile")


mounish = Child()
mounish.land()
mounish.house()
mounish.mobile()
