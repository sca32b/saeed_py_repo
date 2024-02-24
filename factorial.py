
# This is a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n-1)

final = factorial(300)
print("The result is " + str(final))

