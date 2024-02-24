import datetime
import random as r
from random import randint

print(len("hello"))

def sum(a,b):
    return a+b

def diff(a,b):
    return a-b

#define with datetime
def display(a):
    mydt=datetime.datetime.now()
    print(str(mydt)+" "+a)

def greet(name, location):
    print(f"Hello Sire {name} from {location}")
    return 1
    

print(sum(2,3))
print(sum(9,3))
print(diff(2,3))
display("hello world")

greet ("Jamal", "New York")
greet("Jamal", location="Montreal")
greet(name="Charles", location="London") 

names = ["Jamal", "Charles", "John"]
locations = ["New York", "Montreal", "London"]

condition = False
i=0
while not condition:
    random_name = r.randint(0, len(names)-1)
    random_location = randint(0, len(locations)-1)
    greet(names[random_name], locations[random_location])
    if (i == 15):
        condition = True
    i+=1
