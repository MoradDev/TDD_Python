import unittest
from ma_class import *

sample=MaClass("premiere_class")

class MonTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_aire_cercle(self):
        with self.subTest(self):
            self.assertEqual(sample.aire_cercle(0), 0)


if __name__ == "__main__":
    unittest.main()