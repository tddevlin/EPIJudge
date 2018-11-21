from test_framework import generic_test


def inorder_traversal(tree):
    traversal = []
    while True:
        bottom_left_node = descend_left(tree)
        traversal.append(bottom_left_node)
        fork, intermediates = ascend_to_fork(bottom_left_node)
        traversal.extend(intermediates)
        traversal.append(fork.data)
        print(traversal)
        if fork.right:
            tree = fork.right
        else:
            break
    return [bottom_left_node.data, fork.data]


def descend_left(tree):
    while tree.left:
        tree = tree.left
    return tree


def ascend_to_fork(tree):
    intermediates = []
    while tree.parent:
        if tree.right:
            break
        intermediates.append(tree.data)
        tree = tree.parent
    return tree, intermediates



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
