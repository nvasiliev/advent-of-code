def is_valid(s: str) -> bool:
    policy, password = s.split(': ')
    range_, letter = policy.split(' ')
    min_, max_ = map(int, range_.split('-'))

    count = password.count(letter)

    return min_ <= count <= max_


def main(input_path = 0):
    with open(input_path) as f:
        count = 0
        for line in f:
            if is_valid(line.strip()):
                count += 1
        print(count)


if __name__ == '__main__':
    main()
