
l = [545,3,4,5,6,72,3,4,5,67,67,67]
rem_list = []
dup_list = []

for i in l:
    if l.count(i) == 1:
        rem_list = rem_list + [i]
   
print(rem_list)

for i in range(len(l)):
    count = 0
    for b in range(i+1,len(l)):
        if l[i] == l[b]:
            count += 1
            if l[i] not in dup_list:
                dup_list = dup_list + [l[i]]
    if count ==0 and l[i] not in rem_list and l[i] not in dup_list:
        rem_list = rem_list + [l[i]]
print(rem_list) 

print(dup_list)