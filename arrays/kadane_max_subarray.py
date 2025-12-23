def max_subarray_sum(nums):
    """
    Returns the maximum sum of a contiguous subarray
    using Kadane's Algorithm.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum subarray sum:", max_subarray_sum(arr))
