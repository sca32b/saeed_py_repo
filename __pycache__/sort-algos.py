from random import randint
import time

def populate_array (array,size, maximum_value):
    for i in range(size):
        array.append(randint(1,maximum_value))
    return array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

start_time = time.time()
array=[]
array = populate_array(array, 10_000, 10000)
array = bubble_sort(array)
elapsed_time = time.time() - start_time
print(f"the bubble sorted array is {len(array)} and the time taken is {elapsed_time}")
# print(array)

def insertion_sort(array):
    print(f"unsorted array is {array} with length {len(array)}")
    for i in range(1,len(array)):
        j=i
        while array[j-1] > array [j] and j > 0:
                array [j], array [j-1] = array [j-1], array[j]
                print(f"j is {j} and array is {array}")
                j -= 1
    return array


for i in range(20):
    array=[]
    array = populate_array(array, 5, 5)
    array = insertion_sort(array)      
    print(array)