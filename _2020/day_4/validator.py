import re
from typing import Callable


# Custom validation madness, just for fun :)
# todo: Use library or create custom lib (more or less completed, e.g. handling error messages, better API, etc)

def in_range_of(value: str, min_: int, max_: int):
    try:
        return min_ <= int(value) <= max_
    except ValueError:
        return False


def range_validator(min_: int, max_: int) -> Callable:
    def _validate(value: str) -> bool:
        return in_range_of(value, min_, max_)

    return _validate


def height_validator(measure: str, min_: int, max_: int) -> Callable:
    format_regex = re.compile(f'^\\d+{measure}$')
    not_number_regex = re.compile(r'\D+')

    def _validate(raw_height: str) -> bool:
        if not format_regex.match(raw_height):
            return False

        height = not_number_regex.sub('', raw_height)

        return in_range_of(height, min_, max_)

    return _validate


def all_of(*validators: Callable) -> Callable:
    def _validate(value: str):
        for validator in validators:
            if not validator(value):
                return False

        return True

    return _validate


def one_of(*validators: Callable) -> Callable:
    def _validate(value: str):
        for validator in validators:
            if validator(value):
                return True

        return False

    return _validate


def regex_validator(pattern: str) -> Callable:
    regex = re.compile(pattern)

    def _validate(value: str):
        return bool(regex.search(value))

    return _validate
