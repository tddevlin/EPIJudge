import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    i = 0
    j = len(A) - 1
    k = len(A) - 1
    pivot = A[pivot_index]
    while i <= j:
        if A[i] < pivot:
            i += 1
        elif A[i] > pivot:
            A[i], A[j], A[k] = A[j], A[k], A[i]
            k -= 1
            j -= 1
        else:
            A[i], A[j] = A[j], A[i]
            j -= 1


# def dutch_flag_partition(pivot_index, A):
#     pivot = A[pivot_index]
#     n = len(A)
#     less_index = 0
#     i = 0
#     greater_index = n - 1
#     while i <= greater_index:
#         if A[i] < pivot:
#             A[i], A[less_index] = A[less_index], A[i]
#             less_index += 1
#             i += 1
#         elif A[i] > pivot:
#             A[i], A[greater_index] = A[greater_index], A[i]
#             greater_index -= 1
#         else:
#             i += 1
#     return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
