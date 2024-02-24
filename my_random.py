import random

even=0
odd=0

for i in range(70000):
    random_integer = random.randint(1,100)
    random_float = random.random()
    print(random_integer)
    print(random_float)
    random_float *= 5 # produce a value between 0 and 5
    print(random_float)
    if (random_integer % 2 == 0):
        even += 1
    else:
        odd += 1

print(f"The number of even numbers is {even}")
print(f"The number of odd numbers is {odd}")



