from typing import List
from functools import wraps, partial


def memo(fn = None, *, hash_function = lambda *args, **kwargs: f'{args}_{kwargs}'):
    if not fn:
        return partial(memo, hash_function = hash_function)

    cache = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = hash_function(*args, **kwargs)
        if key in cache:
            return cache[key]
        res = fn(*args, **kwargs)
        cache[key] = res
        return res

    wrapper.clear = lambda: cache.clear()

    return wrapper


@memo(hash_function = lambda *args, **kwargs: kwargs['pos'])
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
