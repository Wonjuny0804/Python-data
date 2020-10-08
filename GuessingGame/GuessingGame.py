"""
This Game is just a small project that I made for
fun. You have to guess the number generated between 1 and 1000
"""

import random

randomnumber = random.randint(1,1000)

lowest = 1
highest = 1000
print("Please guess a number between ",lowest,":",highest)
guess = int(input())
while True:
    
    if guess > randomnumber:
        highest = guess
        print("your guess is higher. Go lower")
        print("Please guess a number between ",lowest,"and",highest)
        guess = int(input())
    elif guess < randomnumber:
        lowest = guess
        print("your guess is lower. Go higher")
        print("Please guess a number between",lowest,"and",highest)
        guess = int(input())
    else:
        break

print("Game over")