from test_framework import generic_test


def search_smallest(A):
    n = len(A)
    if n == 1:
        return 0
    jump_size = n // 2
    jump_right = True
    i = 0
    j = 1
    while A[i] < A[j]:
        if jump_right:
            new_i = (i + jump_size) % n
            new_j = (new_i + 1) % n
        else:
            new_i = (i - jump_size) % n
            new_j = (new_i + 1) % n
        if A[new_i] > A[i]:
            jump_right = True
        else:
            jump_right = False
        i = new_i
        j = new_j
        jump_size = max(1, jump_size // 2)
    return j


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
