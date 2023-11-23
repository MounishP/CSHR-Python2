# def add():
#     a = 7
#     b = 65
#     print(a + b)
#
#
# add()


# Functions with arguments
def add(a, b):
    return a + b


# Pass by value
# add(3, 8)
# add(2541, 53476)
# add(28, 234)
# add(32, 5)
# add(3, 36)
# add(3123, 8)

# Pass by reference

a = 24
b = 324
add(a, b)

c = 23
d = 87
print(add(c, d))  # add(c,d) = return a+b -> return 110 =110
