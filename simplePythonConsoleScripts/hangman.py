# simple hangman game
import random   
def get_random_word():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words) 

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           
           
           
           
           
        """,
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)  
    
    while not guessed and tries > 0:    
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries -= 1
        
        print(display_hangman(tries))
        print(word_completion)
        
        if "_" not in word_completion:
            guessed = True
    if guessed:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Sorry, you've run out of tries. The word was:", word)
if __name__ == "__main__":
    play_hangman()  

# This script implements a simple hangman game where the player guesses letters to complete a word.
# The player has a limited number of incorrect guesses before losing the game.