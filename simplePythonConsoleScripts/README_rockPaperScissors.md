# Rock Paper Scissors

A beginner-friendly console-based Rock Paper Scissors game where players compete against the computer with score tracking.

## Description

This Python implementation of the classic Rock Paper Scissors game allows players to compete against the computer. The game includes comprehensive error handling, score tracking, and the ability to play multiple rounds.

## How to Run

```bash
python3 rockPaperScissors.py
```

## Features

- Play against computer opponent with random choices
- Score tracking for both player and computer
- Multiple rounds with play-again option
- Comprehensive error handling and input validation
- Graceful exit options (type 'q' to quit or Ctrl+C)
- Clear game rules and win/lose logic
- Final score display when game ends

## Requirements

- Python 3.x

## Game Rules

- Rock beats Scissors
- Paper beats Rock  
- Scissors beats Paper
- Same choice = Tie (no points awarded)

## Example Gameplay

```
Welcome to Rock, Paper, Scissors!
----------------------------------

Enter your choice (rock/paper/scissors) or 'q' to quit: rock

You chose: rock
Computer chose: scissors
You win!

Score - You: 1 Computer: 0

Play again? (y/n): y

Enter your choice (rock/paper/scissors) or 'q' to quit: paper

You chose: paper
Computer chose: paper
It's a tie!

Score - You: 1 Computer: 0

Play again? (y/n): n

Final Score:
You: 1
Computer: 0

Thanks for playing!
```

## How It Works

1. Player enters their choice (rock, paper, or scissors)
2. Computer randomly selects its choice
3. Game determines winner based on traditional rules
4. Scores are updated and displayed
5. Player can choose to continue or quit
6. Final scores shown at game end

Perfect for quick entertainment and demonstrating basic game logic programming concepts!