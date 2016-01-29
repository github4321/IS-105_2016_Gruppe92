# -*- coding: utf-8 -*-

import unittest
from dele import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_10_2(self):
        self.assertEqual(add(10,2), 5)
        
if __name__ == '__main__':
    unittest.main()