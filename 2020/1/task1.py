def main(input_path = 0):
    with open(input_path) as f:
        nums = {int(line) for line in f}

        for x in nums:
            d = 2020 - x
            if d in nums:
                print(d * x)
                break


if __name__ == '__main__':
    main()
