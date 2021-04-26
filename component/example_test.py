import pytest


@pytest.mark.parametrize(
    ("x", "y"), [(1, 1), (2, 4), (3, 9), (9, 81), (100, 10000)]
)
def test_square(x: int, y: int):
    assert y == x ** 2
