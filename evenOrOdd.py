"""
To check if the given number is even or odd

            2)4(2
              4
            -----
              0      -> remainder
"""

n = int(input("Enter the number: "))

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
