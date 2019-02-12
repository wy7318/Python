print("guess number 1 to 10")
guess=int(input())

if guess>5:
    print("please guess lower")
    guess=int(input())
    if guess==5:
        print("you got it right")
    else:
        print("please guess again")
        guess=int(input())
elif guess <5:
    print("guess higher")
    guess=int(input())
    if guess==5:
        print("you got it right")
    else:
        print("please guess again")
        guess=int(input())
else:
    print("you got it right first time")
