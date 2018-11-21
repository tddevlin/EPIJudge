from test_framework import generic_test
from epi_judge_python.list_node import ListNode
import sys

sys.setrecursionlimit(40000)


def merge_two_sorted_lists(L1, L2):
    if not L1:
        return L2
    if not L2:
        return L1
    if L1.data < L2.data:
        L1.next = merge_two_sorted_lists(L1.next, L2)
        return L1
    L2.next = merge_two_sorted_lists(L1, L2.next)
    return L2


# recursive approach: encounters stack overflow for large test cases
# def merge_two_sorted_lists(L1, L2):
#     if not L1:
#         return L2
#     elif not L2:
#         return L1
#     if L1.data < L2.data:
#         sorted_rest = merge_two_sorted_lists(L1.next, L2)
#         L1.next = sorted_rest
#         return L1
#     else:
#         sorted_rest = merge_two_sorted_lists(L1, L2.next)
#         L2.next = sorted_rest
#         return L2


# def merge_two_sorted_lists(L1, L2):
#     head = ListNode()
#     tail = head
#     while L1 and L2:
#         if L1.data < L2.data:
#             tail.next = L1
#             tail = L1
#             L1 = L1.next
#         else:
#             tail.next = L2
#             tail = L2
#             L2 = L2.next
#     if not L1:
#         tail.next = L2
#     elif not L2:
#         tail.next = L1
#     return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
