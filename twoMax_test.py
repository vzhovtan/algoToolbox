import unittest
import twoMax

class Test(unittest.TestCase):
  def test_twomax(self):
    ''' testing twoMax finction'''
    a = twoMax.twomax([1,2,3,4,5])
    b = (5,4)
    self.assertTrue(a == b, "5 and 4 should be returned as max and second max")