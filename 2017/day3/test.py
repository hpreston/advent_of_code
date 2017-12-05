#! /usr/bin/env python
"""
Tests for Day 3: Spiral Memory
http://adventofcode.com/2017/day/3
"""

from spiral import steps
import unittest

examples = [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31)
]

class Test(unittest.TestCase):
    def test_001(self):
        print("Style 1 Test:")
        for example in examples:
            print("Input: {} - expect {}".format(example[0], example[1]))
            test = steps(example[0])
            self.assertEqual(test, example[1])



if __name__ == '__main__':
    unittest.main()
