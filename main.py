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

# Input from the user
# & validation of input

while True:
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    except ValueError:
        print("Sorry your entry is not valid, please try again.")
        continue
    if user_choice < 0 or user_choice > 2:
        print("Sorry your entry is not valid, please try again.")
        continue
    else:
        break

# created a list for the variables

number_of_variables = [rock, paper, scissors]

# computer random choice algorithm

computer_choice = random.choice(number_of_variables)
index = number_of_variables.index(computer_choice)

# graphics for computer choice

print(computer_choice)
print("Computer choose:")

# graphics and logic for user choice

print(number_of_variables[user_choice])

# Logic for the game

if index == 0 and user_choice == 0:
    print("It's a draw")
elif index == 0 and user_choice == 1:
    print("You win")
elif index == 1 and user_choice == 0:
    print("You lose")
elif index == 2 and user_choice == 0:
    print("You win!")
elif index == 0 and user_choice == 1:
    print("You win!")
elif index == 1 & user_choice == 1:
    print("It's a draw")
elif index == 2 and user_choice == 1:
    print("You lose")
elif index == 0 and user_choice == 2:
    print("You lose")
elif index == 1 and user_choice == 2:
    print("You win!")
elif index == 2 and user_choice == 2:
    print("It's a draw")