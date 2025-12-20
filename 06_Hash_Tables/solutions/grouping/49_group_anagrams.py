from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Problem: 49. Group Anagrams
        Link: https://leetcode.com/problems/group-anagrams/
        
        Given an array of strings strs, group the anagrams together.
        
        Time Complexity: O(m * n) where m is number of strings and n is average string length.
        Space Complexity: O(m * n)
        """
        res = defaultdict(list) # mapping charCount to list of Anagrams
        
        for s in strs:
            count = [0] * 26 # a ... z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            # Lists cannot be keys, so convert to tuple
            res[tuple(count)].append(s)
            
        return list(res.values())
