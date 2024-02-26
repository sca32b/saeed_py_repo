
# Purpose: To find the duplicates in a list

j = [5,6,7,8,9,2,3,5,6,7,9]
d = []
uni=[]


for i in range(len(j)):
  count = 0
  for b in range(i+1,len(j)):
    if j[i] == j[b]:  
      count += 1
      print(count, j[i])
      if j[i] not in d:
        d.append(j[i])

  if count == 0 and j[i] not in uni and j[i] not in d:
    uni.append(j[i])
print(d)
print(uni)

d=[]
uni=[]
for ele in j:
  if j.count(ele) > 1 and ele not in d:
    d.append(ele)
  elif j.count(ele) == 1 and ele not in uni:
    uni.append(ele)
print(d)   
print(uni)
