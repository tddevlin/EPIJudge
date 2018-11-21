from test_framework import generic_test, test_utils


def generate_power_set(S):
    if not S:
        return [[]]
    all_subsets = []
    for subset in generate_power_set(S[1:]):
        all_subsets.append(subset)
        all_subsets.append([S[0]] + subset)
    return all_subsets


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
