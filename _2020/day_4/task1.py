from typing import Set

REQUIRED_FIELDS = {
    'byr',  # Birth Year
    'iyr',  # Issue Year
    'eyr',  # Expiration Year
    'hgt',  # Height
    'hcl',  # Hair Color
    'ecl',  # Eye Color
    'pid'   # Passport ID
}

OPTIONAL_FIELDS = {
    'cid'  # Country ID
}

ALL_FIELDS = REQUIRED_FIELDS | OPTIONAL_FIELDS


def validate(curr_fields: Set[str]) -> bool:
    return len(curr_fields & REQUIRED_FIELDS) == len(REQUIRED_FIELDS) or \
           len(curr_fields & ALL_FIELDS) == len(ALL_FIELDS)


def main(input_path = 0):
    with open(input_path) as f:
        count = 0

        curr_fields = set()
        line = f.readline()

        while line or curr_fields:
            line = line.strip()

            if line == '':
                count += validate(curr_fields)
                curr_fields = set()
            else:
                curr_fields.update({pair.split(':')[0] for pair in line.split(' ')})

            line = f.readline()

        print(count)


if __name__ == '__main__':
    main()
