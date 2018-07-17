def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 56468, 621, 8, 444, 8794531, 6543]))
