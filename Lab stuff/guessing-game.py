import random
guess = random.randint(1,100)
while True:
    userguess = int(input("Enter your guess"))
    if userguess < guess:
        print("Try a bigger number")
    elif userguess > guess:
        print("Try a smaller number")
    else:
        print("You got it")
        break