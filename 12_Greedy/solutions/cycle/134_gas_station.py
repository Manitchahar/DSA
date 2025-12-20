from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Problem: 134. Gas Station
        Link: https://leetcode.com/problems/gas-station/
        
        Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            if total < 0:
                total = 0
                start = i + 1
                
        return start
