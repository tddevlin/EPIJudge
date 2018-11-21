from test_framework import generic_test
from epi_judge_python.binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
    if not preorder:
        return None
    root = preorder.pop(0)
    root_inorder_index = inorder.index(root)
    left_inorder = inorder[:root_inorder_index]
    right_inorder = inorder[root_inorder_index+1:]
    left_tree = binary_tree_from_preorder_inorder(preorder[:root_inorder_index], left_inorder)
    right_tree = binary_tree_from_preorder_inorder(preorder[root_inorder_index:], right_inorder)
    return BinaryTreeNode(root, left_tree, right_tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
