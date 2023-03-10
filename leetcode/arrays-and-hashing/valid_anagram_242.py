from collections import Counter


class Solution:
  def isAnagram(s, t) -> bool:
    return Counter(s) == Counter(t)
    
  print(isAnagram(" "," "))
  print(isAnagram("anagram","nagaram"))
  print(isAnagram("mace","race"))
  
  def isAnagram2(s,t) -> bool:
    return sorted(s) == sorted(t)
    
  print(isAnagram2(" "," "))
  print(isAnagram2("anagram","nagaram"))
  print(isAnagram2("mace","race"))
