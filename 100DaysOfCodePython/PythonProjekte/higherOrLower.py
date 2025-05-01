from arts_and_data.higher_or_lower_art import logo, vs
from arts_and_data.higher_or_lower_data import data
import random

# TODO#1: print logo
# TODO#2: chose two random data from game_data as value a and b, with a != b
# TODO#3: print a and b name, description, and country with the vs art
# TODO#4: ask the user which of them has more followers and save it into a variable guess
# TODO#5: compare follower_count from A and B with guess
# TODO#6: track points in a variable score
# TODO#7: if the user is wrong print final score and end the game
# TODO#8: if the user is right print current score (loop, with clear screen)

def compare(data_a, data_b):
    """returns the greater data follower_count as a char 'a' or 'b'"""
    if data_a['follower_count'] > data_b['follower_count']:
        return 'a'
    else:
        return 'b'


score = 0
game_over = False
a = random.choice(data)
print(logo)

while not game_over:
    b = random.choice(data)
    while a == b:
        b = random.choice(data)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear screen
    print("\n" * 20)
    print(logo)

    # Check guess
    if compare(a, b) == guess:
        score += 1
        a = b
        print(f"You're right! Current score: {score}")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")

