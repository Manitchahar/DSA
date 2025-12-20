from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Problem: 347. Top K Frequent Elements
        Link: https://leetcode.com/problems/top-k-frequent-elements/
        
        Given an integer array nums and an integer k, return the k most frequent elements.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
