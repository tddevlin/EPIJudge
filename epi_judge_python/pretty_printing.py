from test_framework import generic_test
import math


def minimum_messiness(words, line_length):
    scores = [math.inf for _ in range(len(words) + 1)]
    scores[-1] = 0
    for i in range(len(words)-1, -1, -1):
        best_score = math.inf
        for j in range(i, len(words)):
            this_line = words[i:j+1]
            this_score = score(this_line, line_length)
            rest_score = scores[j+1]
            best_score = min(best_score, this_score + rest_score)
        scores[i] = best_score
    return scores[0]


def score(line, length):
    line_text = ' '.join(line)
    if len(line_text) > length:
        return math.inf
    return (length - len(line_text)) ** 2

# len = 5
# 0 1 2 3 4
#         i
#

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))
