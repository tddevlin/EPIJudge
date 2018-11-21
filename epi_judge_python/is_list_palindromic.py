from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    array = []
    while L:
        array.append(L.data)
        L = L.next
    for i in range(len(array)):
        if array[i] != array[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
