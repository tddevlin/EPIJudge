from test_framework import generic_test


def look_and_say(n):
    if n == 1:
        return '1'
    previous_string = look_and_say(n-1)
    current_char = previous_string[0]
    current_count = 1
    new_string = ''
    for i in range(1, len(previous_string)):
        if previous_string[i] != current_char:
            new_string += str(current_count) + current_char
            current_char = previous_string[i]
            current_count = 1
        else:
            current_count += 1
    new_string += str(current_count) + current_char
    return new_string


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
