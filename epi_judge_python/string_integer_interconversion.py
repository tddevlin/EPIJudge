from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    if x == 0:
        return '0'
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x
    char_list = []
    while x > 0:
        x, digit = divmod(x, 10)
        char_list.insert(0, chr(digit + 48))
    if is_negative:
        char_list.insert(0, '-')
    return ''.join(char_list)


def string_to_int(s):
    number = 0
    for i, c in enumerate(reversed(s)):
        if c == '-':
            return -number
        digit = ord(c) - 48
        number += digit * 10 ** i
    return number

# def int_to_string(x):
#     if x == 0:
#         return '0'
#     is_negative = False
#     if x < 0:
#         x = -x
#         is_negative = True
#     digit_list = []
#     while x > 0:
#         x, remainder = divmod(x, 10)
#         digit_list.insert(0, remainder)
#     final_string = digits_to_string(digit_list)
#     if is_negative:
#         final_string = '-' + final_string
#     return final_string
#
#
# def digits_to_string(digit_list):
#     chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     return ''.join([chars[i] for i in digit_list])
#
#
# def string_to_int(s):
#     is_negative = False
#     if s[0] == '-':
#         is_negative = True
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '-': 0}
#     digit_list = [digits[c] for c in s]
#     sum_total = 0
#     for k in range(len(digit_list)):
#         sum_total += digit_list[~k] * 10**k
#     if is_negative:
#         sum_total = -sum_total
#     return sum_total


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
