def two_sum(nums, target):
    # Dictionary to store number and its index
    num_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], i]
        num_index[num] = i

    return []

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
