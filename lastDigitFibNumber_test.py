import pytest
import lastDigitFibNumber

def test_lastdigitfibnumber():
  a1 = lastDigitFibNumber.lastdigit(3)
  a2 = 2
  assert a1 == a2
  b1 = lastDigitFibNumber.lastdigit(139)
  b2 = 1
  assert b1 == b2
  c1 = lastDigitFibNumber.lastdigit(91239)
  c2 = 6
  assert c1 == c2
  d1 = lastDigitFibNumber.lastdigit(999999)
  d2 = 6
  assert d1 == d2