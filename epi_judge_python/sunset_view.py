from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    building_stack = []
    index_stack = []
    for i, building in enumerate(sequence):
        while building_stack and building >= building_stack[-1]:
            building_stack.pop()
            index_stack.pop()
        building_stack.append(building)
        index_stack.append(i)
    return list(reversed(index_stack))
    # tallest_building = 0
    # buildings_with_view = []
    # for i, building in enumerate(reversed(sequence)):
    #     if building > tallest_building:
    #         tallest_building = building
    #         buildings_with_view.append(len(sequence) - i - 1)
    # return buildings_with_view


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
