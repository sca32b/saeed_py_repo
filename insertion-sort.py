array=[4,5,3,2,1]

def insertion_sort(array):
    for i in range(1, len(array)):
        j=i
        while array[j-1] > array [j] and j> 0:
            array [j], array [j-1] = array [j-1], array [j]
            j -=1
    return array


print(insertion_sort(array))
