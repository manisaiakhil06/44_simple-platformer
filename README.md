# Simple Platformer

A 2D platformer game developed using **Python** and **Pygame** for the Software Engineering Lab.

This project was enhanced as part of the **Vibe Coding Lab Assignment**, where the original game was improved by fixing gameplay issues and implementing additional features.

---

## Features

-  Smooth player movement and jumping
-  Platform collision detection
-  Hazard detection
-  Goal system with score tracking
-  Game Over screen
-  Final score display
-  Difficulty selection (Easy, Medium, Hard)
-  Replay after Game Over
-  Jump, Goal and Death sound effects
-  Exit option from menu
-  Improved platform collision to prevent falling through platforms

---

#  Improvements Implemented

### Platform Collision Fix
- Fixed collision detection when falling at high speed.
- Prevents the player from passing through platforms.

### Start Menu
Before the game begins, the player can select:

- Easy
- Medium
- Hard

The selected difficulty changes gravity and jump strength.

---

### Game Over Screen

The game now displays a Game Over screen when:

- Player touches a hazard
- Player falls off the level

The screen shows:

- Final Score
- Selected Difficulty
- Replay Instructions
- Exit Option

---

### Replay System

After Game Over:

- Press **Enter** or **Space**
- Game restarts
- Score resets
- Player respawns
- Difficulty remains selected

---

### Sound Effects

The game generates sound effects programmatically.

Events with sound:

- Jump
- Goal reached
- Death

No external audio files are required.

---

#  Controls

| Action | Keys |
|---------|------|
| Move Left | A / Left Arrow |
| Move Right | D / Right Arrow |
| Jump | Space / W / Up Arrow |
| Select Easy | 1 |
| Select Medium | 2 |
| Select Hard | 3 |
| Start Game | Enter / Space |
| Replay | Enter / Space |
| Exit | Esc |

---

#  Requirements

- Python 3.x
- Pygame

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

#  Run the Game

```bash
python main.py
```

---

#  Project Structure

```
44_simple-platformer-main/
│
├── main.py
├── requirements.txt
├── README.md
│
└── game/
    ├── __init__.py
    ├── game_engine.py
    ├── player.py
    ├── platform.py
    └── hazard.py
```

---

#  Testing Checklist

✔ Game launches successfully

✔ Player movement works

✔ Jump works correctly

✔ Platform collision fixed

✔ Hazard collision detected

✔ Game Over screen appears

✔ Final score displayed

✔ Replay works correctly

✔ Difficulty selection works

✔ Goal increments score

✔ Sound effects play for Jump, Goal and Death

✔ Exit option works

---

#  Technologies Used

- Python
- Pygame

---

#  Assignment Objectives Completed

- Fixed platform collision bug
- Added Game Over screen
- Displayed final score
- Added replay functionality
- Added Easy, Medium and Hard difficulty levels
- Added jump, goal and death sound effects
- Improved gameplay experience
- Preserved original game functionality

---

# 📜 License

This project was developed for academic purposes as part of the Software Engineering Lab.
