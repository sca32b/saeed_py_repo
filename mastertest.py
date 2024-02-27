
import datetime

def height_calc():
 heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
 totalheight = 0
 highestnumber = 0
 for hgt in heights:
   totalheight += hgt
 print (f"Total height is {totalheight}")
 if (hgt > highestnumber):
   highestnumber = hgt
 print (f"Highest number is {highestnumber}")
 # arrange the heights in ascending order
 
 

def bmi_calc():
 height=input("Enter your height in m: ")
 weight=input("Enter your weight in kg: ")

 print (f"your height is of type {type(height)}")

 bmi = int(weight) / float(height) ** 2

 print (f"your BMI is today {datetime.datetime.now()} is {bmi}")

 if (bmi < 3):
  print("You are underweight !!")
 elif (bmi >= 3 ) and (bmi < 5):
  print("You are normal weight")
 else :
  print("You are overweight")  


bmi_calc()
height_calc()