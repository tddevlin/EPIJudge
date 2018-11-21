from test_framework import generic_test
import string


def ss_decode_col_id(col):
    letter_to_digit = {
        letter: number for
        letter, number in
        (zip([letter for letter in string.ascii_uppercase], range(1, 27)))
    }
    number = 0
    for i in range(len(col)):
        number += letter_to_digit[col[~i]] * 26**i
    return number


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
