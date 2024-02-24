height = input()
weight = input()

# convert to metric units

def lbs_to_kg(lbs):
    return float(lbs) * 0.45

def in_to_m(inches):
    return float(inches) * 0.025


bmi = int(lbs_to_kg(weight)) / float(in_to_m(height)) ** 2

if (bmi < 18.5):
    print("You are underweight")
elif (bmi >= 18.5) and (bmi < 25):
    print("You are normal weight")
elif (bmi >= 25) and (bmi < 30):
    print("You are overweight")
else:
    print("You are obese")

print(round(bmi))

z=3.444
print(round(z,2))
a = 24
a /=2
print(a)
print ( 8 // 3)