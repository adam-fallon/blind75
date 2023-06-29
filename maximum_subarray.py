#!/usr/bin/env python3

# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

from typing import List

def maxSubArray(nums: List[int]) -> int:
    curr_sum = 0
    max_so_far = nums[0]

    # looping through all the numbers
    for i in range(len(nums)):
        # keep track of curr num
        curr = nums[i]
        # if the curr sum goes negative
        if curr_sum < 0:
            # start counting again
            curr_sum = 0
        # add current number to the current sum
        curr_sum += curr
        # set max subarray to the max of the max_so_far, or if curr_sum has gotten bigger than that, set it to that.
        max_so_far = max(max_so_far, curr_sum)

    return max_so_far


ans1 = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(ans1)
ans2 = maxSubArray([1])
print(ans2)
ans3 = maxSubArray([5,4,-1,7,8])
print(ans3)
