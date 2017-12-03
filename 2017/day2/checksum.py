#! /usr/bin/env python
"""
Solution for Day 2: Corruption Checksum
http://adventofcode.com/2017/day/1
"""

import csv

def checksum(input):
    """
    Take input sample file and:
      - find the difference between the max and min value in the row
      - add difference to result
    """
    result = 0

    try:
        with open(input) as f:
            csv_input = csv.reader(f, delimiter=' ')
            for row in csv_input:
                int_row = [int(col) for col in row]
                big = max(int_row)
                small = min(int_row)
                # print("Max is {}. Min is {}.".format(big, small))
                difference = big - small
                # print("Difference is {}".format(difference))
                result += difference
    except:
        print("Error!")
        exit("Error.")

    return result

def checksum2(input):
    """
    Take input sample file and:
      - find the two numbers that are evenly dividable
      - add the result of the divsion to the result
    """
    result = 0

    try:
        with open(input) as f:
            csv_input = csv.reader(f, delimiter=' ')
            for row_num, row in enumerate(csv_input):
                match_count = 0
                int_row = [int(col) for col in row]
                col_count = len(int_row)
                # print("col_count: {}".format(col_count))
                # loop over each column to search for even divisiable match
                for col_num, num in enumerate(int_row):
                    # loop over each other colum in the row
                    for i in range(col_count):
                        # Don't test a column against itself
                        if not col_num == i :
                            # See if the division leaves a 0 remainder
                            if int_row[col_num] % int_row[i] == 0:
                                # print("Row {} Mod 0 found.".format(row_num))
                                # print("col_num: {} - i: {}".format(col_num, i))
                                # Calculate quotient
                                quotient = int_row[col_num] / int_row[i]
                                # Save quotient to result
                                result += quotient
                                # Increment match count (each row should have 1)
                                match_count += 1
                # print("Match Count for row {}: {}".format(row_num, match_count))

    except:
        print("Error!")
        exit("Error.")

    return result

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run Advent of Code Day 2.')
    parser.add_argument('input', type=str,
                        help='Input to test')
    parser.add_argument('--style', type=int, default=1,
                        help="Style of test")

    args = parser.parse_args()
    print("Input: {}".format(args.input))
    # print("Test Style: {}".format(args.style))

    if args.style == 1:
        result = checksum(args.input)
    elif args.style ==2:
        result = checksum2(args.input)

    print("Solution: {}".format(result))
