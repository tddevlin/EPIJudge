from test_framework import generic_test


# def can_reach_end(A):
#     can_reach_from_index = [False] * len(A)
#     for i in range(len(A)-1, -1, -1):
#         if i + A[i] >= len(A)-1:
#             can_reach_from_index[i] = True
#         else:
#             for j in range(A[i], 0, -1):
#                 if can_reach_from_index[i+j]:
#                     can_reach_from_index[i] = True
#                     break
#     return can_reach_from_index[0]


def can_reach_end(A):
    current_index = 0
    furthest_index = 0
    while current_index <= furthest_index and current_index < len(A):
        furthest_index = max(furthest_index, A[current_index] + current_index)
        current_index += 1
    return furthest_index >= len(A) - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
