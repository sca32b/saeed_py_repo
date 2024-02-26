from random import randint

uni = []
dup = []


for i in range(1000):
    next_num = randint(1, 1000)
    if next_num not in dup and next_num not in uni:
        uni.append(next_num)
    elif next_num in uni:
        uni.remove(next_num)
        dup.append(next_num)
    else:
        dup.append(next_num)

print(f"Unique numbers: {uni}")
print(f"Duplicate numbers: {dup}")
print(f"Total unique numbers: {len(uni)}")
print(f"Total duplicate numbers: {len(dup)}")


