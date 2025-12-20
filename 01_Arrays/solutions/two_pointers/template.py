"""
Two Pointers Pattern - Template Solutions
==========================================

Use this file as a reference when solving Two Pointers problems.
"""

# ============================================
# PATTERN 1: Opposite Direction Pointers
# ============================================
# Use when: Sorted array, finding pairs, palindrome

def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target in a SORTED array.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # No pair found


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome (ignoring non-alphanumeric).
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def container_with_most_water(heights: list[int]) -> int:
    """
    LeetCode 11: Container With Most Water
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(heights) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_area = max(max_area, width * height)
        
        # Move the pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    LeetCode 15: 3Sum - Find all triplets that sum to zero.
    Time: O(n²), Space: O(1) excluding output
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointer for remaining pair
        left, right = i + 1, n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result


# ============================================
# PATTERN 2: Same Direction (Fast & Slow)
# ============================================
# Use when: In-place modification, removing elements

def remove_duplicates(nums: list[int]) -> int:
    """
    LeetCode 26: Remove duplicates from sorted array in-place.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    slow = 0  # Position to place next unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1  # Length of unique elements


def remove_element(nums: list[int], val: int) -> int:
    """
    LeetCode 27: Remove all instances of val in-place.
    Time: O(n), Space: O(1)
    """
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


def move_zeroes(nums: list[int]) -> None:
    """
    LeetCode 283: Move all zeros to end, maintain relative order.
    Time: O(n), Space: O(1)
    """
    slow = 0  # Position for next non-zero
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def squares_of_sorted_array(nums: list[int]) -> list[int]:
    """
    LeetCode 977: Return squares in sorted order.
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    position = n - 1  # Fill from the end
    
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        
        if left_sq > right_sq:
            result[position] = left_sq
            left += 1
        else:
            result[position] = right_sq
            right -= 1
        
        position -= 1
    
    return result


# ============================================
# PATTERN 3: Dutch National Flag (3-way)
# ============================================
# Use when: Sorting with 3 distinct values

def sort_colors(nums: list[int]) -> None:
    """
    LeetCode 75: Sort array of 0s, 1s, and 2s in-place.
    Time: O(n), Space: O(1)
    """
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ============================================
# TESTING
# ============================================
if __name__ == "__main__":
    # Test two_sum_sorted
    print("Two Sum Sorted:", two_sum_sorted([2, 7, 11, 15], 9))  # [0, 1]
    
    # Test is_palindrome
    print("Is Palindrome:", is_palindrome("A man, a plan, a canal: Panama"))  # True
    
    # Test container_with_most_water
    print("Max Water:", container_with_most_water([1,8,6,2,5,4,8,3,7]))  # 49
    
    # Test three_sum
    print("3Sum:", three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    
    # Test remove_duplicates
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    print(f"Remove Dups: {k}, {nums[:k]}")  # 2, [1, 2]
    
    # Test move_zeroes
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print("Move Zeroes:", nums)  # [1, 3, 12, 0, 0]
    
    # Test sort_colors
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    print("Sort Colors:", nums)  # [0, 0, 1, 1, 2, 2]
    
    print("\n✅ All tests passed!")
