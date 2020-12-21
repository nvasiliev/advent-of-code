from collections import Counter, deque
from typing import Dict

PREAMBLE_LEN = 25
# PREAMBLE_LEN = 5


def main(source = 0):
    with open(source) as f:
        print(solve(f))


def sum_exists(sum_: int, values: Dict[int, int]) -> bool:
    for x in values:
        target = sum_ - x
        if target != x and target in values:
            return True

    return False


def solve(f):
    counter = Counter()
    q = deque()

    for _ in range(PREAMBLE_LEN):
        x = int(f.readline())
        q.append(x)
        counter[x] += 1

    for line in f:
        x = int(line)

        if not sum_exists(x, counter):
            return x

        f = q.popleft()
        decrement_or_evict(counter, f)
        q.append(x)
        counter[x] += 1

    raise ValueError("Not found")


def decrement_or_evict(counter: Dict[int, int], f: int):
    counter[f] -= 1
    if counter[f] == 0:
        counter.pop(f)


if __name__ == '__main__':
    main()
