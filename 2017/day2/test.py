#! /usr/bin/env python
"""
Tests for Day 2: Corruption Checksum
http://adventofcode.com/2017/day/1
"""

from checksum import checksum, checksum2
import unittest

example = ("sample.csv", 18)
example2 = ("sample2.csv", 9)

class ChecksumTest(unittest.TestCase):
    def test_001(self):
        print("Style 1 Test:")
        print("Input: {} - expect {}".format(example[0], example[1]))
        test = checksum(example[0])
        self.assertEqual(test, example[1])

    def test_002(self):
        print("Style 2 Test:")
        print("Input: {} - expect {}".format(example2[0], example2[1]))
        test = checksum2(example2[0])
        self.assertEqual(test, example2[1])


if __name__ == '__main__':
    unittest.main()
