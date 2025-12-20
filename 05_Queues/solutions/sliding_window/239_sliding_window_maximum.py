from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Problem: 239. Sliding Window Maximum
        Link: https://leetcode.com/problems/sliding-window-maximum/
        
        You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
        Return the max sliding window.
        
        Time Complexity: O(n) - Each element added/removed max once.
        Space Complexity: O(k)
        """
        output = []
        q = deque() # Indices
        l = 0
        
        for r in range(len(nums)):
            # 1. Pop smaller values from queue (monotonic decreasing indices)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # 2. Add current index
            q.append(r)
            
            # 3. Remove index if it's out of the window
            if l > q[0]:
                q.popleft()
            
            # 4. Add to output if window is at least size k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
                
        return output
