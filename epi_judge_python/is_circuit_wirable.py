import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import deque

class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []


def is_any_placement_feasible(graph):
    explored = set()
    for vertex in graph:
        if vertex in explored:
            continue
        vertex.d = 0
        queue = deque([vertex])
        while queue:
            current_node = queue.popleft()
            explored.add(current_node)
            for neighbor in current_node.edges:
                if neighbor.d == current_node.d:
                    return False
                neighbor.d = 1 - current_node.d
                if neighbor not in explored:
                    queue.append(neighbor)
    return True


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
