"""
1. Handle exceptions when dividing by zero
2. Handle exceptions when dividing by any other value
"""
try:
    print(10 / 0)
except (ZeroDivisionError, NameError, ValueError) as e:
    print(f"Error: {e}")
    print(10/6)

class CustomError(Exception):
    def __init__(self,message = "A custom error occured"):
        self.message = message
        super().__init__(self.message)