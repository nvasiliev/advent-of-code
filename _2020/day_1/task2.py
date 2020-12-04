# 2, 3, 5, 7, 10, 14, 22

def main(input_path = 0):
    with open(input_path) as f:
        nums = [int(line) for line in f]
        nums_set = set(nums)

        for i, a in enumerate(nums):
            for j in range(i, len(nums)):
                b = nums[j]
                c = 2020 - (a + b)
                if c in nums_set:
                    print(a * b * c)
                    break


if __name__ == '__main__':
    main()
