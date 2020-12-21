import re


def decode_boarding_pass(boarding_pass: str) -> int:
    return int(re.sub(r'B|R', '1', re.sub(r'F|L', '0', boarding_pass)), 2)


def main(input_path = 0):
    with open(input_path) as f:
        max_ = float('-inf')

        for line in f:
            seat_id = decode_boarding_pass(line.strip())
            max_ = max(seat_id, max_)

        print(max_)


if __name__ == '__main__':
    main()
