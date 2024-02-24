import random
import my_module
even=0
odd=0

for i in range(79000):
    random_integer=random.randint(1,500)
    if (random_integer % 2 == 0):
        even += 1
    else:
        odd+=1

print(f"The total number of odd numbers is {odd} and even number is {even} and the pi value is {my_module.pi}")
