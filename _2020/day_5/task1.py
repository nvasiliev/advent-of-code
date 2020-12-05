from typing import Tuple


def decode_boarding_pass(boarding_pass: str) -> Tuple[int, int]:
    def bin_search(s: str, *, left_char: str, start: int, range_: Tuple[int, int]):
        left, right = range_
        i = start

        while left < right:
            c = s[i]
            middle = (right - left) // 2 + left

            if c == left_char:
                right = middle
            else:
                left = middle + 1

            i += 1

        return left, i

    row, i = bin_search(boarding_pass, start = 0, left_char = 'F', range_ = (0, 127))
    column, _ = bin_search(boarding_pass, start = i, left_char = 'L', range_ = (0, 7))

    return row * 8 + column


def main(input_path = 0):
    with open(input_path) as f:
        max_ = float('-inf')

        for line in f:
            seat_id = decode_boarding_pass(line.strip())
            max_ = max(seat_id, max_)

        print(max_)


if __name__ == '__main__':
    main()
