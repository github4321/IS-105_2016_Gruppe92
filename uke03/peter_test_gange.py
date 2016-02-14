# -*- coding: utf-8 -*-

import unittest
from gange import multiply

class TestMultiply(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_3_4(self):
        self.assertEqual(multiply(3.5,4.8), 16.8)
        
if __name__ == '__main__':
    unittest.main()