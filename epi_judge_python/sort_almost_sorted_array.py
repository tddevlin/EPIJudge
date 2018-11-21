from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence, k):
    k_heap = []
    return_list = []
    for _ in range(k):
        heapq.heappush(k_heap, next(sequence))
    next_item = next(sequence, None)
    while isinstance(next_item, int):
        return_list.append(heapq.heappushpop(k_heap, next_item))
        next_item = next(sequence, None)
    return_list.extend(heapq.nsmallest(len(k_heap), k_heap))
    return return_list


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
