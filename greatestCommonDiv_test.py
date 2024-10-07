import pytest
import greatestCommonDiv

def test_gcd():
  a1 = greatestCommonDiv.gcd(28851538,1183019)
  a2 = 17657
  assert a1 == a2
