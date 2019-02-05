# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

""" enhence by Weihan Xu at Feb 5, 2019"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

# before this line is the original test case
# After this line is the test case I enhanced

    def testInvalidInput1(self):  # Test a or b or c can't >200
        self.assertEqual(classifyTriangle(300, 310, 320), 'InvalidInput')

    def testInvalidInput2(self):  # Test a or b or c  can't <= 0
        self.assertEqual(classifyTriangle(-1, 7, 0), 'InvalidInput')

    def testInvalidInput3(self):  # Test three inputs must be integers
        self.assertEqual(classifyTriangle(4.5, 10.5, 8.5), 'InvalidInput')

    def tesInvalidInput4(self):
        self.assertEqual(classifyTriangle(4, 'None', 11), 'InvalidInput')

    # Test the sum of two sides of a triabgle must greater than the third side
    
    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(1, 2, 4), 'NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(1, 4, 2), 'NotATriangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(2, 4, 1), 'NotATriangle')
    # Test the triangle is the Scalene
   
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(6, 4, 9), 'Scalene')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(4, 3, 2), 'Scalene')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene')
    
    # Test the triangle is the Isosceles
   
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

