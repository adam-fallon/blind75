#!/usr/bin/env python3
#https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    hashmap = {}

    for i in range(len(nums)):
        curr = nums[i]
        if curr in hashmap:
            return True

        hashmap[curr] = i
    return False

ans1 = containsDuplicate([1,2,3,1])
print(ans1)

ans2 = containsDuplicate([1,2,3,4])
print(ans2)

ans3 = containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(ans3)
