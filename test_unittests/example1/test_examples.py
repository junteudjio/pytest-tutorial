import unittest

def add_one(x):
    return x + 1

class TestAddOne(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(3), 5)

if __name__ == '__main__':
    unittest.main()