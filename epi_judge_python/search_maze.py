import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


class Node:
    def __init__(self, x, y, neighbors):
        self.x = x
        self.y = y
        self.neighbors = neighbors
        self.explored = False


def search_maze(maze, s, e):
    all_nodes = []
    nodes = build_nodes(maze)
    node_stack = [nodes[s.x][s.y]]
    made_it = False
    while node_stack:
        current_node = node_stack.pop()
        all_nodes.append(current_node)
        if current_node.x == e.x and current_node.y == e.y:
            made_it = True
            break
        current_node.explored = True
        for x, y in current_node.neighbors:
            if not nodes[x][y].explored:
                node_stack.append(nodes[x][y])
    if not made_it:
        return []
    path = [Coordinate(all_nodes[-1].x, all_nodes[-1].y)]
    for node in reversed(all_nodes[:-1]):
        prev = path[-1]
        cur = Coordinate(node.x, node.y)
        if path_element_is_feasible(maze, prev, cur):
            path.append(cur)
    return list(reversed(path))


def build_nodes(maze):
    nodes = [[None for _ in range(len(maze[0]))] for _ in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            neighbors = get_neighbors(i, j, maze)
            nodes[i][j] = Node(i, j, neighbors)
    return nodes


def get_neighbors(i, j, maze):
    neighbors = []
    if i > 0 and maze[i-1][j] == 0:
        neighbors.append((i-1, j))
    if i < len(maze) - 1 and maze[i+1][j] == 0:
        neighbors.append((i+1, j))
    if j > 0 and maze[i][j-1] == 0:
        neighbors.append((i, j-1))
    if j < len(maze[0]) - 1 and maze[i][j+1] == 0:
        neighbors.append((i, j+1))
    return neighbors


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
