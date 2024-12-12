"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""
from typing import List

def twosum(nums = [], target = 0) -> List[int]:
    found = False
    if len(nums) == 0:
        return []
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            
            if (nums[i] + nums[j]) == target:
                found = True
                return [i, j]
    if found == False:
        return []

def twoSumAnotherWay(nums = [], target = 0) -> List[int]:
    i = 0
    j = 0
    while True:
        if i == j:
            j += 1
            continue
        if j > len(nums) - 1:
            return []
        elif (nums[i] + nums[j]) == target:
            return [i, j]
        elif j == len(nums) - 1:
            i += 1
            j = i + 1
        elif j != len(nums) - 1:
            j += 1
            continue

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        somed = True
        while somed:
            somed = False
            for i in range(len(nums)):
                for j in range(i,len(nums)):
                    if i == j:
                        continue
                    if nums[i] + nums[j] == target:
                        somed = True
                        return [i, j]

print(twosum([2,7,11,15], 9))
print(twoSumAnotherWay([2,7,11,15,17,18], 35))
