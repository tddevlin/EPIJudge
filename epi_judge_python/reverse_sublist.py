from test_framework import generic_test


def reverse_sublist(L, start, finish):
    if not L or not L.next:
        return L
    first_node = L
    pre_head = head = None
    for i in range(1, start + 1):
        if i == start - 1:
            pre_head = L
        if i == start:
            head = L
            break
        L = L.next
    last = head
    current = head.next
    for i in range(start, finish):
        next_node = current.next
        current.next = last
        last = current
        current = next_node
    tail = last
    post_tail = current
    if pre_head:
        pre_head.next = tail
    else:
        first_node = tail
    head.next = post_tail
    return first_node


# def reverse_sublist(L, start, finish):
#     if not L or not L.next or start == finish:
#         return L
#     one_before = previous = first = None
#     ith_node = L
#     i = 1
#     while i <= finish:
#         if i < start - 1:
#             ith_node = ith_node.next
#         elif i == start - 1:
#             one_before = ith_node
#             ith_node = ith_node.next
#         elif i == start:
#             first = ith_node
#             previous = ith_node
#             ith_node = ith_node.next
#         elif start < i < finish:
#             next_node = ith_node.next
#             ith_node.next = previous
#             previous = ith_node
#             ith_node = next_node
#         elif i == finish:
#             next_node = ith_node.next
#             ith_node.next = previous
#             previous = ith_node
#             ith_node = next_node
#             first.next = ith_node
#             if one_before:
#                 one_before.next = previous
#         i += 1
#     return L if one_before else previous


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
