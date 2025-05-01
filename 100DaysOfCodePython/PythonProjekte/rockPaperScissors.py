import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissor = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    print(rock_paper_scissor[user_choice])
    print(f"Computer chose:\n{rock_paper_scissor[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    else:
        print("You lose")

else:
    print("Invalid input.")

