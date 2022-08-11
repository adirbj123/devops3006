import random
words = ['laptop', 'python', 'pycharm', 'youtube', 'projects', 'travel', 'salsa']

random_word = random.choice(words)
print('our random word', random_word)
print('********** WORD GUESSING GAME **********')

user_guesses = ''
chances = 10

while chances > 0:
    wrong_guesses = 0
    for charcter in random_word:
        if charter in user_guesses:
            print(f"correct guess: {charcter}")
        else:
            wrong_guesses += 1
            print('_')
