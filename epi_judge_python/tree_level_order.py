from test_framework import generic_test


def binary_tree_depth_order(tree):
    if not tree:
        return []
    level_lists = [[] for _ in range(height(tree))]

    def tree_depth(t, level):
        level_lists[level].append(t.data)
        if t.left:
            tree_depth(t.left, level + 1)
        if t.right:
            tree_depth(t.right, level + 1)

    tree_depth(tree, 0)
    return level_lists


def height(tree):
    if not tree:
        return 0
    heights = []
    if tree.left:
        heights.append(height(tree.left))
    if tree.right:
        heights.append(height(tree.right))
    if heights:
        return 1 + max(heights)
    return 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
