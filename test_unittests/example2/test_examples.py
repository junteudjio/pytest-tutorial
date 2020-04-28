import unittest

def add_one(x):
    return x + 1

class TestAddOne(unittest.TestCase):
    def test_add_one__to_one(self):
        self.assertEqual(add_one(1), 2)
    
    def test_add_one__to_two(self):
        self.assertEqual(add_one(2), 3)
        
    def test_add_one__to_five(self):
        self.assertEqual(add_one(5), 6)

if __name__ == '__main__':
    unittest.main()