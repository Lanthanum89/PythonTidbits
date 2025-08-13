# Ping Pong (Bouncing Ball)

A minimal PyGame demo that opens an 800x600 window and renders a ball that bounces off the window edges.

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
python3 PyGame/ping_pong.py
```

Or from the PyGame directory:
```bash
python3 ping_pong.py
```

## Controls
- No player controls; the ball bounces automatically.
- Close the window to exit.

## Gameplay Notes
- Window size: 800x600
- Ball radius: 15px
- Ball speed: 2px/frame in both X and Y

## Troubleshooting
- If the window doesn’t appear, ensure your Python environment can create GUI windows (not headless).
- If Pygame isn’t found: `pip install pygame`
