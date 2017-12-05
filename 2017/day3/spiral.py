#! /usr/bin/env python
"""
Solution for Day 3: Spiral Memory
http://adventofcode.com/2017/day/3
"""

from math import sqrt

def findpoints(level):
    """
    Calculate and return the four corners of the incremental square.
    Return as 4 element touple.
    - (Upper Right, Upper Left, Lower Left, Lower Right)
    """
    # LR: Square of (Level * 2 + 1)
    # LL: LR - (level * 2)
    # UL: LR - (Level * 4)
    # UR: LR - (level * 6)
    lr = (2 * level + 1) ** 2
    ll = lr - (level * 2)
    ul = lr - (level * 4)
    ur = lr - (level * 6)
    px = ur - level
    py = ul - level
    nx = ll - level
    ny = lr - level
    corners =  (ur, ul, ll, lr)
    coords = (px, py, nx, ny)
    return {"corners": corners, "coords": coords}

def findlevel(number):
    """
    Find the level at which a given number exists.
    Based on the closest square root of an odd number.
    """
    # Find square root of number
    # If result even, add 1
    # If result odd (and not integer) add 2
    # If odd, and an integer, return
    # level = result above - 1 /2
    num_sqrt = sqrt(number)
    if int(num_sqrt) % 2 == 0:
        lrsqrt = int(num_sqrt) + 1
    elif num_sqrt.is_integer():
        lrsqrt = int(num_sqrt)
    else:
        lrsqrt = int(num_sqrt) + 2
    return int((lrsqrt - 1)/2)

def steps(input):
    """
    Return the number of steps around a spiral memory square
    for a given input.
    """
    # Find the Level in the square
    level = findlevel(input)

    # Get the level details
    points = findpoints(level)

    # Find the coord where absolute value of input - coord <= level
    for coord in points["coords"]:
        if abs(input - coord) <= level:
            return abs(input - coord) + level

    return -1

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run Advent of Code Day 2.')
    parser.add_argument('input', type=int,
                        help='Input to test')
    parser.add_argument('--style', type=int, default=1,
                        help="Style of test")

    args = parser.parse_args()
    print("Input: {}".format(args.input))
    print("Test Style: {}".format(args.style))

    if args.style == 1:
        result = steps(args.input)
    # elif args.style ==2:
    #     result = checksum2(args.input)

    print("Solution: {}".format(result))
