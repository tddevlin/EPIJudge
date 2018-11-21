from test_framework import generic_test, test_utils


def permutations(A):
    if len(A) == 1:
        return [A]
    permutation_list = []
    for i in range(len(A)):
        rest_permutations = permutations(A[:i] + A[i+1:])
        for permutation in rest_permutations:
            permutation_list.append([A[i]] + permutation)
    return permutation_list


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
