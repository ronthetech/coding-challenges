from collections import defaultdict
from typing import List


class Solution:
  def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    # mapping charChount of each string to list of Anagrams
    res = defaultdict(list) # Defining a dictionary with values as a list

    for str in strs:
      count = [0] * 26 # a - z

      for ct in str:
        # count how many of each char there is
        count[ord(ct) - ord("a")] += 1

      res[tuple(count)].append(str)

    return res.values()

    # O(m * n) 
    # m ~number of strings in input
    # n ~average length of each string 