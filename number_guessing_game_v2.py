import random
import time
import pygame
import os

# Initialize pygame for sound effects
pygame.init()

# Path to your 'sounds' folder located in your current project folder
sound_folder = os.path.join(os.getcwd(), 'sounds')

# Load sound effects
correct_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'correct.wav'))
wrong_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'wrong.wav'))
cheer_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'cheer.wav'))

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Difficulty selection with validation
    while True:
        print("\nChoose a difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")

        try:
            difficulty = int(input("Enter the number corresponding to the difficulty level: "))
            if difficulty == 1:
                number_to_guess = random.randint(1, 50)
                max_attempts = 10
                break
            elif difficulty == 2:
                number_to_guess = random.randint(1, 100)
                max_attempts = 7
                break
            elif difficulty == 3:
                number_to_guess = random.randint(1, 200)
                max_attempts = 5
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    attempts = 0
    start_time = time.time()
    elapsed_time = None  # Initialize to track if the player wins

    while attempts < max_attempts:
        try:
            user_guess = int(input("\nGuess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        

        if user_guess == number_to_guess:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"🎉 Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts and {elapsed_time:.2f} seconds.")
            correct_sound.play()
            pygame.time.wait(1000) 
             
            print("🎉 You Win! Playing Congratulations Sound!")
            cheer_sound.play()
            pygame.time.wait(6000)

            
            break
        elif user_guess < number_to_guess:
            print("⬇️ Your guess is too low. Try again.")
            wrong_sound.play()
            pygame.time.wait(1000)
        else:
            print("⬆️ Your guess is too high. Try again.")
            wrong_sound.play()
            pygame.time.wait(1000)

        if attempts == max_attempts // 2:
            hint = "even" if number_to_guess % 2 == 0 else "odd"
            print(f"Hint: The number is {hint}.")

    if user_guess != number_to_guess:
        print(f"\n😢 You've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

    # Record high score only if guessed correctly
    if elapsed_time:
        try:
            with open('high_scores.txt', 'r') as file:
                high_scores = file.readlines()
        except FileNotFoundError:
            high_scores = []

        high_scores.append(f"{elapsed_time:.2f} seconds - {attempts} attempts\n")

        with open('high_scores.txt', 'w') as file:
            file.writelines(high_scores)

        print("\nHigh Scores:")
        for score in high_scores:
            print(score.strip())

# Run the game
number_guessing_game()