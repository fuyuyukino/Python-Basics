#Random Number Guessing
import random

print("Hello, welcome to random game number \n")
print("Now, create upper and lower bond for the game \n")
print("You only have 10 chances to guess. Good Luck!! \n")

#Enter bound
low = int(input("Generate lower input: "))
up = int(input("Generate upper input: "))

print(f"You have 7 chances to guess number between {low} and {up}. Let's start!")

#Time and guess
num = random.randint(low,up)
chance = 7
guess = 0

while guess < chance:
    guess += 1
    trying = int(input(f"Attempt {guess}/{chance} - Enter your guess: "))

    if trying == num:
        print(f"Congratulation, correct number is {num}, you guessed it in {guess} attemps.")
        break
    elif guess == chance and guess != num:
        print(f"Sorry, the number was {num}. Better luck next time!")
    elif trying > num:
        print("The number is too high!")
    elif trying < num:
        print("THe number is too low")