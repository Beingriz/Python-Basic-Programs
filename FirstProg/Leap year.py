#prog to find leap year

while True:
    year = input("Enter the year\n")
    if(year=="Exit"):
        break
    try:
        iyear=int(year)
        if (iyear%4==0):
           if(iyear%100==0):
               if(iyear%400==0):
                   print("It is leap year")
               else:
                print("Not a leap year")
           else:
                print("It is a leap year")
        else:
              print("It is not a leap year")
    except:
        print("Invalid year")
        continue
