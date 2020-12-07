import re


def decode_boarding_pass(boarding_pass: str) -> int:
    return int(re.sub(r'B|R', '1', re.sub(r'F|L', '0', boarding_pass)), 2)


def main(input_path = 0):
    with open(input_path) as f:
        sum_ = 0
        min_, max_ = float('inf'), float('-inf')

        for line in f:
            seat_id = decode_boarding_pass(line.strip())

            min_ = min(min_, seat_id)
            max_ = max(max_, seat_id)
            sum_ += seat_id

        total_sum = ((max_ * (max_ + 1)) // 2) - ((min_ * (min_ - 1)) // 2)

        print(total_sum - sum_)


if __name__ == '__main__':
    main()
