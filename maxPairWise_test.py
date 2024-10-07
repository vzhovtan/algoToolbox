import pytest
import maxPairWise

def test_maxpairwise():
  a1 = maxPairWise.maxpairwise([1,2,3])
  a2 = 6
  assert a1 == a2
  b1 = maxPairWise.maxpairwise([10,20,30])
  b2 = 600
  assert b1 == b2
  c1 = maxPairWise.maxpairwise([3,1,0])
  c2 = 3
  assert c1 == c2