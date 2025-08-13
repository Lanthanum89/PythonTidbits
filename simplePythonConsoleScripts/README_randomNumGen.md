# Random Number Generator

A simple console utility that generates random numbers within a specified range.

## Description

This Python script allows users to generate random numbers between any minimum and maximum values they specify. It includes input validation to ensure the minimum value is less than the maximum value.

## How to Run

```bash
python3 randomNumGen.py
```

## Features

- Interactive input prompts for minimum and maximum values
- Input validation (ensures minimum < maximum)
- Generates truly random numbers using Python's `random` module
- Clear error messages for invalid input
- Simple one-time execution per run

## Requirements

- Python 3.x

## Example Usage

```
Enter the minimum value: 1
Enter the maximum value: 100
Generated random number between 1 and 100: 42
```

```
Enter the minimum value: 50
Enter the maximum value: 30
Minimum value must be less than maximum value.
```

## How It Works

The application:
1. Prompts the user for minimum and maximum values
2. Validates that minimum < maximum
3. Uses `random.randint()` to generate a random integer within the specified range (inclusive)
4. Displays the generated number

Perfect for games, decision making, or any situation where you need a random number within a specific range.