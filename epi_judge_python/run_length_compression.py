from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    decoded_s = ''
    current_number = ''
    for i in range(len(s)):
        if s[i].isnumeric():
            current_number += s[i]
        else:
            decoded_s += int(current_number) * s[i]
            current_number = ''
    return decoded_s


def encoding(s):
    current_char = s[0]
    num_seen = 1
    encoded_s = ''
    for i in range(1, len(s)):
        if s[i] != current_char:
            encoded_s += str(num_seen) + current_char
            current_char = s[i]
            num_seen = 1
        else:
            num_seen += 1
    encoded_s += str(num_seen) + current_char
    return encoded_s


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
