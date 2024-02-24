heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
totalheight = 0
highestnumber = 0
for height in heights:
    totalheight += height
    if height > highestnumber:
        highestnumber = height
averageheight = totalheight / len(heights)
print(averageheight)
print(highestnumber)

for i in range(1,90,10):
    print(f"Hello {i}")
total=0
for i in range(100):
    if i % 2 == 0:
       total+=i
print(total) 

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)

# will only print odd numbers
a=0
while a < 100:
    a+=1
    if a % 2 != 0:
        continue
    print(a)