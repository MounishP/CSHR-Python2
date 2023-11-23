"""
Find the greatest number of the 3 numbers
"""

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))


# d = int(input("Enter the number: "))

# if a > b and a > c:
#     print("a is greatest")
# elif b > a and b > c:
#     print("b is greatest")
# else:
#     print("c is greatest")

# max = a  # max = 346
#
# if b > max:  # 3246 > 346
#     max = b  # max = 3246
#
# if c > max:  # 243 > 3246
#     max = c
#
# if d > max:
#     max = d

# print(f"{max} is the greater")  # max = 3246


def maxOf3(a, b, c):
    max = a  # max = 346

    if b > max:  # 3246 > 346
        max = b  # max = 3246

    if c > max:  # 243 > 3246
        max = c

    return max


print(maxOf3(a, b, c))
