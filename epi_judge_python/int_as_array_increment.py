from test_framework import generic_test


def plus_one(A):
    for i in range(1, len(A) + 1):
        if A[-i] == 9:
            A[-i] = 0
        else:
            A[-i] = A[-i] + 1
            break
    if A[0] == 0:
        A.insert(0, 1)
    return A


# def plus_one(A):
#     for i in range(len(A)-1, -1, -1):
#         if A[i] == 9:
#             A[i] = 0
#         else:
#             A[i] += 1
#             return A
#     if A[0] == 0:
#         return [1] + A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
