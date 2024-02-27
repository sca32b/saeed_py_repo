from random import randint

def selection_sort(array):
    for sorted in range(len(array)):
        minimum = sorted
        for current_item in range(sorted, len(array)):
             if (array[sorted] > array[current_item]):
                    minimum = current_item
        if minimum != sorted:
         array[sorted], array[minimum] = array[minimum], array[sorted]

array = [randint(1,10) for i in range(10)]
print(array)
selection_sort(array)
print(array)
