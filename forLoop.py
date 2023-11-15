"""
for every item in the bucket I'll pay you 5rs

range(0   -> start point
range(,5) -> end point
for -> does incrementation -> when you complete executing the block get the next value
"""

# for item in range(0, 5):
#     print(item)

l = [1, 3.4, True, "Mounish"]
"""
for every item in the list check the data type
"""
for i in l:
    for j in range(4):
        print(f"{j} : {i}")
