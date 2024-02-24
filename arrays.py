#Example array / list
from random import randint
testlist=[]
for i in range(0,30,2):
    if len(testlist)==0:
        testlist.append(randint(1,100))
    else:
        randlocation=randint(0,len(testlist)-1)
        testlist.insert(randlocation,randint(1,100))
print(testlist)

#remove the first element from the list
removed=testlist.pop(0)
print(f"The first element {removed} is removed: {testlist}")

#remove the last element from the list
removed=testlist.pop()
print(f"The last element {removed} is removed: {testlist}")

#Dictionary
names = ["John", "James", "Jack", "Jill", "Jenny", "Charles", "Charlie", "Chad", "Chloe", "Cheryl]
ages = [34, 23, 45, 32]
locations = ["New York", "California", "Texas", "Florida", "New Jersey"]

LocationArray = []

#Create a list of dictionaries
for i in range(10):
    recordset = {}
    #Create a dictionary
    randomname = randint(0, len(names)-1)
    randomages = randint(0, len(ages)-1)
    randomlocations = randint(0, len(locations)-1)

    recordset["Name"] = names[randomname]
    recordset["Age"] = ages[randomages]
    recordset["Location"] = locations[randomlocations]

    LocationArray.append(recordset)

print(LocationArray)
print(LocationArray[0]["Location"])


