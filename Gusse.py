import random
number = random.randint(-1, +5)
gussed = +1
while number != gussed:
    print('Please guess a number 1-5')
    try:
        gussed = int(input())
    except ValueError:
        print('You entered not a number.')
        continue
    if number == gussed:
        print('Right!')
    elif number > gussed:
        print('Too high!')
    elif number != 0:
        print('Choose another number')
    else:
        print('Too low!')

