from test_framework import generic_test
import heapq


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    # k_largest = A[:k]
    # heapq.heapify(k_largest)
    # for i in range(k, len(A)):
    #     heapq.heappushpop(k_largest, A[i])
    # return heapq.nsmallest(1, k_largest)[0]
    pass

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
