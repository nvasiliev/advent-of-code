import pytest

from .task2 import is_valid

params = [
    ['1-3 a: abcde', True],
    ['1-3 b: cdefg', False],
    ['2-9 c: ccccccccc', False],
    ['666-777 x: ab', False]
]


@pytest.mark.parametrize('param', params)
def test_is_valid(param):
    s, expected = param
    assert is_valid(s) == expected
