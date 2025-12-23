def combination_sum(nums, target):
    result = []

    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        if total > target:
            return

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i, current, total + nums[i])
            current.pop()

    backtrack(0, [], 0)
    return result


print(combination_sum([2, 3, 6, 7], 7))
