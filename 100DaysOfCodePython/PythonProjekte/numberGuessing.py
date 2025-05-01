from arts.number_guessing_art import logo
import random

# TODO#1: print the logo and welcome the user
# TODO#2: choose a random number between 1 and 100
# TODO#3: ask player to choose a difficulty
# TODO#4: print the attempts and ask the user for a guess
# TODO#5: print if guess was too high, too low, or if the user guess right

GAME_OVER = 0
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
attempts = EASY_LEVEL_TURNS

if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'hard':
    attempts = HARD_LEVEL_TURNS

while attempts > GAME_OVER:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    attempts -= 1

    if attempts == GAME_OVER:
        print(f"You've run out of guesses. The answer was {number}. Refresh the page to run again.")
    else:
        if guess == number:
            print(f"You got it! The answer was {number}")
            attempts = GAME_OVER
        elif guess > number:
            print("Too high.\nGuess again.")
        elif guess < number:
            print("Too low.\nGuess again.")
