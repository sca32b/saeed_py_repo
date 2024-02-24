print("Welcome to the tip calculator.")
total_bill=float(input("what was the total bill?"))
no_of_people=int(input("how many people are there to split the bill?"))
tip_percentage=float(input("what percentage tip would you like to give? 10, 12, or 15?"))
tip_percentage=tip_percentage/100
total_tip=total_bill*tip_percentage
print("Each person should pay:   " + str((total_bill+total_tip)/no_of_people))

# always starts wit zero
# subscripting
a_string = "Hello World!"[4]
print(a_string)
#replace commas with underscores
b_int = 39
b_float = 3.2333
print(b_int + b_float)

a_bool = True

print(type(b_float))
print(36+int(b_float))

two_digit_no = input("please enter a two digit number and I will add them")
print("The sum of the two digits is " + str(int(two_digit_no[0])+int(two_digit_no[1])
