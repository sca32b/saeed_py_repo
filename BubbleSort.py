from random import randint

def bubble_sort(array):
  for i in range(len(array)):
    for (j) in range(len(array)-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]

array=[7,6,5,4,3,2,1]

bubble_sort(array)
print(array)