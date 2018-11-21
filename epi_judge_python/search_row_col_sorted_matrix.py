from test_framework import generic_test
import numpy as np


def matrix_search(A, x):
    return matrix_search_np(np.array(A), x)


def matrix_search_np(A, x):
    if A.size == 0:
        return False
    m = len(A)
    n = len(A[0])
    if m == n == 1:
        return A[0, 0] == x
    if A[m // 2, n // 2] == x:
        return True
    elif A[m // 2, n // 2] > x:
        return any([
            matrix_search(A[:m // 2, :n // 2], x),
            matrix_search(A[m // 2:, :n // 2], x),
            matrix_search(A[:m // 2, n // 2:], x),
        ])
    else:
        return any([
            matrix_search(A[m // 2:, n // 2:], x),
            matrix_search(A[m // 2:, :n // 2], x),
            matrix_search(A[:m // 2, n // 2:], x),
        ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
