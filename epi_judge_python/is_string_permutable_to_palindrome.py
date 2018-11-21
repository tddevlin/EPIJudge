from test_framework import generic_test
from collections import Counter


def can_form_palindrome(s):
    letter_counts = Counter(s)
    num_odds = 0
    for count in letter_counts.values():
        if count % 2 != 0:
            num_odds += 1
    if len(s) % 2 == 0:
        return num_odds == 0
    return num_odds == 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
