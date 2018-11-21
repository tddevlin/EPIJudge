from test_framework import generic_test
import math


def find_nearest_repetition(paragraph):
    last_seen = {}
    closest_distance = math.inf
    for i, word in enumerate(paragraph):
        if word in last_seen:
            if i - last_seen[word] < closest_distance:
                closest_distance = i - last_seen[word]
            last_seen[word] = i
        else:
            last_seen[word] = i
    if closest_distance < math.inf:
        return closest_distance
    else:
        return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
