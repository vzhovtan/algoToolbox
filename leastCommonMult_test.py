import pytest
import leastCommonMult

def test_gcd():
  a1 = leastCommonMult.lcm(761457, 614573)
  a2 = 467970912861
  assert a1 == a2