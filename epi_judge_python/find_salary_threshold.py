from test_framework import generic_test


def find_salary_cap(target_payroll, current_salaries):
    if sum(current_salaries) < target_payroll:
        return -1
    current_salaries.sort()
    poor_total = 0
    for i in range(len(current_salaries)):
        difference = target_payroll - poor_total
        cap = difference / (len(current_salaries) - i)
        if cap < current_salaries[i]:
            return cap
        poor_total += current_salaries[i]
    return current_salaries[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
