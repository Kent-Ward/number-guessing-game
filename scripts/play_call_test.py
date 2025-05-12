import random
import time
import pygame
import os

# Initialize pygame
pygame.init()

# Load sound files
sound_folder = os.path.join(os.getcwd(), 'sounds')
correct_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'correct.wav'))
wrong_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'wrong.wav'))

# Setup game variables
number_to_guess = random.randint(1, 10)  # Keep it small for testing
max_attempts = 3
attempts = 0

print("Diagnostic Test: Guess the number between 1 and 10")

while attempts < max_attempts:
    try:
        user_guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if user_guess == number_to_guess:
        print("Playing CORRECT sound 🎉")  # Diagnostic log
        correct_sound.play()
        pygame.time.wait(1000)
        break
    elif user_guess < number_to_guess:
        print("Playing WRONG sound ⬇️")  # Diagnostic log
        wrong_sound.play()
        pygame.time.wait(1000)
    else:
        print("Playing WRONG sound ⬆️")  # Diagnostic log
        wrong_sound.play()
        pygame.time.wait(1000)

if user_guess != number_to_guess:
    print(f"The correct number was {number_to_guess}.")
