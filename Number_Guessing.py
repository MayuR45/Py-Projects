import random

print("Welcome to the number-guessing game!")

# Set the target number
target = random.randint(1, 100)

# Initialize the player guess
guess = 0

# Set the number of guesses the player has made
num_guesses = 0

# Set the maximum number of allowed guesses
max_guesses = 5

while guess != target and num_guesses < max_guesses:
    # Get the player guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Check if the guess is correct
    if guess == target:
        print("You've guessed the right number! Congratulations!")
    else:
        if guess > target:
            print("Sorry, your guess was too high.")
        else:
            print("Sorry, your guess was too low.")

    # Increment the number guesses the player made
    num_guesses += 1

# If the player has run out of guesses, the game is over
if num_guesses == max_guesses:
    print("You've run out of guesses. The target number was: ", target)
