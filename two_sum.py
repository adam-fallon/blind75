#!/usr/bin/env python3
# https://leetcode.com/problems/two-sum/

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}

    for i in range(len(nums)):
        # print(f"i: {i}\tnums[i]: {nums[i]}\ttarget: {target}\tdict: {dict}")
        t = target - nums[i]

        # If the target is stored in the dictionary
        # it means we've found the complement of the number adding up to the target
        if nums[i] in dict:
            return [dict[nums[i]], i]

        dict[t] = i

    return []

ans1 = twoSum([2, 7, 11, 15], 9)

print(ans1)
