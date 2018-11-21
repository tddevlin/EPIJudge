from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter_counts = Counter(letter_text)
    magazine_counts = Counter(magazine_text)
    magazine_counts.subtract(letter_counts)
    for letter in letter_counts.keys():
        if magazine_counts[letter] < 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
