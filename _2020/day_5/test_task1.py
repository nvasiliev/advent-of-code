import pytest

from _2020.testing import assert_single
from .task1 import main, decode_boarding_pass

test_cases = [
    ['1_in.txt', '1_1_out.txt']
]


@pytest.mark.parametrize('test_case', test_cases)
def test_task1(test_case):
    assert_single(__file__, main, *test_case)


seats = [
    ['FBFBBFFRLR', 357],
    ['BFFFBBFRRR', 567],
    ['FFFBBBFRRR', 119],
    ['BBFFBBFRLL', 820]
]


@pytest.mark.parametrize('pair', seats)
def test_decode_boarding_pass(pair):
    boarding_pass, expected_seat_id = pair
    assert decode_boarding_pass(boarding_pass) == expected_seat_id
