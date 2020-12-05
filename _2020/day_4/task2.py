from typing import Dict

from .validator import range_validator, one_of, height_validator, regex_validator

VALIDATION_RULES = {
    'byr': range_validator(1920, 2002),  # Birth Year
    'iyr': range_validator(2010, 2020),  # Issue Year
    'eyr': range_validator(2020, 2030),  # Expiration Year
    'hgt': one_of(height_validator('cm', 150, 193), height_validator('in', 59, 76)),  # Height
    'hcl': regex_validator(r'^#[a-f0-9]{6}$'),  # Hair Color
    'ecl': regex_validator(r'^amb|blu|brn|gry|grn|hzl|oth$'),  # Eye Color
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
