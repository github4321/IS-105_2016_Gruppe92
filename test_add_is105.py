# -*- coding: utf-8 -*-

import unittest
from is105 import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_3_4(self):
        self.assertEqual(add(3,4), 7)
        
if __name__ == '__main__':
    unittest.main()