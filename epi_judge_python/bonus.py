from test_framework import generic_test


def calculate_bonus(productivity):
    tickets = [1 for _ in range(len(productivity))]
    if len(productivity) == 1:
        return 1
    for i in range(1, len(productivity) - 1):
        left = productivity[i - 1]
        current = productivity[i]
        right = productivity[i + 1]
        if left < current > right:
            tickets[i] = max(tickets[i-1], tickets[i+1]) + 1
        elif left < current:
            tickets[i] = tickets[i-1] + 1
        elif right < current:
            tickets[i] = tickets[i+1] + 1
    for i in range(len(productivity) - 2, 0, -1):
        left = productivity[i - 1]
        current = productivity[i]
        right = productivity[i + 1]
        if left < current > right:
            tickets[i] = max(tickets[i-1], tickets[i+1]) + 1
        elif left < current:
            tickets[i] = tickets[i-1] + 1
        elif right < current:
            tickets[i] = tickets[i+1] + 1
    if productivity[0] > productivity[1]:
        tickets[0] = tickets[1] + 1
    if productivity[-1] > productivity[-2]:
        tickets[-1] = tickets[-2] + 1
    return sum(tickets)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bonus.py", 'bonus.tsv',
                                       calculate_bonus))
