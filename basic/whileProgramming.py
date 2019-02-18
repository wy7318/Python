available_exit=["east", "west", "north", "south"] #creating list
choosen_exit=""
while choosen_exit not in available_exit:
    choosen_exit=input("please choose direction:")
    if choosen_exit == "exit":
        print("game over")
        break
else:
    print("glad you got out")

###################################################################################
    
#guessing number 
import random

highest = 10
answer = random.randint(1, highest)

print("guess a number between 1 and {}".format(highest))
guess = int(input())

while guess != answer:
    if guess != answer:
        if guess < answer:
            print("please guess higher")
        else:
            print("guess lower")
        guess = int(input())
    if guess == answer:
        print("Well done")
        break
else:
    print("got it right first time")
