from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    if k == 0 or not L:
        return L
    end_pointer = L
    num_encountered = 1
    while end_pointer.next:
        end_pointer = end_pointer.next
        num_encountered += 1
    end_pointer.next = L
    for _ in range(num_encountered - k % num_encountered):
        end_pointer = end_pointer.next
        L = L.next
    end_pointer.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
