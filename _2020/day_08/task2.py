from collections import deque


def solve(lines):
    acc, i, n = 0, 0, len(lines)
    swappable = ('jmp', 'nop')
    op_stack = deque()
    visited = set()
    attempted = set()
    swap_index = -1

    while i < n:
        op, x = lines[i].split(' ')
        num = int(x)

        if i in visited:
            prev_attempt_found = False if swap_index >= 0 else True

            while op not in swappable or i in attempted or not prev_attempt_found:
                op, acc, i, num = op_stack.pop()
                visited.remove(i)

                if i == swap_index:
                    prev_attempt_found = True

            op = 'nop' if op == 'jmp' else 'jmp'
            attempted.add(i)
            swap_index = i

        visited.add(i)
        op_stack.append((op, acc, i, num))

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
