
# Recursive function to find the sum of natural numbers up to n
def evennum(number):
    print(number)
    if number % 2 == 0:
        if number == 2:
            return number
        else:
            return number * evennum(number-2)

# print(evennum(4))

def sumofnumbers(n):
    if n<=1:
     return n
    else:
     return n + sumofnumbers(n-1)

print(f"Sum of numbers is {sumofnumbers(int(input('Enter a number: ')))}")

def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# The index is: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(fibonacci(8))