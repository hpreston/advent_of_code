#! /usr/bin/env python
"""
Solution for Day 1: Inverse Captcha
http://adventofcode.com/2017/day/1
"""


def captcha(input, style=1):
    """
    Take input numeric string and for each digit:
      - test if it matches the next digit
      - if so, add digit to result
    Note: Final digit is compared to first digit

    Part 2 of puzzle:
    Now compare the digit to the one "halfway around"
      - only run comparision if index less than half lenght
      - if match, add 2x
    """
    # print("Running test on: {}".format(input))
    result = 0
    input_length = len(input)

    # Determine Compare Digit Distance
    # style 1 = +1
    # style 2 = length/2
    compare = 1
    if style == 2:
        compare = int(input_length/2)
        # print("Style 2: Compare distance {}".format(compare))

    for i, digit in enumerate(input):
        # Verify digit is an integer
        try:
            int(digit)
        except ValueError:
            print("Error: Non Integer digit found.")
            exit("1")

        # Run test on digit
        if style == 1:
            # If final digit, set i to -1 to compare to first digit
            if i == input_length - 1:
                i = -1

            if digit == input[i+compare]:
                # print("Digit {} Match".format(i))
                result += int(digit)
        elif style == 2:
            if i < compare and digit == input[i+compare]:
                # print("Digit {} Match".format(i))
                result += int(digit) * 2

    return result

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run Advent of Code Day 1.')
    parser.add_argument('input', type=str,
                        help='Input to test')
    parser.add_argument('--style', type=int, default=1,
                        help="Style of test")

    args = parser.parse_args()
    print("Input: {}".format(args.input))
    print("Test Style: {}".format(args.style))

    print("Solution: {}".format(captcha(args.input, args.style)))
