from test_framework import generic_test


def roman_to_integer(s):
    roman_to_decimal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    decimal_sum = 0
    index = 0
    while index < len(s) - 1:
        if (
            (s[index] == 'I' and s[index+1] in {'V', 'X'})
            or (s[index] == 'X' and s[index+1] in {'L', 'C'})
            or (s[index] == 'C' and s[index+1] in {'D', 'M'})
        ):
            decimal_sum += roman_to_decimal[s[index+1]] - roman_to_decimal[s[index]]
            index += 2
        else:
            decimal_sum += roman_to_decimal[s[index]]
            index += 1
    if index == len(s) - 1:
        decimal_sum += roman_to_decimal[s[-1]]
    return decimal_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
