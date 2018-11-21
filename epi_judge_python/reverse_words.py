import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    reversed_words = []
    word_index = 0
    for i in range(len(s)):
        if s[i] == ' ':
            reversed_words.insert(0, s[word_index:i])
            word_index = i+1
        if i == len(s) - 1:
            reversed_words.insert(0, s[word_index:])
    new_s = ' '.join(w for w in reversed_words)
    for i in range(len(s)):
        s[i] = new_s[i]
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
