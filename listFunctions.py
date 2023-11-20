n = [2, 4, 6, 8, 10]
# print
print(n)
# add a new number
n.append(12)
print("after adding: ", n)
# remove
n.remove(4)
print("after removing: ", n)
# access and print
print(f"first element: {n[0]}")
print(f"first element: {n[-1]}")
# sum of the list
total = sum(n)
print(f"total: {total}")
# check if a number is in the list
searchNumber = 4
if searchNumber in n:
    print(f"{searchNumber} is present")
else:
    print(f"{searchNumber} is not present")
