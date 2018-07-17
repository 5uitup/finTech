def find_smallest(lis):
    smallest = lis[0]
    smallest_index = 0
    for i in range(len(lis)):
        if lis[i] < smallest: smallest, smallest_index = lis[i], i
    return smallest_index


def selection_sort(lis):
    new_list = []
    for i in range(len(lis)):
        smallest = find_smallest(lis)
        new_list.append(lis.pop(smallest))
    return new_list


print(selection_sort([1, 45455, 545, 8777777, 551]))
