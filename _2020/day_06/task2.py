from collections import Counter


def main(input_path = 0):
    with open(input_path) as f:
        group_answer_counter = Counter()
        group_size = 0
        line = f.readline().strip()
        sum_ = 0

        while group_answer_counter or line:
            if line == '':
                sum_ += sum([count == group_size for _, count in group_answer_counter.items()])
                group_answer_counter = Counter()
                group_size = 0
            else:
                group_answer_counter.update(line)  # Increments count for each character in line
                group_size += 1
            line = f.readline().strip()

        print(sum_)


if __name__ == '__main__':
    main()
