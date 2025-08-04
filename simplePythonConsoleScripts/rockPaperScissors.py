"""
A beginner-friendly Rock Paper Scissors console game in Python. The script allows players to compete against the computer, keeps score, and includes error handling.

How it works:
1. The player enters their choice (rock, paper, or scissors)
2. The computer randomly selects its choice
3. The program determines the winner based on game rules
4. Scores are updated and displayed
5. The player can choose to play again or quit
"""

import random
import sys

def get_player_choice():
    while True:
        try:
            choice = input("\nEnter your choice (rock/paper/scissors) or 'q' to quit: ")
            if choice == 'q':
                print("Thanks for playing!")
                sys.exit()
                
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            else:
                print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            sys.exit()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def play_game():
    
    player_score = 0
    computer_score = 0
    
    print("\nWelcome to Rock, Paper, Scissors!")
    print("----------------------------------")
    
    while True:
        try:
            
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            
            
            print(f"\nYou chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            
            
            result = determine_winner(player_choice, computer_choice)
            
            if result == "tie":
                print("It's a tie!")
            elif result == "player":
                print("You win!")
                player_score += 1
            else:
                print("Computer wins!")
                computer_score += 1
            
            
            print(f"\nScore - You: {player_score} Computer: {computer_score}")
            
            
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                print("\nFinal Score:")
                print(f"You: {player_score}")
                print(f"Computer: {computer_score}")
                print("\nThanks for playing!")
                break
                
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Let's try again!")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

"""
To play the game:
1. Run the script
2. Enter your choice (rock, paper, or scissors)
3. See the result and current score
4. Choose to play again or quit

The game will continue until you choose to quit or press Ctrl+C to exit.

This implementation is suitable for beginners as it:
- Uses basic Python concepts (functions, loops, conditionals)
- Includes clear comments explaining the code
- Handles errors gracefully
- Has a simple and intuitive interface

You can run this code in any Python environment (Python 3.x recommended) and start playing immediately!"""