# Import random module
import random

# list of possible choices
choices = ['rock', 'paper', 'scissors']

# Print welcome message
print("Welcome to the game of rock, paper, scissors!")

# Ask player to choose
player_choice = input("Please enter your choice (rock, paper, or scissors): ")

# Check the player's choice is right
while player_choice not in choices:
  player_choice = input("Please enter a valid choice (rock, paper, or scissors): ")

# Generate a random choice for computer
computer_choice = random.choice(choices)

# Print player's choice and the computer choice
print("You chose:", player_choice)
print("The computer chose:", computer_choice)

# find the winner
if player_choice == computer_choice:
  # It's a tie
  print("It's a tie!")
elif player_choice == 'rock' and computer_choice == 'scissors':
  # Rock beats scissors
  print("You win!")
elif player_choice == 'paper' and computer_choice == 'rock':
  # Paper beats rock
  print("You win!")
elif player_choice == 'scissors' and computer_choice == 'paper':
  # Scissors beats paper
  print("You win!")
else:
  # The computer wins
  print("The computer wins!")
