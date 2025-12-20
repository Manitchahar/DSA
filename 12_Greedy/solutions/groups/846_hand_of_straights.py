from typing import List
import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Problem: 846. Hand of Straights
        Link: https://leetcode.com/problems/hand-of-straights/
        
        Rearrange the into groups of groupSize, where each group is a consecutive sequence.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        minH = list(count.keys())
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]
            
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]: # Must always remove the smallest available
                        return False
                    heapq.heappop(minH)
                    
        return True
