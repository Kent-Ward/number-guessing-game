# 🎮 Number Guessing Game with Sound Effects

This is a simple Python **Number Guessing Game** that lets players choose a difficulty level and rewards or encourages them with **sound effects** based on their guesses.

---

## ✅ Features

- 🟢 Difficulty levels (Easy, Medium, Hard)
- 🟢 High score tracking in `high_scores.txt`
- 🟢 Fun **correct** and **wrong** sound effects
- 🟢 6-second **cheer sound** when the player wins
- 🟢 Input validation and hint system

---

## ✅ Files Included

| File Path                                           | Purpose                                                                 |
|----------------------------------------------------|-------------------------------------------------------------------------|
| `number_guessing_game/scripts/number_guessing_game_v2.py` | Final version of the game with sound effects and high score tracking. |
| `number_guessing_game/scripts/play_call_test.py`          | A test script to confirm correct sound file calls and mappings.       |
| `number_guessing_game/scripts/sound_test.py`              | Verifies basic functionality of sound playback in Python.             |
| `number_guessing_game/sounds/`                             | Folder containing sound files for game feedback.                      |
| `number_guessing_game/high_scores.txt`                    | Stores high scores between sessions.                                   |
| `number_guessing_game/README.md`                         | This project overview and documentation.                              |
| `number_guessing_game/venv/`                             | Python virtual environment (not tracked by Git).   


---

## ✅ Requirements

- Python 3.11 or higher
- Pygame library  
  Install it with:
  ```bash
  pip install pygame

  
## ✅ How to Run the Game

### 🖥️ Run This Game Locally On Your Computer

1. **Make sure you have Python 3.11 or higher installed.**  
   You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Clone or Download This Repository.**
   - If you have Git installed, run:
     ```bash
     git clone https://github.com/yourusername/number-guessing-game.git
     ```
   - Or click **"Code" > "Download ZIP"** on this page and extract the files.

3. **Open your terminal or command prompt.**
   - Navigate to the project folder you just downloaded:
     ```bash
     cd number-guessing-game
     ```

4. **(Optional but Recommended) Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows