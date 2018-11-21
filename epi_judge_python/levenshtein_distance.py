from test_framework import generic_test


def levenshtein_distance(A, B):
    distances = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    for i in range(1, len(A) + 1):
        distances[i][0] = i
    for j in range(1, len(B) + 1):
        distances[0][j] = j
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            distances[i][j] = min([
                1 + distances[i-1][j],
                1 + distances[i][j-1],
                int(A[i-1] != B[j-1]) + distances[i-1][j-1],
            ])
    return distances[len(A)][len(B)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
