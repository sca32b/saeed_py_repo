a = 100
if (a > 1) and (a < 10):
    print("a is greater than 1 and less than 10")
elif(a >= 10) and (a < 100):
    print("a is greater than or equal to 10 or less than or equal to 100")
else:
    print("a is greater than  equal to 100 or less than 1")


if a!=100:
    print("a is not equal to 100")
else:
    print("a is equal to 100")

if a==100:
    print("a is equal to 100")

name = "ADIL"
citizenship = "CANADA"

if not name.lower() == "jamal".lower():
    print("Your name is not Jamal")
elif name.lower() == "adil".lower():
    print("Your name is Adil")
    if citizenship.lower() == "usa".lower():
        print("You are a US citizen")
    else:
        print("You are not a US citizen")
else:
    print("Your name is not Jamal")




num=input("Please enter a number between 1 and 10\n")
if (int(num) %2 == 0):
    print ("The number is even")
else:
    print("The number is odd")