import pytest
import lastDigitSumFib

def test_lastdigitsum():
  a1 = lastDigitSumFib.lastdigsum(3)
  a2 = 4
  assert a1 == a2
  b1 = lastDigitSumFib.lastdigsum(100)
  b2 = 5
  assert b1 == b2
  c1 = lastDigitSumFib.lastdigsum(0)
  c2 = 0
  assert c1 == c2
  d1 = lastDigitSumFib.lastdigsum(1)
  d2 = 1
  assert d1 == d2