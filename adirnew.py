import random

LIMIT = 5

   def display_title():
    print("Guess the number!")
    print()

    def get_name():
    player_name = input("What is yor name? ")
    print("Hello", player_name)

    def play_game():
    number = random.randit(1, LIMIT)
    print("Choose a number from 1 to " + str(LIMIT) + "\n")
    count = 1
    while True:
    guess = int(input("Your guess: "))
    if guess < number:
    print("Too low.")
    count += 1
    elif guess > number:
    print("Too high.")
    elif guess == number:
    print("You gussed it in " + str(count) + "tries.\n")
    return
    def main():
    display_title()
    get_name()
    again = "y"
    while again.lower() == "y"
    play_game()
    again = input("Would you like to play again? (y/n): ")
    print()
    print("Bye!")

    if _name_ == "_main_":
    main()



