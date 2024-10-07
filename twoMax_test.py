import pytest
import twoMax

def test_twomax():
  a1 = twoMax.twomax([1,2,3])
  a2 = (3,2)
  assert a1 == a2
  b1 = twoMax.twomax([10,20,30])
  b2 = (30,20)
  assert b1 == b2
  c1 = twoMax.twomax([3,1,0])
  c2 = (3,1)
  assert c1 == c2