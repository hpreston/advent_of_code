#! /usr/bin/env python
"""
Tests for Day 1: Inverse Captcha
http://adventofcode.com/2017/day/1
"""

from captcha import captcha
import unittest

examples = [
("1122", 3),
("1111", 4),
("1234", 0),
("91212129", 9)
]

examples2 = [
("1212", 6),
("1221", 0),
("123425", 4),
("123123", 12),
("12131415", 4)
]

class CaptchaTest(unittest.TestCase):
    def test_001(self):
        print("Style 1 Test:")
        for example in examples:
            print("Input: {} - expect {}".format(example[0], example[1]))
            test = captcha(example[0])
            self.assertEqual(test, example[1])

    def test_002(self):
        print("Style 2 Test:")
        for example in examples2:
            print("Input: {} - expect {}".format(example[0], example[1]))
            test = captcha(example[0], 2)
            self.assertEqual(test, example[1])


if __name__ == '__main__':
    unittest.main()
