import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):
    # build left side
    left_side = []
    current_tree = tree
    while current_tree:
        left_side.append(current_tree)
        if current_tree.left:
            current_tree = current_tree.left
        else:
            current_tree = current_tree.right

    # build bottom
    bottom = []

    def dfs(t):
        if not t.left and not t.right:
            bottom.append(t)
        if t.left:
            dfs(t.left)
        if t.right:
            dfs(t.right)
    dfs(tree)

    # build right side
    right_side = []
    current_tree = tree
    while current_tree:
        right_side.append(current_tree)
        if current_tree.right:
            current_tree = current_tree.right
        else:
            current_tree = current_tree.left

    print([x.data for x in left_side])
    print([x.data for x in bottom])
    print([x.data for x in right_side])

    if left_side[-1] == bottom[0]:
        del left_side[-1]
    if bottom[-1] == right_side[-1]:
        del right_side[-1]

    return left_side + bottom + list(reversed(right_side[1:]))

#      1
#   -3     5
#     11  9
#      2


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
