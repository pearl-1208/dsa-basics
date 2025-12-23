def power_set(nums):
    if not nums:
        return [[]]

    remaining = power_set(nums[1:])
    return remaining + [[nums[0]] + subset for subset in remaining]


print(power_set([1, 2, 3]))
