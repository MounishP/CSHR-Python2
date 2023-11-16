"""
malayalam
tot
dad
mom
madam

take input from the user and check if the word or string is a palidrome
"""

word = input("Enter the word to check: ")
result = ''.join(char.lower() for char in word if char.isalnum() and char != '')

"""
explaination for everything inside join()

for char in word:
    if char.isaplnum():
        char.lower()
"""

if result == result[::-1]:
    print(f"{word} is a palidrome")
else:
    print(f"{word} is not a palindrome")
