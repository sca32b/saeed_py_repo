list = [2,3,0,0,4,5,6,7,8,0,4]
counter=0
for i in list:
    if i == 0:
        print(i)
        list.remove(counter)  # remove the first occurence of 0
        list.append(0)
counter+=1
print(list)

youtuber = input("Enter the name of the youtuber: ")

print(f"subscribe to {youtuber}")
print("subscribe to {}".format(youtuber))
print("subscribe to " + youtuber)