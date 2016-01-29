# -*- coding: utf-8 -*-

import unittest
from multiply import add


class TestMultiply(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_3_4(self):
        self.assertEqual(add(3,4), 12)
        
if __name__ == '__main__':
    unittest.main()