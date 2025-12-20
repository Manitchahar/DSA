import heapq

class MedianFinder:
    """
    Problem: 295. Find Median from Data Stream
    Link: https://leetcode.com/problems/find-median-from-data-stream/
    
    The median is the middle value in an ordered integer list.
    
    Time Complexity: O(log n) for addNum, O(1) for findMedian
    Space Complexity: O(n)
    """

    def __init__(self):
        # Two heaps: small (max heap) and large (min heap)
        # small stores the smaller half of numbers
        # large stores the larger half of numbers
        self.small = [] # Python default is min heap, so store negatives
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        # Ensure every element in small is <= every element in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance sizes (small can have at most 1 more element than large)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2.0
