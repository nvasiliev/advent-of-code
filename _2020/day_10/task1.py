def main(source = 0):
    with open(source) as f:
        joltes = (int(line) for line in f)

        prev = 0
        counter = [0] * 3
        for x in sorted(joltes):
            counter[x - prev - 1] += 1
            prev = x
        print(counter[0] * (counter[2] + 1))


if __name__ == '__main__':
    main()
