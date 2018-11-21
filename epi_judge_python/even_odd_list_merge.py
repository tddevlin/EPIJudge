from test_framework import generic_test


def even_odd_merge(L):
    if not L or not L.next:
        return L
    even_iter = L
    even_last = L
    odd_iter = L.next
    odd_last = L.next
    odd_head = L.next
    while odd_iter.next and odd_iter.next.next:
        even_iter = even_iter.next.next
        even_last.next = even_iter
        even_last = even_iter
        odd_iter = odd_iter.next.next
        odd_last.next = odd_iter
        odd_last = odd_iter
    if even_iter.next and even_iter.next.next:
        even_iter = even_iter.next.next
        even_last.next = even_iter
        odd_iter.next = None
    even_iter.next = odd_head
    return L

# 0 1 2 3 4
# i   j


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
