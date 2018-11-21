from test_framework import generic_test
from test_framework.test_failure import TestFailure
import math


def find_missing_element(stream):
    data = []
    for item in stream:
        data.append(item)
    found = [0] * int(2 ** math.ceil(math.log2(len(data))))
    for item in data:
        found[item] = 1
    for i in range(len(found)):
        if not found[i]:
            return i


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
