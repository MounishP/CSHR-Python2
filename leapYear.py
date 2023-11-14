"""
Check is the year is leap year or not
if year is completely divisible by 4 and not by 100 -> leap year
"""

year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

