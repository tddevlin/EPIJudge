import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    suffix_decompositions = [[] for _ in range(len(domain))]
    for i in range(len(domain)):
        suffix = domain[-(i+1):]
        if suffix in dictionary:
            suffix_decompositions[i] = [suffix]
        else:
            for j in range(1, len(suffix)):
                prefix = suffix[:j]
                if prefix in dictionary and suffix_decompositions[i-j]:
                    suffix_decompositions[i] = [prefix] + suffix_decompositions[i-j]
    return suffix_decompositions[len(domain)-1]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
