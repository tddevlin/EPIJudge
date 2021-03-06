from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    if not tree:
        return []
    k_largest = find_k_largest_in_bst(tree.right, k)
    if len(k_largest) < k:
        k_largest.append(tree.data)
    if len(k_largest) < k:
        k_largest.extend(find_k_largest_in_bst(tree.left, k - len(k_largest)))
    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
