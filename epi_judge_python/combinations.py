from test_framework import generic_test, test_utils


def combinations(n, k):
    if k == 0:
        return [[]]
    if n == k:
        return [[i for i in range(1, n+1)]]
    all_combinations = []
    all_combinations.extend(combinations(n-1, k))
    for combination in combinations(n-1, k-1):
        all_combinations.append([n] + combination)
    return all_combinations


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
