# Magic 8 Ball

A simple console-based Magic 8 Ball fortune teller application that provides random responses to yes/no questions.

## Description

This Python script simulates the classic Magic 8 Ball toy. Ask any yes or no question, and the Magic 8 Ball will provide you with a random response from a collection of traditional Magic 8 Ball answers.

## How to Run

```bash
python3 magic8Ball.py
```

## Features

- Interactive question-and-answer format
- 13 different possible responses including:
  - "Yes"
  - "No" 
  - "Ask again later"
  - "Definitely"
  - "I wouldn't count on it"
  - And more traditional Magic 8 Ball responses
- Continuous play until you choose to exit
- Simple exit command (type 'exit' to quit)

## Requirements

- Python 3.x

## Example Usage

```
Welcome to the Magic 8 Ball!
Ask a yes or no question (or type 'exit' to quit): Will I have a good day?
The Magic 8 Ball says: Definitely

Ask a yes or no question (or type 'exit' to quit): Should I learn Python?
The Magic 8 Ball says: Without a doubt

Ask a yes or no question (or type 'exit' to quit): exit
Thanks for playing!
```

## How It Works

The application uses Python's `random` module to randomly select from a predefined list of responses, providing an authentic Magic 8 Ball experience in your terminal.