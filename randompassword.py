import random

numbers=[1,2,3,4,5,6,7,8,9,10]
symbols=["*","/","+","-"]
letters=["a","b","c","d","e","f","g","h","i","j"]
choice=["numbers","symbols","letters"]

num_of_numbers=int(input("How many numbers do you want in your password? "))
num_of_symbols=int(input("How many symbols do you want in your password? "))
num_of_letters=int(input("How many letters do you want in your password? "))

total_password_length = num_of_numbers + num_of_symbols + num_of_letters
running_total = total_password_length
password=""
for i in range(num_of_numbers):
    password += str(random.choice(numbers))
for i in range(num_of_symbols):
    password += random.choice(symbols)
for i in range(num_of_letters):
    password += random.choice(letters)

print(password)

password=""

while running_total > 0:
    random_choice = random.choice(choice)
    if random_choice == "numbers":
        if num_of_numbers > 0:
            password += str(random.choice(numbers))
            num_of_numbers -= 1
            running_total -= 1
    elif random_choice == "symbols":
        if num_of_symbols > 0:
            password += random.choice(symbols)
            num_of_symbols -= 1
            running_total -= 1
    else:
        if num_of_letters > 0:
            password += random.choice(letters)
            num_of_letters -= 1
            running_total -= 1

print(password)
