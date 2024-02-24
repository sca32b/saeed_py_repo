
for i in range(2, 100):
    square_root = i**0.5
    is_prime = True
    for j in (2, square_root):
        if i % j == 0:
            is_prime = False
    if is_prime:
      print(f"{i} is a prime number")