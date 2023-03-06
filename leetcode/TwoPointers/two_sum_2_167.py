from typing import List


class Solution:
#   Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.
# numbers is sorted in non-decreasing order.
# The tests are generated such that there is exactly one solution.
    def twSum(numbers: List[int], target: int):
        #setting our pointers up at as the first index which is 0 and the last index, the length of numbers -1
        l, r = 0, len(numbers)-1

        while l < r:
            current = numbers[l] + numbers[r]
            # if the current sum is too big, decrease by moving the right pointer left one spot
            if current > target:
                r -= 1
            # else if the current sum is too small, increase by moving the left pointer right one spot
            elif current < target:
                l += 1
            # else the only remaining condition is that the successful pair of indexes has been found
            # so add one to their index since the question states it was 1 indexed instead of 0 indexed
            else:
                return [l + 1, r + 1]
    # Input: numbers = [2,7,11,15], target = 9
    # Output: [1,2]
    # Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    
    # Input: numbers = [2,3,4], target = 6
    # Output: [1,3]
    # Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
    
    # Input: numbers = [-1,0], target = -1
    # Output: [1,2]
    # Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].