#! /usr/bin/env python
"""
Tests for Day 4: High-Entropy Passphrases
http://adventofcode.com/2017/day/4
"""

from passphrase import dup_test, anagram_test
import unittest

examples = [
            ("aa bb cc dd ee", True),
            ("aa bb cc dd aa", False),
            ("aa bb cc dd aaa", True)
           ]

examples2 = [
("abcde fghij", True),
("abcde xyz ecdab", False),
("a ab abc abd abf abj", True),
("iiii oiii ooii oooi oooo", True),
("oiii ioii iioi iiio", False)
]

class Test(unittest.TestCase):
    def test_001(self):
        print("Style 1 Test:")
        for example in examples:
            print("Input: {} - expect {}".format(example[0], example[1]))
            test = dup_test(example[0])
            self.assertEqual(test, example[1])

    def test_002(self):
        print("Style 2 Test:")
        for example in examples2:
            print("Input: {} - expect {}".format(example[0], example[1]))
            test = anagram_test(example[0])
            self.assertEqual(test, example[1])



if __name__ == '__main__':
    unittest.main()
