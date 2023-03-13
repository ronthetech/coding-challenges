from typing import List


class Solution:
  def productExceptSelf1(nums: List[int]) -> List[int]:
      # we want to multiply each element in nums times all of the other elements
      # and add it to a new array
      # make 2 passes, first in-order, second in-reverse, to compute products
      results = []

      prefix = 1
      for i in range(0,len(nums)):
          results.append(prefix)
          prefix *= nums[i]
      postfix = 1
      for i in range(len(nums)-1, -1, -1):
          results [i] *= postfix
          postfix *= nums[i]
      return results
  # Input: nums = [1,2,3,4]
  # Output: [24,12,8,6]
  
  # Input: nums = [-1,1,0,-3,3]
  # Output: [0,0,9,0,0]
  
  # nums.length is always at least 2
  # nums[i] is in range of -30 and +30