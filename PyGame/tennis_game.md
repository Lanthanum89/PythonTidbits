# Tennis Game (Single-Paddle Pong)

A simple one-paddle Pong-style game. Move the bat up and down to bounce the ball back.

## Requirements
- Python 3.8+
- Pygame 2.1+

Install dependencies:
```bash
pip install pygame
```

## How to Run
From the repository root:
```bash
python3 PyGame/tennis_game.py
```

Or from the PyGame directory:
```bash
python3 tennis_game.py
```

## Controls
- Up Arrow or W: Move bat up
- Down Arrow or S: Move bat down
- Close the window to exit

## Gameplay Notes
- Window size: 800x600
- Ball radius: 15px
- Ball bounces off walls and the bat
- Colors can be customized via constants at the top of the file:
  - BACKGROUND_COLOR
  - BAT_COLOR
  - BALL_COLOR

## Troubleshooting
- NameError: SCREEN_HEIGHT is not defined
  - The script references `SCREEN_HEIGHT` but does not define it. Add these lines near the top (after setting the display) to fix:
    ```python
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    ```
  - Alternatively, replace `SCREEN_HEIGHT` usages with `600`.
- If Pygame isn’t found: `pip install pygame`