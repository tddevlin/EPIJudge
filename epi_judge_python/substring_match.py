from test_framework import generic_test


def rabin_karp(t, s):
    for i in range(len(t) - len(s) + 1):
        mismatch_found = False
        for j in range(len(s)):
            if s[j] != t[i + j]:
                mismatch_found = True
                break
        if not mismatch_found:
            return i
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
