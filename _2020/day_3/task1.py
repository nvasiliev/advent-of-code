def main(input_path = 0):
    with open(input_path) as f:
        count = 0
        i = 0

        for line in f:
            line = line.strip()

            if line[i] == '#':
                count += 1

            i = (i + 3) % len(line)

        print(count)


if __name__ == '__main__':
    main()
