from random import randint

def insertion_sort(array):
    for i in range(1,len(array)):
        j=i
        while array[j-1] > array[j] and j > 0:
            array[j-1], array [j] = array [j], array [j-1]
            j-=1
    return array
array=[4,5,3,2,1,7]

print(insertion_sort(array))