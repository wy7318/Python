import datetime

def Auto_todayOD(input):
    current_time = datetime.datetime.now()

    if "/" in input:
        if input.count("/") == 1:
            month = input.split("/")[0]     # Number before /
            date = input.split("/")[1]      # Number after /
            year = current_time.year
            print(month + "-" + date + "-" + str(year))
        elif input.count("/") == 2:
            month = input.split("/")[0]     # Number before /
            date = input.split("/")[1]      # Number after /
            year = input.split("/")[2]      # Number after /
            print(month + "-" + date + "-" + year)
        else:
            print("Incorrect Format")
    else:
        print("Incorrect Format")


date = input("Enter : ")
Auto_todayOD(date)
