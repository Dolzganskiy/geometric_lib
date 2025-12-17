import unittest
import circle
import math

class TestCircle(unittest.TestCase):
    
    def test_area_positive(self):

        self.assertAlmostEqual(circle.area(1), math.pi)
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)
        self.assertAlmostEqual(circle.area(5), 25 * math.pi)
    
    def test_area_decimal(self):

        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)
    
    def test_perimeter_positive(self):

        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)
        self.assertAlmostEqual(circle.perimeter(5), 10 * math.pi)
    
    def test_perimeter_decimal(self):

        self.assertAlmostEqual(circle.perimeter(2.5), 5 * math.pi)
        self.assertAlmostEqual(circle.perimeter(3.3), 6.6 * math.pi)
    
    def test_edge_cases(self):

        small_radius = 0.001
        self.assertAlmostEqual(circle.area(small_radius), math.pi * 0.000001)
        self.assertAlmostEqual(circle.perimeter(small_radius), 0.006283185307179586)

        large_radius = 1000000
        self.assertAlmostEqual(circle.area(large_radius), math.pi * 1e12)
        self.assertAlmostEqual(circle.perimeter(large_radius), 2 * math.pi * 1e6)
    
if __name__ == '__main__':
    unittest.main()