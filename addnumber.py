
inputnum = input("Enter a number: ")

length = len(inputnum)
total=0
for i in range (0,length):
    total+= int(inputnum[i])

print(total)