class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Problem: 242. Valid Anagram
        Link: https://leetcode.com/problems/valid-anagram/
        
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        
        Time Complexity: O(n)
        Space Complexity: O(1) (since alphabet size is fixed at 26 usually)
        """
        if len(s) != len(t):
            return False
            
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        return countS == countT
