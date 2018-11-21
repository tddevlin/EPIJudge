from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    for row in range(9):
        num_set = set()
        for col in range(9):
            number = partial_assignment[row][col]
            if number == 0:
                continue
            if number in num_set:
                return False
            num_set.add(number)
    for col in range(9):
        num_set = set()
        for row in range(9):
            number = partial_assignment[row][col]
            if number == 0:
                continue
            if number in num_set:
                return False
            num_set.add(number)
    upper_left_corners = [(x, y) for x in [0, 3, 6] for y in [0, 3, 6]]
    for (x, y) in upper_left_corners:
        num_set = set()
        indices = generate_subsquare_indices(x, y)
        for (i, j) in indices:
            number = partial_assignment[i][j]
            if number == 0:
                continue
            if number in num_set:
                return False
            num_set.add(number)
    return True


def generate_subsquare_indices(i, j):
    row_indices = [i, i+1, i+2]
    col_indices = [j, j+1, j+2]
    indices = [(x, y) for x in row_indices for y in col_indices]
    return indices



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
