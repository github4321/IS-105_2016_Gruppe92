import unittest 
from tor_dele import add

class TestAdd (unittest.TestCase):
    def setup (self):
        pass
    def test_numbers_8_9 (self):
        self.assertEqual (add(4,2),2)
        
if __name__ == '_main_':
    unittest.main()
        