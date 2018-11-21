from test_framework import generic_test


def palindrome_decompositions(input):
    if not input:
        return [[]]
    elif len(input) == 1:
        return [[input]]
    all_decompositions = []
    for i in range(1, len(input)+1):
        if is_palindromic(input[:i]):
            rest_decompositions = palindrome_decompositions(input[i:])
            for decomposition in rest_decompositions:
                all_decompositions.append([input[:i]] + decomposition)
    return all_decompositions


def is_palindromic(input: str):
    for i in range(len(input)):
        if input[i] != input[-(i+1)]:
            return False
    return True

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
