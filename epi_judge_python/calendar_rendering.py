import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    start_times = sorted([e.start for e in A])
    finish_times = sorted([e.finish for e in A])
    i = j = num_events = max_num_events = 0
    while i < len(start_times) and j < len(finish_times):
        if start_times[i] <= finish_times[j]:
            num_events += 1
            i += 1
        else:
            num_events -= 1
            j += 1
        if num_events > max_num_events:
            max_num_events = num_events
    return max_num_events


def events_at(i, A):
    num_events = 0
    for event in A:
        if event.start <= i <= event.finish:
            num_events += 1
    return num_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
