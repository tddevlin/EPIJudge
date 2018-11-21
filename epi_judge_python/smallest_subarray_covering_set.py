import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import math

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    i = j = 0
    counts = collections.Counter({paragraph[0]: 1})
    best_length = math.inf
    best_subarray = Subarray(0, 0)
    while j < len(paragraph):
        if covers_keywords(counts, keywords):
            if j - i + 1 < best_length:
                best_length = j - i + 1
                best_subarray = Subarray(i, j)
            counts[paragraph[i]] -= 1
            i += 1
        else:
            j += 1
            if j < len(paragraph):
                counts[paragraph[j]] += 1
    return best_subarray


def covers_keywords(counts, keywords):
    return all([counts[keyword] > 0 for keyword in keywords])


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
