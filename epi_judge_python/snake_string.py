from test_framework import generic_test


def snake_string(s):
    top_row = []
    middle_row = []
    bottom_row = []
    for i in range(len(s)):
        if i % 2 == 0:
            middle_row.append(s[i])
        elif (i-1) % 4 == 0:
            top_row.append(s[i])
        else:
            bottom_row.append(s[i])
    return ''.join(top_row + middle_row + bottom_row)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
