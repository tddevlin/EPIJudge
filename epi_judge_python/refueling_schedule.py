import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import math

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    net_gas = [0] * len(gallons)
    cum_sum = 0
    min_sum = math.inf
    min_i = 0
    for i in range(len(gallons)):
        net_gas[i] = cum_sum + gallons[i] - distances[i] / MPG
        if net_gas[i] < min_sum:
            min_sum = net_gas[i]
            min_i = i+1
        cum_sum += gallons[i] - distances[i] / MPG
    return min_i

    # for start in range(len(net_gas)):
    #     cum_sum = 0
    #     can_make_it = True
    #     for i in range(start, start+len(net_gas)):
    #         cum_sum += net_gas[i % len(net_gas)]
    #         if cum_sum < 0:
    #             can_make_it = False
    #             break
    #     if can_make_it:
    #         return start


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
