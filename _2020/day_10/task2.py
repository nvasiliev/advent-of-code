from typing import List


class Cached(object):
    def __init__(self, fn):
        self.cache = {}
        self.fn = fn

    def __call__(self, *args, **kwargs):
        key = kwargs['pos']
        if key in self.cache:
            return self.cache[key]
        res = self.fn(*args, **kwargs)
        self.cache[key] = res
        return res

    def clear(self):
        self.cache.clear()


@Cached
def find_arrangements(prev, pos: int, joltes: List[int]):
    n = len(joltes)

    if pos == n:
        return 1

    arrangements = 0

    for i in range(pos, min(pos + 3, n)):
        x = joltes[i]
        for k in range(1, 4):
            if prev + k == x:
                arrangements += find_arrangements(prev = x, pos = i + 1, joltes = joltes)

    return arrangements


def main(source = 0):
    with open(source) as f:
        print(find_arrangements(prev = 0, pos = 0, joltes = sorted(int(line) for line in f)))


if __name__ == '__main__':
    main()
