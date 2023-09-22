import unittest
from ma_class import *



class MonTest(unittest.TestCase):
    
    def setUp(self):
        print("Nouveau Test")
        self.instance=MaClass("premiere_class")

    def test_aire_cercle(self):
        '''tests de aire_cercle()'''
        with self.subTest(self):
            self.assertEqual(self.instance.aire_cercle(0), 0)

    def tearDown(self):
        print("Fin de ce test")


if __name__ == "__main__":
    unittest.main()