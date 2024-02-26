


def factorial(n):
    if n == 0:
     return 1
    else:
     return n * factorial (n-1)

print(factorial((int(input("Enter a number to calculate factorial: ")))))


def sum (n):
    if n ==0:
     return 0
    if n < 0:
      return 0
    else:
      x = n + sum (n-1)
      print(n)
      return x
     
print(sum(int(input("Enter a number to add: "))))


def breaknum(n):
  if n <= 0:
    return
  else:
    x = breaknum(n//10)
    digit = n % 10
    if digit == None:
       print("None case reached")
    print(digit)
    return x

print(breaknum(int(input("Enter a number to break down digit by digit: "))))

def poweroftwo(n):
    if n == 0 :
      return 1
    else:
      return 2 * poweroftwo (n-1)
print(poweroftwo(int(input("Enter a number to calculate power of 2: "))))