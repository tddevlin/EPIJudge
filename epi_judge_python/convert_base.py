from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    if num_as_string in ['0', '-0']:
        return num_as_string
    string_to_digit = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
        }
    digit_to_string = {v: k for k, v in string_to_digit.items()}
    b1_num = 0
    is_negative = False
    for k, c in enumerate(reversed(num_as_string)):
        if c == '-':
            is_negative = True
            break
        b1_num += string_to_digit[c] * b1**k
    b2_list = []
    while b1_num > 0:
        b1_num, digit = divmod(b1_num, b2)
        b2_list.insert(0, digit_to_string[digit])
    return_string = ''.join(b2_list)
    if is_negative:
        return_string = '-' + return_string
    return return_string


# def convert_base(num_as_string, b1, b2):
#     if num_as_string == '0' or num_as_string == '-0':
#         return num_as_string
#     is_negative = False
#     if num_as_string[0] == '-':
#         is_negative = True
#         num_as_string = num_as_string[1:]
#     string_to_digit = {
#         '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
#     }
#     digit_to_string = {v: k for k, v in string_to_digit.items()}
#     base_10_num = 0
#     for i in range(len(num_as_string)):
#         base_10_num += string_to_digit[num_as_string[~i]] * b1**i
#     return_string = ''
#     while base_10_num > 0:
#         base_10_num, remainder = divmod(base_10_num, b2)
#         return_string = digit_to_string[remainder] + return_string
#     if is_negative:
#         return_string = '-' + return_string
#     return return_string


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
