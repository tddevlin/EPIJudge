from test_framework import generic_test


def rotate_matrix(square_matrix):
    if not square_matrix or len(square_matrix) == 1:
        return
    num_layers = len(square_matrix) // 2
    for i in range(num_layers):
        rotate_ith_layer(square_matrix, i)


def rotate_ith_layer(A, i):
    n = len(A)
    for j in range(i, n - i - 1):
        A[i][j], A[j][n-i-1], A[n-i-1][n-j-1], A[n-j-1][i] = (
            A[n-j-1][i], A[i][j], A[j][n-i-1], A[n-i-1][n-j-1]
        )


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
