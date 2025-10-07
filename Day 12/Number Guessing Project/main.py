from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_ans , actual_ans , turns):
    """Checks answer against guess , returns the number of turns remaining."""
    if user_ans > actual_ans:
        print("Too High")
        return turns - 1
    elif user_ans < actual_ans:
        print("Too Low ")
        return turns - 1
    else:
        print(f"Your guess {actual_ans} is correct.🥳")

def set_difficulty():
    """Sets the number of attempts or turns with respect to the difficultly level chosen by the user."""
    diff_level = input("Choose a difficulty level. Type 'e' for easy or 'h' for hard.")

    if diff_level == 'e':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to my number guessing game (●'◡'●)!!")
    print("I am thinking of a number between 1 and 100.🤔")

    num = random.randint(1,100)
    print(num)

    turns = set_difficulty()

    guess = 0
    while guess != num:
        print(f"You've have {turns} attempts remaining to guess the number.")
        guess = int(input("MAKE A GUESS: "))
        check_answer(guess , num , turns)
        if turns == 0:
            print("You've run out of guesses , you lose.😭")
            return
        elif guess != num:
            print("Guess again.")


game()