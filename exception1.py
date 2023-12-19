# try:
#     result = 10 /0
#     print(result)
# except ZeroDivisionError:
#     print("Error: Dividing by zero")
# finally:
#     print("Thank you for using our ATM")

try:
    print(10/0)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Thank you")