import pytest
import lastDigPartialSumFib

def test_lastdigitsum():
  a1 = lastDigPartialSumFib.lastdigpartsum(3,7)
  a2 = 1
  assert a1 == a2
  b1 = lastDigPartialSumFib.lastdigpartsum(10,10)
  b2 = 5
  assert b1 == b2