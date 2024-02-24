numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["John", "Jane", "Joe", "Jill", "Jack", "Jim", "Duclos"]
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
ages = {"John": 30, "Jane": 25, "Joe": 28, "Jill": 22, "Jack": 32, "Jim": 27, "Zack" : 12}
addresses = {"John": "1 Oak Street", "Jane": "2 Elm Street", "Joe": "3 Pine Street", "Jill": "4 Cedar Street", "Jack": "5 Maple Street", "Jim": "6 Birch Street"}


print(f"The maximum number in the list is {max(numbers)}")
print(f"The maximum name in the list is {max(names)}")
print(f"The maximum name by length in the list is {max(names, key=len)}")
print(f"The maximum age is {max(ages, key=ages.get)}")
print(f"The maximum address is {max(addresses, key=addresses.get)}")
print(f"The maximum key in ages is  {max(ages, key=ages.get)}")