year = int(input("enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("is the leap year".format(year))
elif(year % 4 == 0) and (year % 100 != 0):
    print("is the leap year".format(year))
else:
    print("is the not leap year".format(year))