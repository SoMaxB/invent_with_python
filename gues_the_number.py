# This is a Guess the Number game.
import random

guesses_taken = 0

print("Hello, whats your name? ")
my_name = input()

number = random.randint(1, 20)
print(f"Well {my_name}, I am thinking of a number between 1 and 20.")

for guesses_taken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken +1)
    print(f"Good job {my_name}! You guessed my number in {guesses_taken} guesses!")

if guess != number:
    number = str(number)
    print(f"Nope. The number I was thinking of was {number}.")

