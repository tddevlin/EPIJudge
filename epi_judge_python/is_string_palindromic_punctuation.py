from test_framework import generic_test


def is_palindrome(s):
    forward_index = 0
    backward_index = len(s) - 1
    while forward_index < backward_index:
        if not s[forward_index].isalnum():
            forward_index += 1
            continue
        if not s[backward_index].isalnum():
            backward_index -= 1
            continue
        if s[forward_index].lower() != s[backward_index].lower():
            return False
        forward_index += 1
        backward_index -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
