from test_framework import generic_test
from typing import List


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    product_sign = 1 if (num1[0] * num2[0] > 0) else -1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    sum_total = [0]
    reversed_num2 = list(reversed(num2))
    for i in range(len(num2)):
        digit2 = reversed_num2[i]
        partial = partial_product(digit2, num1)
        partial += [0] * i
        sum_total = add(sum_total, partial)
    sum_total[0] = sum_total[0] * product_sign
    return strip_zeroes(sum_total)


def partial_product(digit: int, num: List[int]) -> List[int]:
    product = []
    carryover = 0
    for num_digit in reversed(num):
        digit_product = (digit * num_digit) + carryover
        carryover, digit_product = divmod(digit_product, 10)
        product.insert(0, digit_product)
    if carryover != 0:
        product.insert(0, carryover)
    return product


def add(num1: List[int], num2: List[int]) -> List[int]:
    n1 = len(num1)
    n2 = len(num2)
    if n1 > n2:
        num2 = (n1 - n2) * [0] + num2
    elif n2 > n1:
        num1 = (n2 - n1) * [0] + num1
    total_sum = []
    carryover = 0
    for i in range(len(num1)-1, -1, -1):
        partial_sum = num1[i] + num2[i] + carryover
        carryover, partial_sum = divmod(partial_sum, 10)
        total_sum.insert(0, partial_sum)
    if carryover != 0:
        total_sum.insert(0, carryover)
    return total_sum


def strip_zeroes(num: List[int]) -> List[int]:
    while len(num) > 1:
        if num[0] == 0:
            del num[0]
        else:
            break
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
