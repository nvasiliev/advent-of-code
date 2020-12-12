from typing import Dict, List


def parse_neighbor(raw_neighbor: str) -> str:
    pieces = raw_neighbor.split(' ')
    return f'{pieces[1]} {pieces[2]}'


def dfs(g: Dict[str, List[str]], target: str, u: str) -> bool:
    if u == target:
        return True

    for v in g[u]:
        if dfs(g, target, v):
            return True

    return False


def main(input_path = 0):
    with open(input_path) as f:
        target = 'shiny gold'
        empty = 'no other bags.'

        g = {}

        for line in f:
            line = line.strip()
            u, v = line.split(' bags contain ')
            g[u] = [] if v == empty else [parse_neighbor(x) for x in v.split(', ')]

        count = sum(dfs(g, target, u) for u in g if u != target)
        print(count)


if __name__ == '__main__':
    main()
