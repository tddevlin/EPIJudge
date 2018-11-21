from test_framework import generic_test


def inorder_traversal(tree):
    node_stack = [tree]
    traversal = []
    if not tree:
        return traversal
    while node_stack:
        current_node = node_stack.pop()
        if isinstance(current_node, int):
            traversal.append(current_node)
        else:
            if current_node.left:
                node_stack.append(current_node.left)
            node_stack.append(current_node.data)
            if current_node.right:
                node_stack.append(current_node.right)
    return list(reversed(traversal))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
