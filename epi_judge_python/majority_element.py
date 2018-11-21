from test_framework import generic_test


def majority_search(stream):
    counts = {}
    majority_item = ''
    majority_count = 0
    for item in stream:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 0
        if counts[item] > majority_count:
            majority_count = counts[item]
            majority_item = item
    return majority_item


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
