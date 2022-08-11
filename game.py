#Gusse game
import random



#computer choose a number
secret = random.randint(0,10)


#user choose a number
user = int(input("please enter your number"))



if secret == user:
    print("you win, my number is", secret)
else:
    print("Incorrect, try again", secret)
    #user choose a number
    user = int(input("please enter your number, again"))
    if secret == user:
     print("You won, my number is", secret)
    else:
        print("You lose, my number is", secret, "your number is", user)
    print("end")


