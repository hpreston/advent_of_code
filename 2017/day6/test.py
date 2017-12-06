#! /usr/bin/env python
"""
Tests for Day 6: Memory Reallocation
http://adventofcode.com/2017/day/6
"""

from memory import debugger_part1
import unittest

examples = [
            ("sample.txt", 5)
           ]

examples2 = [
            ("sample.txt", 10)
]

class Test(unittest.TestCase):
    def test_001(self):
        print("Style 1 Test:")
        for example in examples:
            print("Input: {} - expect {}".format(example[0], example[1]))
            test = debugger_part1(example[0])
            self.assertEqual(test[0], example[1])

    # def test_002(self):
    #     print("Style 2 Test:")
    #     for example in examples2:
    #         print("Input: {} - expect {}".format(example[0], example[1]))
    #         test = maze_part2(example[0])
    #         self.assertEqual(test, example[1])



if __name__ == '__main__':
    unittest.main()
