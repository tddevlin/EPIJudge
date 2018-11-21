def binary_search(sorted_array, target):
    if not sorted_array:
        return False
    if len(sorted_array) == 1:
        return sorted_array[0] == target
    middle_index = len(sorted_array) // 2
    pivot = sorted_array[middle_index]
    if pivot == target:
        return True
    if pivot < target:
        return binary_search(sorted_array[middle_index+1:], target)
    return binary_search(sorted_array[:middle_index], target)


a = [1, 2, 3, 4]
print(binary_search(a, 3))