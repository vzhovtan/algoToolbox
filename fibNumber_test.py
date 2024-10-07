import pytest
import fibNumber

def test_fubnumber():
  a1 = fibNumber.fibnumber(3)
  a2 = 2
  assert a1 == a2
  b1 = fibNumber.fibnumber(10)
  b2 = 55
  assert b1 == b2
  c1 = fibNumber.fibnumber(100)
  c2 = 354224848179261915075
  assert c1 == c2
  d1 = fibNumber.fibnumber(0)
  d2 = 0
  assert d1 == d2
  e1 = fibNumber.fibnumber(1)
  e2 = 1
  assert e1 == e2