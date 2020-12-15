from typing import Dict, List, Tuple


def parse_neighbor(raw_neighbor: str) -> Tuple[str, int]:
    pieces = raw_neighbor.split(' ')
    return f'{pieces[1]} {pieces[2]}', int(pieces[0])


def dfs(g: Dict[str, List[str]], v: str) -> int:
    total = 1

    for u, count in g[v]:
        total += count * dfs(g, u)

    return total


def main(input_path = 0):
    with open(input_path) as f:
        target = 'shiny gold'
        empty = 'no other bags.'

        g = {}

        for line in f:
            line = line.strip()
            u, v = line.split(' bags contain ')
            g[u] = [] if v == empty else [parse_neighbor(x) for x in v.split(', ')]

        count = dfs(g, target) - 1
        print(count)


if __name__ == '__main__':
    main()
