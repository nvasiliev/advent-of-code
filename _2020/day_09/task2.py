from collections import deque

if __name__ == '__main__':
    from task1 import solve  # Run from terminal
else:
    from .task1 import solve  # Run from tests


def main(source = 0):
    with open(source) as f:
        target = solve(f)
        f.seek(0)

        window = deque()
        sum_ = 0

        line = f.readline()
        while line:
            while sum_ < target:
                x = int(line)
                window.append(x)
                sum_ += x
                line = f.readline()

            if sum_ == target and len(window) > 1:
                break

            while sum_ > target:
                sum_ -= window.popleft()

        print(min(window) + max(window))


if __name__ == '__main__':
    main()
