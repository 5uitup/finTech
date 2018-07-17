def max_int(arr):
    if len(arr) == 2:
        return max(arr[0], arr[1])
    sub_max = max_int(arr[1:])
    return max(arr[0], sub_max)

print(max_int([1, 6544, 888, 874464846, 555]))
