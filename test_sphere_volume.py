# import unittest
# import math
# from sphere_volume import calculate_sphere_volume

# pi = math.pi

# class TestSphereVolume(unittest.TestCase):
#     def test_area(self):
# 	    self.assertAlmostEqual(calculate_sphere_volume(5), 523.5987755982989)
    
#     def test_area(self): 
#         self.assertAlmostEqual(calculate_sphere_volume(3.7), 212.17479024304507)
    
#     def test_area(self):
#         self.assertAlmostEqual(calculate_sphere_volume(1), 4.1887902047863905)

#     def test_string(self):
# 	    self.assertRaises(TypeError,calculate_sphere_volume('four'),"unsupported operand type(s) for ** or pow(): 'str' and 'int'")

#     def test_negative(self):
# 	    self.assertEqual(calculate_sphere_volume(-5),-523.5987755982989)

# unittest.main()