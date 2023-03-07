class MinStack:
  # ["MinStack","push","push","push","getMin","pop","top","getMin"]
  # [[],[-2],[0],[-3],[],[],[],[]]
  
  # Expected: 
  # [null,null,null,null,-3,null,0,-2]
  
  def __init__(self):
    self.stack = [] # start with empty stacks
    self.minStack = []
    
  def push1(self, val: int) -> None:
    self.stack.append(val)
    if self.minStack:
      val = min(self.minStack[-1],val)
    self.minStack.append(val)

  def push2(self, val: int) -> None:
    self.stack.append(val) # add new item to stack
    # sets val to the minimum between val and (the last item in the stack if it isn't empty, or the value itself if the stack is empty
    val = min(val, self.minStack[-1] if self.minStack else val)
    # add minimum val to minStack
    self.minStack.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()