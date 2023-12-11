class Blueprint:
    def __init__(self):
        print("Contructor called")

    def add(self, a, b):
        print(a + b)


mounish = Blueprint()
mounish.add(3, 5)
ravali = Blueprint()
ravali.add(34, 546)
ravali.add(3245, 43265)
