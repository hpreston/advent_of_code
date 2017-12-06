#! /usr/bin/env python
"""
Solution for Day 5: A Maze of Twisty Trampolines, All Alike
http://adventofcode.com/2017/day/5
"""


def maze_part1(input_file):
    """
    Open file and process the instructions for the maze.
    Return number of steps needed to complete.
    """
    result = 0
    # Read in input and convert to list of numbers
    with open(input_file) as f:
        input_list = [int(line) for line in f.readlines()]

    # Process Maze
    maze_length = len(input_list) # Success is when location >= maze_length
    location = 0
    while location < maze_length:
        # Store step data
        start_location = location
        start_step_value = input_list[location]
        increment_step_value = start_step_value + 1

        # Move location
        location = location + input_list[location]

        # Store new increment_step_value
        input_list[start_location] = increment_step_value

        # Increment Step Count
        result += 1

    return result

def maze_part2(input_file):
    """
    Open file and process the instructions for the maze.
    Return number of steps needed to complete.
    """
    result = 0
    # Read in input and convert to list of numbers
    with open(input_file) as f:
        input_list = [int(line) for line in f.readlines()]

    # Process Maze
    maze_length = len(input_list) # Success is when location >= maze_length
    location = 0
    while location < maze_length:
        # Store step data
        start_location = location
        start_step_value = input_list[location]

        # Calculate Increment
        # If start_step_value >= 3, then = -1
        # else: = +1
        increment = 1
        if start_step_value >= 3:
            increment = -1

        increment_step_value = start_step_value + increment

        # Move location
        location = location + input_list[location]

        # Store new increment_step_value
        input_list[start_location] = increment_step_value

        # Increment Step Count
        result += 1

    return result


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
        result = maze_part1(args.file)
    elif args.style ==2:
        result = maze_part2(args.file)

    print("Solution: {}".format(result))
