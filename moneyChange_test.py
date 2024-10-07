import pytest
import moneyChange

def test_change():
  a1 = moneyChange.change(2)
  a2 = 2
  assert a1 == a2
  b1 = moneyChange.change(28)
  b2 = 6
  assert b1 == b2
