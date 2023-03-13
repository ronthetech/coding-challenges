from collections import Counter
from typing import List


class Solution:
  # nums1 = [1,1,1,2,2,3] k1 = 2
  # nums2 = [1] k2 = 1


  # Bucket Sort
  def topKFrequent1(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
      count[n] = 1 + count.get(n,0)
    for n, c in count.items():
      freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
      for n in freq[i]:
        res.append(n)
        if len(res) == k:
          return res

  # O(n)
  
  def topKFrequent2(nums: List[int], k: int) -> List[int]:
    # dict with all of the integers as key 
    # and number of times it appears as value
    count = Counter(nums) 
    count = sorted(count, key=lambda x:count[x], reverse=True)

    return count[:k]