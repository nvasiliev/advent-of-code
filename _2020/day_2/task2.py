def is_valid(s: str) -> bool:
    policy, password = s.split(': ')
    positions, letter = policy.split(' ')
    pos1, pos2 = map(int, positions.split('-'))

    def contains_target(pos: int) -> bool:
        return pos <= len(password) and password[pos - 1] == letter

    return bool(contains_target(pos1) ^ contains_target(pos2))


def main(input_path = 0):
    with open(input_path) as f:
        count = 0
        for line in f:
            if is_valid(line.strip()):
                count += 1
        print(count)


if __name__ == '__main__':
    main()
