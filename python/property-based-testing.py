# https://fsharpforfunandprofit.com/posts/property-based-testing-2/
from hypothesis import given
import hypothesis.strategies as st


@given(st.integers(), st.integers())
def test_add(x, y):
    assert(add(x, y) == x + y)


@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
