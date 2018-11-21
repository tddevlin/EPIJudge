from test_framework import generic_test
import bisect


def search_first_of_k(A, k):
    if not A:
        return -1
    lo = 0
    hi = len(A) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if A[mid] >= k:
            hi = mid
        else:
            lo = mid + 1
    if A[lo] == k:
        return lo
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
