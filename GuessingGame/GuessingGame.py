"""
This Game is just a small project that I made for
fun. You have to guess the number generated between 1 and 1000
# v1.1 mild upgrade
: get the starting number and the end number from the user!

"""

import random

start, end = input("Please give us the starting number and the ending number:").split()
randomnumber = random.randint(int(start),int(end))

lowest = int(start)
highest = int(end)
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