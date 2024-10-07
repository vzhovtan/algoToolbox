import pytest
import hugeFibNumber

def test_hugefibnumber():
  a1 = hugeFibNumber.hugefibnumber(1, 239)
  a2 = 1
  assert a1 == a2
  b1 = hugeFibNumber.hugefibnumber(115, 1000)
  b2 = 885
  assert b1 == b2
  c1 = hugeFibNumber.hugefibnumber(2816213588, 239)
  c2 = 151
  assert c1 == c2