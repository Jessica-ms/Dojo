import pytest


def answer(a, b):
    return a * b


@pytest.mark.parametrize(
    "var1, var2,expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)],
)
def test_answer(var1, var2, expected):
    assert answer(var1, var2) == expected
