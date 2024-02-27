a = [5,6,7,7,8,9,9]
rem = []
dup = []

for i in range (len(a)):
    if a.count(a[i]) == 1:
        rem.append(a[i])
    elif a.count(a[i]) > 1 and a[i] not in dup:
        rem.append(a[i])
        dup.append(a[i])

print(rem)
print(dup)