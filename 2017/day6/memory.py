#! /usr/bin/env python
"""
Solution for Day 6: Memory Reallocation
http://adventofcode.com/2017/day/6
"""

def balance_routine(input_listb):
    """
    Run a Balance routine against the list.
    Return the new list.
    """
    start_list = list(input_listb)
    max_value = max(input_listb)
    location_max = input_listb.index(max_value)
    list_length = len(input_listb)

    # Empty slot with max
    input_listb[location_max] = 0

    # Distribute across slots
    dist_holder = max_value
    current_slot = location_max + 1
    if current_slot == list_length:
        current_slot = 0
    while dist_holder > 0:
        # Increment current slot
        input_listb[current_slot] += 1
        # Decrement dist_holder
        dist_holder -= 1
        # Move to next slot
        current_slot += 1
        if current_slot == list_length:
            current_slot = 0

    return input_listb


def debugger_part1(input_file):
    """
    Open file and process the instructions for the debugger.
    Return number of steps needed to complete.
    """
    result = 0
    # Read in input and convert to list of numbers
    with open(input_file) as f:
        input_list = [int(slot) for slot in f.readline().split()]

    # print("Starting List: {}".format(input_list))

    # List of incountered verisons
    previous_versions = []
    previous_versions.append(list(input_list))
    # print("Previous Lists: ")
    # for l in previous_versions:
    #     print(l)
    # Variables for test
    current_list = list(input_list)
    test = []

    while True:
        print("Test Count: {}".format(result))
        # Run routine
        test = balance_routine(current_list)
        # print("Test result: {}".format(test))
        # Increment step count
        result += 1
        # Test if returned list seen before
        # print("Previous Lists: ")
        # for l in previous_versions:
        #     print(l)
        if test in previous_versions:
            return (result, test)
            # Add returned list to previous version
        previous_versions.append(list(test))
        # Reset current list to returned list
        current_list = list(test)

    # return result

def debugger_part2(input_list):
    """
    Take an input list.
    Return number of steps needed to complete.
    """
    result = 0

    # print("Starting List: {}".format(input_list))

    # List of incountered verisons
    previous_versions = []
    previous_versions.append(list(input_list))
    # print("Previous Lists: ")
    # for l in previous_versions:
    #     print(l)
    # Variables for test
    current_list = list(input_list)
    test = []

    while True:
        print("Test Count: {}".format(result))
        # Run routine
        test = balance_routine(current_list)
        # print("Test result: {}".format(test))
        # Increment step count
        result += 1
        # Test if returned list seen before
        # print("Previous Lists: ")
        # for l in previous_versions:
        #     print(l)
        if test in previous_versions:
            return (result, test)
            # Add returned list to previous version
        previous_versions.append(list(test))
        # Reset current list to returned list
        current_list = list(test)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run Advent of Code Day 5.')
    parser.add_argument("--file", type=str, help="File name to test.")
    parser.add_argument('--style', type=int, default=1,
                        help="Style of test")

    args = parser.parse_args()
    print("Input file: {}".format(args.file))
    print("Test Style: {}".format(args.style))

    if args.style == 1:
        result = debugger_part1(args.file)
    elif args.style ==2:
        result1 = debugger_part1(args.file)
        result = debugger_part2(result1[1])
        print(result)


    print("Solution: {}".format(result[0]))
