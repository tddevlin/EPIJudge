from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    if num_pairs == 0:
        return ['']
    if num_pairs == 1:
        return ['()']
    all_strings = set()
    for string in generate_balanced_parentheses(num_pairs - 1):
        all_strings.add('(' + string + ')')
    for i in range(1, num_pairs):
        new_strings = [
            x + y
            for x in generate_balanced_parentheses(i)
            for y in generate_balanced_parentheses(num_pairs - i)
        ]
        for string in new_strings:
            all_strings.add(string)
    return list(all_strings)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
