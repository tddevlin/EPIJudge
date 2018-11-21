import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    seen_nodes = set()
    seen_nodes.add(node0.data)
    while node0.parent:
        node0 = node0.parent
        seen_nodes.add(node0.data)
    if node1.data in seen_nodes:
        return node1
    while node1.parent:
        node1 = node1.parent
        if node1.data in seen_nodes:
            return node1
    return node1


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
