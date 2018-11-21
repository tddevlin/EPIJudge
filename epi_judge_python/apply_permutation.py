from test_framework import generic_test


def apply_permutation(perm, A):
    is_permuted = [False] * len(A)
    for i in range(len(A)):
        old_index = i
        moving_element = A[i]
        while not is_permuted[old_index]:
            new_index = perm[old_index]
            new_moving_element = A[new_index]
            A[new_index] = moving_element
            is_permuted[old_index] = True
            old_index = new_index
            moving_element = new_moving_element
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
