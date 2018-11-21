from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    # full_array = []
    # for array in sorted_arrays:
    #     for i in range(len(array)):
    #         heapq.heappush(full_array, array[i])
    # return heapq.nsmallest(len(full_array), full_array)
    array_heap = []
    for array in sorted_arrays:
        heapq.heappush(array_heap, (array[0], array))
    full_array = []
    while array_heap:
        smallest_elt, smallest_array = heapq.heappop(array_heap)
        smallest_array.pop(0)
        full_array.append(smallest_elt)
        if smallest_array:
            heapq.heappush(array_heap, (smallest_array[0], smallest_array))
    return full_array


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
