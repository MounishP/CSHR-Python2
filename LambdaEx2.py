# def mulOrAdd(x, y):
#     if x > 0:
#         return x * y
#     else:
#         # return x + y

mulOrAdd = lambda x, y: x * y if x > 0 else x + y
print(mulOrAdd(-4,9))
print(mulOrAdd(4,9))
