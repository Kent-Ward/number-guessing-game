import pygame
import os

# Initialize pygame mixer
pygame.init()

# Path to your 'sounds' folder located in your current project folder
sound_folder = os.path.join(os.getcwd(), 'sounds')

# Full paths to the sound files
correct_sound_path = os.path.join(sound_folder, 'correct.wav')
wrong_sound_path = os.path.join(sound_folder, 'wrong.wav')

# Load sounds
try:
    correct_sound = pygame.mixer.Sound(correct_sound_path)
    wrong_sound = pygame.mixer.Sound(wrong_sound_path)
    print("✅ Sounds loaded successfully!")

    # Play the sounds to test
    print("Playing correct sound...")
    correct_sound.play()
    pygame.time.wait(1000)  # Wait for 1 second to let the sound finish

    print("Playing wrong sound...")
    wrong_sound.play()
    pygame.time.wait(1000)

except Exception as e:
    print(f"❌ Failed to load or play sounds: {e}")