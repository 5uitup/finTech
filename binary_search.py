def binary_search(sorted_list, item):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


lis = [1, 8446, 5, 542, 4128]
lis.sort()
print(lis)
print(binary_search(lis, 542))
