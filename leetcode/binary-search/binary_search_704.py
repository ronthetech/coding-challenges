# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def bin_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1