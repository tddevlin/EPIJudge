from test_framework import generic_test
import math


def find_first_greater_than_k(tree, k):
    if not tree:
        return
    smallest_key = math.inf
    smallest_node = None
    while True:
        # print(tree.data)
        if tree.data == k:
            break
        if k < tree.data:
            if tree.data < smallest_key:
                smallest_key = tree.data
                smallest_node = tree
            if tree.left:
                tree = tree.left
            else:
                break
        else:
            if tree.right:
                tree = tree.right
            else:
                break
    if tree.right:
        min_tree = find_min(tree.right)
        if min_tree.data < smallest_key:
            return min_tree
    if smallest_key > k:
        return smallest_node


def find_min(tree):
    if not tree.left:
        return tree
    else:
        return find_min(tree.left)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
