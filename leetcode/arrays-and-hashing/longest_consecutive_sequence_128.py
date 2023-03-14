from typing import List


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
class Solution:
  def longestConsecutiveSeq(nums: List[int]) -> int:
    longest = 0
    num_set = set(nums)

    for n in num_set:
      # check if its the start of a sequence, if the number to its left on a time line isnt in the set, then its the start of a sequence
        if (n-1) not in num_set:
            length = 1
            while (n+length) in num_set:
                length += 1
            longest = max(longest, length)
    
    return longest
  
  # Input: nums = [100,4,200,1,3,2]
  # Output: 4
  # Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
  # Therefore its length is 4.

  nums1 = [100,4,200,1,3,2]
  print(longestConsecutiveSeq(nums1))

  # Input: nums = [0,3,7,2,5,8,4,6,0,1]
  # Output: 9
  
  nums2 = [0,3,7,2,5,8,4,6,0,1]
  print(longestConsecutiveSeq(nums2))