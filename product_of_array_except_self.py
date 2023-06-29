#!/usr/bin/env python3
from typing import List

# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
def productExceptSelf(nums: List[int]) -> List[int]:
    # init array to size of input array
    ans = [1] * len(nums)
    # set 1 as a default value
    prefix = 1

    # for each value compute the prefix and placing it in the ans array
    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]
        print(f"prefix: {prefix}\tans: {ans}")


    # for each value compute the postfix by multiplying whats in the array already
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]
        print(f"postfix: {postfix}\tans: {ans}")

    return ans



ans1 = productExceptSelf([1,2,3,4])
print(ans1)


#ans2 = productExceptSelf([-1,1,0,-3,3])
#print(ans2)
