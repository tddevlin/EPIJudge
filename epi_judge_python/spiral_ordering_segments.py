from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    n = len(square_matrix)
    left_bound = upper_bound = 0
    right_bound = lower_bound = n - 1
    directions = ['right', 'down', 'left', 'up']
    row = col = 0
    path_number = 0
    spiral_nums = []
    while len(spiral_nums) < n ** 2:
        direction = directions[path_number % 4]
        if direction == 'right':
            while col <= right_bound:
                spiral_nums.append(square_matrix[row][col])
                col += 1
            col = right_bound
            upper_bound += 1
            row += 1
        elif direction == 'down':
            while row <= lower_bound:
                spiral_nums.append(square_matrix[row][col])
                row += 1
            row = lower_bound
            right_bound -= 1
            col -= 1
        elif direction == 'left':
            while col >= left_bound:
                spiral_nums.append(square_matrix[row][col])
                col -= 1
            col = left_bound
            lower_bound -= 1
            row -= 1
        else:
            while row >= upper_bound:
                spiral_nums.append(square_matrix[row][col])
                row -= 1
            row = upper_bound
            left_bound += 1
            col += 1
        path_number += 1
    return spiral_nums


# def matrix_in_spiral_order(square_matrix):
#     if not square_matrix:
#         return []
#     n = len(square_matrix[0])
#     spiral_array = []
#     for i in range(n):
#         spiral_array.append(square_matrix[0][i])
#     current_row = 0
#     current_col = n - 1
#     move_index = 0
#     for num_steps in range(n-1, 0, -1):
#         next_positions = next_indices(current_row, current_col, move_index, num_steps)
#         for (x, y) in next_positions:
#             spiral_array.append(square_matrix[x][y])
#         move_index += 1
#         next_positions = next_indices(next_positions[-1][0], next_positions[-1][1], move_index, num_steps)
#         for (x, y) in next_positions:
#             spiral_array.append(square_matrix[x][y])
#         move_index += 1
#         current_row, current_col = next_positions[-1][0], next_positions[-1][1]
#     return spiral_array
#
#
# def next_indices(i, j, move_index, num_steps):
#     if move_index % 4 == 0:
#         return [(x, j) for x in range(i+1, i+num_steps+1)]
#     if move_index % 4 == 1:
#         return [(i, y) for y in range(j-1, j-num_steps-1, -1)]
#     if move_index % 4 == 2:
#         return [(x, j) for x in range(i-1, i-num_steps-1, -1)]
#     if move_index % 4 == 3:
#         return [(i, y) for y in range(j+1, j+num_steps+1)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
