class Solution:
  # s1 = "()"
  # s2 = "()[]{}"
  # s3 = "(]"
  
  def validParentheses(s: str) -> bool:
    stack = []
    hashMap = {")" : "(", "]" : "[", "}" : "{"}

    for char in s:
      if char in hashMap:
        if stack and stack[-1] == hashMap[char]:
          stack.pop()
        else:
          return False
      else:
        stack.append(char)
    
    return True if not stack else False