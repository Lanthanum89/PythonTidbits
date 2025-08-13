# Balance Bird (Flappy-Bird-Style)

A lightweight side-scrolling game where a bird “jumps” to stay afloat while pipes scroll from right to left. Colliding with a pipe or the ground ends the game.

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
python3 PyGame/balance_bird.py
```

Or from the PyGame directory:
```bash
python3 balance_bird.py
```

## Controls
- Space: Jump (apply upward impulse)
- Esc: Exit the game loop
- Close the window to quit

## Gameplay Notes
- Window size: 800x600
- Pipes are generated periodically with a randomized gap position
- Collision with a pipe or the ground stops the game
- Target frame rate: 60 FPS

## Troubleshooting
- NameError: SCREEN_HEIGHT is not defined
  - The script references `SCREEN_HEIGHT` but does not define it. Add these lines near the top (after setting the display) to fix:
    ```python
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    ```
  - Alternatively, replace `SCREEN_HEIGHT` usages with `600`.
- If Pygame isn’t found: `pip install pygame`
