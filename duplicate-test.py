

z = [7,7,8,9,12]

rem=[]
dup=[]

print(rem)
print(dup)

for i in range(len(z)):
    if z.count(i) > 1:
        if z[i] not in dup:
            dup.append(z[i])
    else:
        rem.append(z[i])
