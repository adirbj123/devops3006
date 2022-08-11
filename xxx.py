from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts_left = EASY_LEVEL_TURNS
    else:
        attempts_left = HARD_LEVEL_TURNS
    return attempts_left


def guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    number = randint(1, 100)
    print(f"Pssst, the correct answer is {number}")

    attempts_left = set_difficulty()

    continue_guessing = True
    while continue_guessing:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            continue_guessing = False
        else:
            if guess < number:
                print("Too low.")
            else:
                print("Too high.")

            attempts_left -= 1
            if attempts_left == 0:
                print("You've run out of guesses, you lose.")
                continue_guessing = False
            else:
                print("Guess again.")


guessing_game()
