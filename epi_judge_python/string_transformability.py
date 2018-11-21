from test_framework import generic_test
from string import ascii_lowercase
from collections import deque


# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    word_queue = deque([(s, 0)])
    not_found = True
    explored = set()
    while word_queue and not_found:
        current_word, distance = word_queue.pop()
        # print(current_word)
        if current_word == t:
            return distance
        explored.add(current_word)
        for i in range(len(current_word)):
            for letter in ascii_lowercase:
                neighbor = current_word[:i] + letter + current_word[i+1:]
                if neighbor in D and neighbor not in explored:
                    word_queue.appendleft((neighbor, distance + 1))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
