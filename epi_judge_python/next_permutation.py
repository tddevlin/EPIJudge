from test_framework import generic_test

# 0 1 -> 1 0
# 0123 -> 0132
# 3120 -> 3210
# 2310 -> 3012


def next_permutation(perm):
    if len(perm) <= 1:
        return []
    first_unsorted = -1
    max_so_far = perm[-1]
    for i in range(len(perm)-1, -1, -1):
        if perm[i] < max_so_far:
            first_unsorted = i
            break
        max_so_far = max(max_so_far, perm[i])
    if first_unsorted == -1:
        return []
    for i in range(first_unsorted, len(perm)):
        end_perm = next_permutation(perm[len(perm) - i:])
        if end_perm:
            return perm[:len(perm) - i] + end_perm
    next_largers = [(x, i + 1) for i, x in enumerate(perm[1:]) if x > perm[0]]
    if next_largers:
        max_in_rest, index = min(next_largers)
        perm[0], perm[index] = max_in_rest, perm[0]
        perm[1:] = sorted(perm[1:])
        return perm
    return []


def smallest_perm_with_elements(array):
    perm = []
    for i in range(len(array)):
        if array[i]:
            perm.append(i)
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
