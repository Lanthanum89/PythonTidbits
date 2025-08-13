# Hangman Game

A classic console-based word guessing game where players try to guess a hidden word one letter at a time.

## Description

This Python implementation of the traditional Hangman game challenges players to guess a randomly selected word by guessing individual letters. Players have a limited number of incorrect guesses before losing the game, with a visual hangman drawing that progresses with each wrong guess.

## How to Run

```bash
python3 hangman.py
```

## Features

- Random word selection from a predefined word list
- Visual hangman drawing that updates with each incorrect guess
- 6 maximum incorrect guesses allowed
- Input validation (single letters only)
- Prevents duplicate letter guesses
- Win/lose conditions with appropriate messages
- ASCII art hangman stages

## Requirements

- Python 3.x

## Word List

The game includes these words:
- python
- hangman  
- challenge
- programming
- developer

## Example Gameplay

```
Let's play Hangman!

           -----
           
           
           
           
           

_ _ _ _ _ _

Guess a letter: p
Good job! 'p' is in the word.
p _ _ _ _ _

Guess a letter: z
Sorry, 'z' is not in the word.

           -----
           |   |
           |   O
           |
           |
           -

p _ _ _ _ _
```

## How It Works

1. A random word is selected from the word list
2. The word is displayed as underscores
3. Player guesses letters one at a time
4. Correct guesses reveal letters in their positions
5. Incorrect guesses add to the hangman drawing
6. Game ends when the word is completed or hangman is fully drawn

Perfect for improving vocabulary and having fun with word puzzles!