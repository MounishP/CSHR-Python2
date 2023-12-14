class MathOperations:
    def add(self, x, y=None, z=None):
        if y is not None and z is not None:  # y,z are having some values
            return x + y + z
        elif y is not None:  # z is None, y is having some value
            return x + y
        else:
            return x


sum = MathOperations()
print(sum.add(1))
print(sum.add(1, 2))
print(sum.add(1, 2, 3))
