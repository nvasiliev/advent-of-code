from typing import List, TextIO


def main(source = 0):
    with open(source) as f:
        print(solve(f))


def solve(f: TextIO) -> int:
    grid = [list(f'.{line.strip()}.') for line in f]
    pseudo_row = ['.' for _ in range(len(grid[0]))]
    grid.insert(0, pseudo_row)
    grid.append(pseudo_row)

    next_grid = [row.copy() for row in grid]

    should_repeat = True

    while should_repeat:
        should_repeat = do_round(grid, next_grid)
        grid = next_grid
        next_grid = [row.copy() for row in grid]

    return sum(row.count('#') for row in grid)


def do_round(grid: List[List[str]], next_grid: List[List[str]]) -> bool:
    changed = False

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            neighbors = [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1), (i, j + 1),
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
            ]

            occupied_neighbors = 0

            for neighbor_i, neighbor_j in neighbors:
                if grid[neighbor_i][neighbor_j] == '#':
                    occupied_neighbors += 1

            seat = grid[i][j]
            if seat == 'L' and occupied_neighbors == 0:
                next_grid[i][j] = '#'
                changed = True
            if seat == '#' and occupied_neighbors >= 4:
                next_grid[i][j] = 'L'
                changed = True

    return changed


# For debug
def print_real_grid(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            print(grid[i][j], end = '')
        print()


if __name__ == '__main__':
    main()
