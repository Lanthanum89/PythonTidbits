# magic 8 ball application
import random   
def magic_8_ball():
    responses = [
        "Yes",
        "No",
        "Ask again later",
        "Definitely",
        "I wouldn't count on it"
        "The stars are hazy, try again",
        "Absolutely",
        "My sources say no",
        "It is certain",
        "Outlook not so good",
        "Yes, in due time",
        "Very doubtful",
        "Without a doubt",  
    ]
    return random.choice(responses)

if __name__ == "__main__":
    print("Welcome to the Magic 8 Ball!")
    while True:
        question = input("Ask a yes or no question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Thanks for playing!")
            break
        answer = magic_8_ball()
        print(f"The Magic 8 Ball says: {answer}")   
        


