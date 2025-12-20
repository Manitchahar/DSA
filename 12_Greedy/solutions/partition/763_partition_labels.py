from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Problem: 763. Partition Labels
        Link: https://leetcode.com/problems/partition-labels/
        
        You want to partition the string into as many parts as possible so that each letter appears in at most one part.
        
        Time Complexity: O(n)
        Space Complexity: O(1) (Only 26 characters)
        """
        lastIndex = {c: i for i, c in enumerate(s)}
        res = []
        size, end = 0, 0
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])
            
            if i == end:
                res.append(size)
                size = 0
                
        return res
