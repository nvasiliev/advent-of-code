from functools import reduce
from typing import List, Tuple


def count_trees(grid: List[str], slope: Tuple[int, int]) -> int:
    count = 0
    right, down = slope
    j = 0

    for i in range(0, len(grid), down):
        line = grid[i]
        if line[j] == '#':
            count += 1

        j = (j + right) % len(line)

    return count


def solve(grid: List[str]) -> int:
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    counts = [count_trees(grid, slope) for slope in slopes]

    return reduce(lambda acc, count: acc * count, counts, 1)


def main(input_path = 0):
    grid = []

    with open(input_path) as f:
        for line in f:
            grid.append(line.strip())

    print(solve(grid))


if __name__ == '__main__':
    main()
