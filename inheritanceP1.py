"""
Parent - Vehicle -> make, model, year
Child - Car -> no. of wheels
Child - Bike -> no. of wheels

"""


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display(self):
        super().display()
        print(f"Number of wheels: {self.num_wheels}")


class Bike(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display(self):
        super().display()
        print(f"Number of wheels: {self.num_wheels}")


car = Car("MG", "Hector", 2022, 6)
car.display()
bike = Bike("Yamaha", "R15", 2021, 2)
bike.display()
