import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of choices
choices = [scissors, paper, rock]

# User input
user_choice = int(input("Enter a number: 1. Scissors, 2. Paper, 3. Rock: "))
if user_choice not in [1, 2, 3]:
    print("Invalid input! Please enter 1, 2, or 3.")
else:
    print("You chose:")
    print(choices[user_choice - 1])

    # Computer choice
    computer_choice = random.randint(1, 3)
    print("Computer chose:")
    print(choices[computer_choice - 1])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 2) or \
            (user_choice == 2 and computer_choice == 3) or \
            (user_choice == 3 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")
