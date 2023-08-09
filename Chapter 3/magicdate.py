#6 MAGIC DATE CALCULATOR

#Ask user to enter month in numeric form, a day and a two-digit year

month = int(input("Enter month in numeric form: "))
day = int(input("Enter day in numeric form: "))
year = int(input("Enter year in numeric form: "))

#Check if it's a magic date
if month * day == year:
    print(month,"/",day,"/",year, ", This is a magic date")
else:
    print("The is not a magic date")

