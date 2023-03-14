from typing import List


class Solution:
  def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}
    
    for i, n in enumerate(nums):
      diff = target - n
      if diff in prevMap:
        return [prevMap[diff], i]
      prevMap[n] = i
      
  nums1 = [2,7,11,15]
  tar1 = 9
  nums2 = [3,2,4]
  tar2 = 6
  nums3 = [3,3]
  tar3 = 6
  
  print(twoSum(nums1,tar1))
  print(twoSum(nums2,tar2))
  print(twoSum(nums3,tar3))
  
  
  def twoSum2(nums: List[int], target: int) -> List[int]:
    lookup = {}

    for i in range(len(nums)):
        if nums[i] in lookup:
            return [lookup[nums[i]], i]
        else:
            lookup[target-nums[i]] = i
  
  print(twoSum2(nums1,tar1))
  print(twoSum2(nums2,tar2))
  print(twoSum2(nums3,tar3))