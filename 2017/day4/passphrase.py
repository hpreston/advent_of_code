#! /usr/bin/env python
"""
Solution for Day 4: High-Entropy Passphrases
http://adventofcode.com/2017/day/4
"""

def dup_test(input):
    """
    Test input string to see if any "words" are repeated.
    """
    # Take input and split to words
    input_list = input.split()

    # Search to see if any duplicates are in the list
    for word in input_list:
        if input_list.count(word) != 1:
            return False

    # If no duplicates found, return true
    return True

def anagram_test(input):
    """
    Test input string if any words are anagrams of each other.
    """
    # Take input and split to words
    input_list = input.split()
    input_list = [list(word) for word in input_list]

    # Sort each word character
    for word in input_list:
        word.sort()

    # Search to see if any duplicates are in the list
    for word in input_list:
        if input_list.count(word) != 1:
            return False

    # If no duplicates found, return true
    return True


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run Advent of Code Day 4.')
    parser.add_argument("--file", type=str, help="File name to test.")
    parser.add_argument('--style', type=int, default=1,
                        help="Style of test")

    args = parser.parse_args()
    print("Input file: {}".format(args.file))
    print("Test Style: {}".format(args.style))

    # Open input File
    total_count = 0
    pass_count = 0
    fail_count = 0


    if args.style == 1:
        with open(args.file) as f:
            for line in f:
                total_count += 1
                if dup_test(line):
                    pass_count += 1
                else:
                    fail_count += 1
    elif args.style ==2:
        with open(args.file) as f:
            for line in f:
                total_count += 1
                if anagram_test(line):
                    pass_count += 1
                else:
                    fail_count += 1

    print("Total: {}\nPass: {}\nFail: {}".format(total_count, pass_count, fail_count))
    # print("Solution: {}".format(result))
