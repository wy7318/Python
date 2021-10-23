def Auto_todayOD(input):
    current_time = datetime.datetime.now()

    if "/" in input:                        # If input contain '/'
        if input.count("/") == 1:           # If mm/dd format
            month = input.split("/")[0]     # Number before /
            date = input.split("/")[1]      # Number after /
            year = current_time.year
            # Check and catch if date format is correct using datetime
            try:
                t = month + "-" + date + "-" + str(year)
                t2 = datetime.datetime.strptime(t,"%m-%d-%Y")
                finalT = str(t2.strftime('%m-%d-%Y'))
                print(finalT)
            except:
                print("Error")

        elif input.count("/") == 2:         # If mm/dd/yy or mm/dd/yyyy format
            month = input.split("/")[0]     # Number before /
            date = input.split("/")[1]      # Number after /
            year = input.split("/")[2]      # Number after /
            if len(year) == 2:              # /YY format
                try:
                    t = month + "-" + date + "-" + "20" + str(year)
                    t2 = datetime.datetime.strptime(t,"%m-%d-%Y")
                    finalT = str(t2.strftime('%m-%d-%Y'))
                    print(finalT)
                except:
                    print("Error")
            elif len(year) == 4:            # /YYYY format
                try:
                    t = month + "-" + date + "-" + year
                    t2 = datetime.datetime.strptime(t,"%m-%d-%Y")
                    finalT = str(t2.strftime('%m-%d-%Y'))
                    print(finalT)
                except:
                    print("Error")
            else:
                print("Incorrect Format")
        else:
            print("Incorrect Format")
    else:
        print("Incorrect Format")
        
date = input("Enter : ")
Auto_todayOD(date)
