

def isLeapYear(year):
    """This is a test function
    This function checks if the year is a leap year"""  
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

year=int(input("Enter a year: "))
month=int(input("Enter a month (in number): "))

if month > 12:
    print("Invalid month")
    exit()


if isLeapYear(year) and int(month) == 2:
    print(f"{year} is a leap year and February has 29 days")
else:
    print(f"{year} and {months[int(month)-1]} has {days_in_month[int(month)-1]} days")
