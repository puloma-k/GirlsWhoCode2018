# --- Define your functions below! ---
from random import *

def intro():
    name = input("Hello! What's your name? ")
    print("Nice to meet you,", name)

def is_valid_input():
    while True:
        answer = input("What would you like to do? You can CHAT or PLAY rock, paper, scissors: ")
        valid_responses = ["chat", "play"]
        if answer in valid_responses:
            process_input(answer)
        elif answer == "bye":
            return answer

def rock_paper_scissors():
    gameOver = False
    while gameOver == False:
        objects = ["rock", "paper", "scissors"]
        objIdx = randint(0, len(objects) - 1)
        choice = input("Choose rock, paper, or scissors: ")
        move = objects[objIdx]
        if choice == move:
            print("Your choice: %s. My choice: %s." %(choice, move))
            print("Draw! Try again.")
        elif (choice == "rock" and move == "paper") or (choice == "paper" and move == "scissors") or (choice == "scissors" and move == "rock"):
            print("Your choice: %s. My choice: %s." %(choice, move))
            print("You lose!")
            gameOver = True
        elif (choice == "paper" and move == "rock") or (choice == "scissors" and move == "paper") or (choice == "rock" and move == "scissors"):
            print("Your choice: %s. My choice: %s." %(choice, move))
            print("You win!")
            gameOver = True
        elif choice == "bye":
            gameOver = True
            return choice
        else:
            print("That's not an option")

def process_input(answer):
    valid_greeting = ["hi", "hello", "hey", "hey there", "Hi", "Hey", "Hello", "Hey there"]
    if answer == "play":
        rock_paper_scissors()
    elif answer == "chat":
        while True:
            answer = input("What would you like to talk about? ")
            if answer in valid_greeting:
                print("Hello!")
            elif answer == "bye":
                return answer
            else:
                print("That's cool!")
    elif answer == "bye":
        return answer
    else:
        answer = input("What would you like to do? You can CHAT or PLAY rock, paper, scissors: ")

# --- Put your main program below! ---
def main():
    intro()
    is_valid_input()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
