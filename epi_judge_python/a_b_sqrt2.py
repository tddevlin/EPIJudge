from test_framework import generic_test
import math, heapq


def generate_first_k_a_b_sqrt2(k):
    all_possibilities = [a + b*math.sqrt(2) for a in range(k) for b in range(k)]
    return heapq.nsmallest(k, all_possibilities)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
