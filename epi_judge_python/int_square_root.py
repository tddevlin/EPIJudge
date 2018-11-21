from test_framework import generic_test


def square_root(k):
    if k == 0 or k == 1:
        return k
    # for i in range(k + 1):
    #     if i**2 > k:
    #         return i-1

    candidate = k // 2
    while candidate ** 2 > k:
        candidate = candidate // 2
    for i in range(candidate, k + 1):
        if i**2 > k:
            return i-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
