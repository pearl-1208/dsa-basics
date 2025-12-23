def two_sum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        if target - num in mp:
            return [mp[target - num], i]
        mp[num] = i

print(two_sum([2, 7, 11, 15], 9))
