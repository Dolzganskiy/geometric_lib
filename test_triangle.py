import unittest
import triangle
import math

class TestTriangle(unittest.TestCase):
    
    def test_area_positive(self):

        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(3, 4), 6)
        self.assertEqual(triangle.area(7, 2), 7)
    
    def test_perimeter_valid_triangle(self):

        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)
        self.assertEqual(triangle.perimeter(7, 10, 12), 29)
    
    def test_equilateral_triangle(self):

        side = 5
        perimeter_result = triangle.perimeter(side, side, side)
        
        expected_perimeter = 3 * side
        
        self.assertEqual(perimeter_result, expected_perimeter)
    
    def test_right_triangle(self):

        base, height = 3, 4
        hypotenuse = 5
        
        area_result = triangle.area(base, height)
        perimeter_result = triangle.perimeter(base, height, hypotenuse)
        
        self.assertEqual(area_result, 6)
        self.assertEqual(perimeter_result, 12)
        
        self.assertEqual(area_result, (base * height) / 2)
    
    def test_edge_cases(self):

        large_side = 1000000
        self.assertEqual(triangle.area(large_side, large_side), 500000000000)
        self.assertEqual(triangle.perimeter(large_side, large_side, large_side), 3000000)

if __name__ == '__main__':
    unittest.main()

    