from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Problem: 207. Course Schedule
        Link: https://leetcode.com/problems/course-schedule/
        
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
        Return true if you can finish all courses.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        preMap = { i: [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # 0 = unvisited, 1 = visiting, 2 = visited
        visitSet = set() 
        
        def dfs(crs):
            if crs in visitSet: # Loop detected
                return False
            if preMap[crs] == []: # No prereqs
                return True
                
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            
            preMap[crs] = [] # Mark as done to avoid re-work
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True
