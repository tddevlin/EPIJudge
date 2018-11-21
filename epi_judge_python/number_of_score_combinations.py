from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):

    pass

# # correct but slow
# def num_combinations_for_final_score(final_score, individual_play_scores):
#     combination_sets = [{tuple([0] * len(individual_play_scores))}]
#     for score in range(1, final_score+1):
#         print(score)
#         if score < min(individual_play_scores):
#             combination_sets.append(set())
#         else:
#             new_combination_set = set()
#             for i, play in enumerate(individual_play_scores):
#                 if play <= score:
#                     for combination in combination_sets[score - play]:
#                         new_combination = list(combination)
#                         new_combination[i] += 1
#                         new_combination_set.add(tuple(new_combination))
#             combination_sets.append(new_combination_set)
#     return len(combination_sets[-1])





# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 0 1 1 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
