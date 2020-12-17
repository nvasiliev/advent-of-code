def solve(lines):
    visited = set()
    acc, i, n = 0, 0, len(lines)

    while i < n:
        if i in visited:
            break

        visited.add(i)

        op, x = lines[i].split(' ')
        num = int(x)

        if op == 'jmp':
            i += num - 1

        if op == 'acc':
            acc += num

        i += 1

    return acc


def main(source = 0):
    with open(source) as stdin:
        print(solve([line.strip() for line in stdin]))


if __name__ == '__main__':
    main()
