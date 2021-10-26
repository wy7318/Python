import datetime


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
                finalT = str(t2.strftime('%Y-%m-%d'))
                return finalT
            except:
                pass

        elif input.count("/") == 2:         # If mm/dd/yy or mm/dd/yyyy format
            month = input.split("/")[0]     # Number before /
            date = input.split("/")[1]      # Number after /
            year = input.split("/")[2]      # Number after /
            if len(year) == 2:              # /YY format
                try:
                    t = month + "-" + date + "-" + "20" + str(year)
                    t2 = datetime.datetime.strptime(t,"%m-%d-%Y")
                    finalT = str(t2.strftime('%Y-%m-%d'))
                    return finalT
                except:
                    pass
            elif len(year) == 4:            # /YYYY format
                try:
                    t = month + "-" + date + "-" + year
                    t2 = datetime.datetime.strptime(t,"%m-%d-%Y")
                    finalT = str(t2.strftime('%Y-%m-%d'))
                    return finalT
                except:
                    pass
            else:
                print("1000-01-01")
        else:
            print("1000-01-01")
    else:
        print("1000-01-01")


import mysql.connector
from mysql.connector import MySQLConnection, Error,connect

def AutoDBDateChange():
    conn = mysql.connector.connect(host="00.00.00.000",
                                   user="user",
                                   password="pwd",
                                   database="Sales"
                                   )
    c = conn.cursor()
    idxq = "SELECT orderD FROM orders WHERE idx = %s"      # Getting index SQL
    updateq = "UPDATE orders SET orderD = %s WHERE idx = %s"        # Updating formatted date to corresponding index SQL

    try:
        for i in range(16, 1500):         # Setting Range of index
            try:
                # Getting Index First
                dateVal = (i,)
                c.execute(idxq, dateVal)
                so = c.fetchone()
                print(Auto_todayOD(so[0]))
                # Updating formatted value to corresponding index
                updatedDate = (Auto_todayOD(so[0]), i)
                c.execute(updateq, updatedDate)
                conn.commit()
            except:                 # Pass if error occur
                pass
    except mysql.connector.Error as error:  #Explain the SQL error
        print(error)

AutoDBDateChange()
