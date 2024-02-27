
a=[3,5]
b=[4,6]
merged=[]

def merge_two_arrays(a, b):
    i=j=0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            j+=1
    
    while i < len(a):
        merged.append(a[i])
        i+=1
    while j < len(b):
        merged.append(b[j])
        j+=1

    return merged

print(merge_two_arrays(a, b))