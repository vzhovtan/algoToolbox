import pytest
import twoSum

def test_twoSum ():
 a1 = 5
 a2 = twoSum.twosum(2,3)
 assert a1 == a2
 b1 = 9
 b2 = twoSum.twosum(5, 4)
 assert b1 == b2
 c1 = 0
 c2 = twoSum.twosum(0, 0)
 assert c1 == c2
