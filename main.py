from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess,actual_number,turns):
    if user_guess > actual_number:
        print("Too High!")
        return turns - 1
    elif user_guess < actual_number:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_number}.")
        
# Function to set difficulty
def set_difficulty():
    level = input("Choose a dicciculty. Type 'esay' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
       return HARD_LEVEL_TURNS  
      
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()
    # Let the user guess a number
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guees the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guess, You lose.")
            return
        elif guess != answer:
            print('Guess again.')
game()