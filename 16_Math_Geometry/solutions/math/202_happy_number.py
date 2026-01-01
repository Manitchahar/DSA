class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Problem: 202. Happy Number
        Link: https://leetcode.com/problems/happy-number/
        
        Write an algorithm to determine if a number n is happy.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        def sumSq(n):
            output = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n // 10
            return output
            
        slow, fast = n, sumSq(n)
        
        while fast != 1 and slow != fast:
            slow = sumSq(slow)
            fast = sumSq(sumSq(fast))
            
        return fast == 1
