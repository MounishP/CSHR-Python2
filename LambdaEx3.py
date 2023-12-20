# def test(x):
#     if x > 0:
#         return "Positive"
#     elif x == 0:
#         return "Zero"
#     else:
#         return "negative"

test = lambda x: "Positive" if x > 0 else ("Zero" if x == 0 else "negative")
print(test(-4))