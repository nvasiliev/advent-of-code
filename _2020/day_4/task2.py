import re
from typing import Callable, Dict


# Custom validation madness :)

def in_range_of(value: str, min_: int, max_: int):
    try:
        return min_ <= int(value) <= max_
    except ValueError:
        return False


def year_validator(min_: int, max_: int) -> Callable:
    def _validate(year: str) -> bool:
        return in_range_of(year, min_, max_)

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


def regex_validator(pattern: str):
    regex = re.compile(pattern)

    def _validate(value: str):
        return bool(regex.search(value))

    return _validate


def stub() -> Callable:
    return lambda x: True


# class Composition:
#     def __init__(self):
#         self.validators = []
#     def

VALIDATION_RULES = {
    'byr': year_validator(1920, 2002),  # Birth Year
    'iyr': year_validator(2010, 2020),  # Issue Year
    'eyr': year_validator(2020, 2030),  # Expiration Year
    'hgt': one_of(height_validator('cm', 150, 193), height_validator('in', 59, 76)),  # Height
    'hcl': regex_validator(r'^#[a-f0-9]{6}$'),  # Hair Color
    'ecl': regex_validator(r'^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$'),  # Eye Color
    'pid': regex_validator(r'^\d{9}$')  # Passport ID
}


def validate(fields: Dict[str, str]) -> bool:
    count = 0

    for field, value in fields.items():
        if field not in VALIDATION_RULES:
            continue

        if not VALIDATION_RULES[field](value):
            return False

        count += 1

    if count < len(VALIDATION_RULES):
        return False

    return True


def main(input_path = 0):
    with open(input_path) as f:
        count = 0

        curr_fields = {}
        line = f.readline().strip()

        while line or curr_fields:
            if line == '':
                count += validate(curr_fields)
                curr_fields = {}
            else:
                for pair in line.split(' '):
                    k, v = pair.split(':')
                    curr_fields[k] = v

            line = f.readline().strip()

        print(count)


if __name__ == '__main__':
    main()
