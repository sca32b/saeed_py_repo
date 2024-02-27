from random import randint
import time

def populate_array (array,size, maximum_value):
    for i in range(size):
        array.append(randint(1,maximum_value))
    return array

# This is an example of a function that sorts an array using the bubble sort algorithm
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

start_time = time.time()
array=[]
originalarray = populate_array(array, 20000, 20000)
array = bubble_sort(originalarray)
elapsed_time = time.time() - start_time
print(f"the bubble sorted array is {len(array)} and the time taken is {elapsed_time}")
# print(array)

# This is an example of a function that sorts an array using the insertion sort algorithm
def insertion_sort(array):
    for i in range(1,len(array)):
        j=i
        while array[j-1] > array [j] and j > 0:
                array [j], array [j-1] = array [j-1], array[j]
                print(f"j is {j} and array is {array}")
                j -= 1
    return array

start_time = time.time()
array = insertion_sort(originalarray)      
elapsed_time = time.time() - start_time
print(f"the insertion sorted array is {len(array)} and the time taken is {elapsed_time}")


# This is an example of a function that sorts an array using the selection sort algorithm
def selection_sort(array):
    current_item = 0
    for sorted_space in range(len(array)):
            minimum = sorted_space
            for current_item in range(sorted_space, len(array)):
                if (array[sorted_space] > array [current_item]):
                    minimum = current_item
            if array[sorted_space] > array [minimum]:
                array[sorted_space], array [minimum] = array[minimum], array[sorted_space]
    return array

start_time = time.time()
array = selection_sort(originalarray)
elasped_time = time.time() - start_time
print(f"the selection sorted array is {len(array)} and the time taken is {elapsed_time}")


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursively split and sort the halves
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        # Check if any element was left on the left side
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Check if any element was left on the right side
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


start_time = time.time()
array = merge_sort(originalarray)
elapsed_time = time.time() - start_time
print(f"the merge sorted array is {len(array)} and the time taken is {elapsed_time}")
