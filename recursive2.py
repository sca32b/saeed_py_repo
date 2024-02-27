# a list of recursive functions to help explain how recursion works!
# the number of times the function itself gets called also maps into thenumber of the base case.
# think of the call stack as a stack of plates. The last plate you put on the stack is the first one you take off.
# think of the recursion tree to think through recursion.

# 1. Factorial
def factorial(n):
# base case 0! = 1
    if n == 0:
     return 1
    else:
# recursive case
     return n * factorial (n-1)

print(factorial((int(input("Enter a number to calculate factorial: ")))))



# 2. Sum of natural numbers that are +ive
def sum (n):
# base case n = 0
    if n ==0:
     return 0
    if n < 0:
      return 0
    else:
# recursive case (head recursion)
      x = n + sum (n-1)
# processing
      print(n)
      return x
     
print(sum(int(input("Enter a number to add: "))))

# given a number n, print individual digits
def breaknum(n):
# base case eg 3//10 = 0
  if n <= 0:
    return
  else:
# recursive case (head recursion)
    x = breaknum(n//10)
    digit = n % 10
    if digit == None:
       print("None case reached")
    print(digit)
    return x

print(breaknum(int(input("Enter a number to break down digit by digit: "))))

# 4. Power of 2
def poweroftwo(n):
# base case 2^0 = 1
    if n == 0 :
      return 1
    else:
# recursive case
      return 2 * poweroftwo (n-1)
print(poweroftwo(int(input("Enter a number to calculate power of 2: "))))

# total number of ways to climb a staircase 
# given n steps, you can climb 1 or 2 steps at a time
def climbstairs(n):
  # base case if you are in the 0th step
  if n == 0:
    return 1
  # base case if you are in the negative step
  if n < 0
    return 0
  else:
    # recursive case
    return climbstairs(n-1) + climbstairs(n-2)
print(climbstairs(int(input("Enter a number of steps to climb: "))))