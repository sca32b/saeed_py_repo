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

array = [7,3,6]
print(array)
print(merge_sort(array))
