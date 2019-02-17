available_exit=["east", "west", "north", "south"] #creating list
choosen_exit=""
while choosen_exit not in available_exit:
    choosen_exit=input("please choose direction:")
    if choosen_exit == "exit":
        print("game over")
        break
else:
    print("glad you got out")
