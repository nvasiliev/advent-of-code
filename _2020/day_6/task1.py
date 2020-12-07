def main(input_path = 0):
    with open(input_path) as f:
        group_answers = set()
        line = f.readline().strip()
        sum_ = 0
        while group_answers or line:
            if line == '':
                sum_ += len(group_answers)
                group_answers = set()
            else:
                group_answers.update(line)
            line = f.readline().strip()
        print(sum_)


if __name__ == '__main__':
    main()
