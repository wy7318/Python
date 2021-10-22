import datetime

def Auto_todayOD(input):
    current_time = datetime.datetime.now()

    if "/" in input:
        if input.count("/") == 1:           # Count how many '/' is included to distinguish m/d or m/d/y format
            month = input.split("/")[0]     # Number before /
            date = input.split("/")[1]      # Number after /
            year = current_time.year
            if int(month) > 12 or int(date) > 31:
                print("Incorrect Month")
            else:
                print(month + "-" + date + "-" + str(year))
        elif input.count("/") == 2:
            month = input.split("/")[0]     # Number before /
            date = input.split("/")[1]      # Number after /
            year = input.split("/")[2]      # Number after /
            if int(month) > 12 or int(date) > 31:       #Check if month and date is not out of format
                print("Incorrect Month")
            else:
                if len(year) == 2:                      #Check if year format. 2 or 4 digit
                    print(month + "-" + date + "-" + "20" + str(year))
                elif len(year) == 4:
                    print(month + "-" + date + "-" + year)
                else:
                    print("Incorrect Format")
        else:
            print("Incorrect Format")
    else:
        print("Incorrect Format")


date = input("Enter : ")
Auto_todayOD(date)
