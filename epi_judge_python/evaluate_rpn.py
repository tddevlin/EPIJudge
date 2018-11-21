from test_framework import generic_test


def evaluate(expression):
    expression_list = [x if x in {'+', '-', '*', '/'} else int(x) for x in expression.split(',')]
    expression_stack = []
    for symbol in expression_list:
        if isinstance(symbol, int):
            expression_stack.append(symbol)
        else:
            second = expression_stack.pop()
            first = expression_stack.pop()
            if symbol == '+':
                expression_stack.append(first + second)
            elif symbol == '-':
                expression_stack.append(first - second)
            elif symbol == '*':
                expression_stack.append(first * second)
            elif symbol == '/':
                expression_stack.append(first // second)
    return expression_stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
