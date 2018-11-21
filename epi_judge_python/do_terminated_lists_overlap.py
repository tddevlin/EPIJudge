import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    if not l0:
        return l0
    if not l1:
        return l1
    step0 = l0
    step1 = l1
    length0 = length1 = 0
    while step0:
        length0 += 1
        step0 = step0.next
    while step1:
        length1 += 1
        step1 = step1.next
    if length0 < length1:
        for _ in range(length1 - length0):
            l1 = l1.next
    elif length1 < length0:
        for _ in range(length0 - length1):
            l0 = l0.next
    while l0:
        if l0 == l1:
            return l0
        l0 = l0.next
        l1 = l1.next
    return None

# # correct but slow: O(mn)
# def overlapping_no_cycle_lists(l0, l1):
#     if not (l0 and l1):
#         return None
#     last0 = l0
#     while last0.next:
#         last1 = l1
#         while last1.next:
#             if last0 == last1:
#                 return last0
#             last1 = last1.next
#         last0 = last0.next
#     return None




@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
