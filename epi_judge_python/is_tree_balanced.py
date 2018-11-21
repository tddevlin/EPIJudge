from test_framework import generic_test


def is_balanced_binary_tree(tree):
    if not tree or (not tree.left and not tree.right):
        return True
    if not tree.left:
        return height(tree.right) == 1
    if not tree.right:
        return height(tree.left) == 1
    return all([
        abs(height(tree.left) - height(tree.right)) <= 1,
        is_balanced_binary_tree(tree.left),
        is_balanced_binary_tree(tree.right),
    ])


def height(tree):
    if not tree.left and not tree.right:
        return 1
    if not tree.left:
        return 1 + height(tree.right)
    if not tree.right:
        return 1 + height(tree.left)
    return 1 + max(height(tree.left), height(tree.right))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
