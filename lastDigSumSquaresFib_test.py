import pytest
import lastDigSumSquaresFib

def test_pisanonumod60():
  a1 = lastDigSumSquaresFib.pisanonummod60(7)
  a2 = 13
  assert a1 == a2
  b1 = lastDigSumSquaresFib.pisanonummod60(8)
  b2 = 21
  assert b1 == b2
  c1 = lastDigSumSquaresFib.pisanonummod60(73)
  c2 = 53
  assert c1 == c2
  d1 = lastDigSumSquaresFib.pisanonummod60(74)
  d2 = 17
  assert d1 == d2