import unittest
import rectangle
import math

class TestRectangle(unittest.TestCase):
    
    def test_area_positive(self):

        self.assertEqual(rectangle.area(5, 3), 15)
        self.assertEqual(rectangle.area(10, 2), 20)
        self.assertEqual(rectangle.area(7, 7), 49)
    
    def test_perimeter_positive(self):

        self.assertEqual(rectangle.perimeter(5, 3), 16)
        self.assertEqual(rectangle.perimeter(10, 2), 24)
        self.assertEqual(rectangle.perimeter(7, 7), 28)
    
    def test_edge_cases(self):

        self.assertEqual(rectangle.area(1000000, 1000000), 1000000000000)
        self.assertEqual(rectangle.perimeter(1000000, 1000000), 4000000)   

if __name__ == '__main__':
    unittest.main()