"""
1. program to find the first three even numbers in a given range.

start
stop

odd -> skip
even -> print

3 even -> break
"""

start = int(input("Enter the start range: "))      #3
stop = int(input("Enter the stop range: "))        #80

evenNumbersFound = 0                               #0,1,2

for num in range(start, stop + 1):                 #3,4,5,6,7,8
    if num % 2 != 0:                               #T,F,T,F,T,F
        continue

    print(f"Found an even number: {num}")          #4,6,8
    evenNumbersFound += 1                          #1,2,3

    if evenNumbersFound == 3:                      #F,F,T
        print("Found 3 even numbers. Exiting the loop")   #
        break                                             #Stop
