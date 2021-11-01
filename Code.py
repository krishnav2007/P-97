import random
number= random.randint(1, 9)
chances= 0
print("Guessing game")
print("Guess a number between 1 to 9")

while chances<5:
    guess= int(input("Enter your guess: "))
    if guess == number:
        print("You won!")
        break
    elif guess<number:
        print("Guess a higher a number")
    else:
        print("Guess a lower number")
    chances= chances+1
if not chances<5:
    print("You lose, The number was", number)
    
