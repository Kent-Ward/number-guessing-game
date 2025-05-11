import random

# Step 1: Import the random module
# The random module will be used to generate a random number

def number_guessing_game():
    # Step 2: Generate a random number between 1 and 100
    # The randint function from the random module generates a random integer between the specified range
    number_to_guess = random.randint(1, 100)

    # Step 3: Initialize the number of attempts
    attempts = 0

    # Step 4: Start the game loop
    while True:
        # Step 5: Prompt the user to guess the number
        user_guess = int(input("Guess the number between 1 and 100: "))
        
        # Step 6: Increment the number of attempts
        attempts += 1
        
        # Step 7: Check if the user's guess is correct
        if user_guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("⬇️ Your guess is too low. Try again.")
        else:
            print("⬆️ Your guess is too high. Try again.")

# Step 8: Call the function to start the game
number_guessing_game()

