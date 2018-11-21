from test_framework import generic_test


class Node:
    def __init__(self, x, y, neighbors):
        self.x = x
        self.y = y
        self.neighbors = neighbors
        self.explored = False


def build_nodes(maze):
    nodes = [[None for _ in range(len(maze[0]))] for _ in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            neighbors = get_neighbors(i, j, maze, maze[i][j])
            nodes[i][j] = Node(i, j, neighbors)
    return nodes


def get_neighbors(i, j, maze, color):
    neighbors = []
    if i > 0 and maze[i-1][j] == color:
        neighbors.append((i-1, j))
    if i < len(maze) - 1 and maze[i+1][j] == color:
        neighbors.append((i+1, j))
    if j > 0 and maze[i][j-1] == color:
        neighbors.append((i, j-1))
    if j < len(maze[0]) - 1 and maze[i][j+1] == color:
        neighbors.append((i, j+1))
    return neighbors


def flip_color(x, y, image):
    nodes = build_nodes(image)
    reachable_nodes = set()
    node_queue = [nodes[x][y]]
    while node_queue:
        current_node = node_queue.pop(0)
        reachable_nodes.add((current_node.x, current_node.y))
        current_node.explored = True
        for i, j in current_node.neighbors:
            if not nodes[i][j].explored:
                node_queue.append(nodes[i][j])
    for i, j in reachable_nodes:
        image[i][j] = 1 - image[i][j]
    return image


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
