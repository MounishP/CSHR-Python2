# Function
def square(x):
    return x ** 2


# print(list(map(lambda x:x**2,numbers)))

# Iterable
numbers = [1, 2, 3, 4, 5]

# result = []
# for i in numbers:
#     result.append(square(i))
# print(result)

result = map(square, numbers)
print(list(result))

print(list(map(lambda x: x ** 2, numbers)))
