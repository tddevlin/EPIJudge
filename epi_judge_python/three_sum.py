from test_framework import generic_test


def has_three_sum(A, t):
    A.sort()
    i, j = 0, len(A) - 1
    narrowed_down = False
    while not narrowed_down and i <= j:
        if 2*A[i] + A[j] > t:
            j -= 1
        elif A[i] + 2*A[j] < t:
            i += 1
        else:
            narrowed_down = True
    for index in range(i, j+1):
        if has_two_sum(A[i:j+1], t - A[index]):
            return True
    return False


def has_two_sum(A, t):
    i, j = 0, len(A) - 1
    while i <= j:
        if A[i] + A[j] < t:
            i += 1
        elif A[i] + A[j] > t:
            j -= 1
        else:
            return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
