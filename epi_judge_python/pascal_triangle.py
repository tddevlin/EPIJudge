from test_framework import generic_test


def generate_pascal_triangle(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    upper_triangle = generate_pascal_triangle(n-1)
    bottom_row = upper_triangle[-1]
    new_row = [1]
    for i in range(1, n-1):
        new_row.append(bottom_row[i-1] + bottom_row[i])
    new_row.append(1)
    upper_triangle.append(new_row)
    return upper_triangle


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
