from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    if tree.left:
        if tree_min_max(tree.left, max) > tree.data:
            return False
        if not is_binary_tree_bst(tree.left, low_range, high_range):
            return False
    if tree.right:
        if tree_min_max(tree.right, min) < tree.data:
            return False
        if not is_binary_tree_bst(tree.right, low_range, high_range):
            return False
    return True


def tree_min_max(tree, min_max):
    bests = []
    if tree.left:
        bests.append(tree_min_max(tree.left, min_max))
    if tree.right:
        bests.append(tree_min_max(tree.right, min_max))
    bests.append(tree.data)
    return min_max(bests)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
