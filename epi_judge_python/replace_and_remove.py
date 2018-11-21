import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    i = j = 0
    intermediate_size = 0
    final_size = 0
    while j < size:
        if s[j] == 'b':
            j += 1
        else:
            intermediate_size += 1
            if s[j] == 'a':
                final_size += 2
            else:
                final_size += 1
            s[i] = s[j]
            i += 1
            j += 1
    final_index = final_size - 1
    read_index = intermediate_size - 1
    while final_index > 0:
        if s[read_index] == 'a':
            s[final_index] = 'd'
            s[final_index - 1] = 'd'
            final_index -= 2
        else:
            s[final_index] = s[read_index]
            final_index -= 1
        read_index -= 1
    del s[final_size:]


# # not in place
# def replace_and_remove(size, s):
#     read_index = 0
#     new_array = []
#     while read_index < size:
#         if s[read_index] == 'a':
#             new_array.extend(['d', 'd'])
#         elif s[read_index] != 'b':
#             new_array.append(s[read_index])
#         read_index += 1
#     s[:] = new_array
#     return


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
