import unittest
import square
import math

class TestSquare(unittest.TestCase):
    
    def test_area_positive(self):

        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(3), 9)
        self.assertEqual(square.area(10), 100)
    
    def test_perimeter_positive(self):

        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(3), 12)
        self.assertEqual(square.perimeter(10), 40)
    
    def test_relationship_area_perimeter(self):

        side = 5
        area_result = square.area(side)
        perimeter_result = square.perimeter(side)
        
        self.assertEqual(perimeter_result, 4 * side)
        
        self.assertEqual(area_result, side ** 2)
        
        self.assertEqual(side, perimeter_result / 4)
        
        self.assertEqual(area_result, (perimeter_result / 4) ** 2)
    
    def test_edge_cases(self):


        large_side = 1000000
        self.assertEqual(square.area(large_side), 1e12)
        self.assertEqual(square.perimeter(large_side), 4e6)

if __name__ == '__main__':
    unittest.main()
    