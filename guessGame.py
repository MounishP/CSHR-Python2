"""
3. Guess the number game:
    in the range of 1 to 100 -> input
    guess -> ?
    attempts = 3
    hints -> lesser, greater
"""
import random

secretNumber = random.randint(1, 100)
guess = None
attempts = 0

while guess != secretNumber:                                #T,50!=87,90!=87
    guess = int(input("Enter the secret number(1-100): "))  #50,90,87
    attempts = attempts + 1                                 #1,2,3
    if guess < secretNumber:                                #50<87,90<87,87<87
        print("Too low! Try again")                         #
    elif guess > secretNumber:                              #90>87, 87>87
        print("Too high! Try again")                        #
    else:
        print(f"Congratulations! You guessed the correct number {secretNumber} with {attempts} attempts")
