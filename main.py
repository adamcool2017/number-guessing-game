import random  # This lets us generate a random number

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print(" Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

# Loop until the user guesses correctly
while True:
    try:
        # Take input from the user
        guess = int(input("Enter your guess: "))
    except ValueError:
        print(" Please enter a valid number!")
        continue

    # Check if the guess is correct
    if guess == secret_number:
        print(" Correct! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low ")
    else:
        print("Too high ")