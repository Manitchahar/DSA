"""
Sorting Patterns - Template Solutions
"""

def sort_colors(nums):
    """LeetCode 75: Dutch National Flag"""
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

def cyclic_sort(arr):
    """Sort array with elements [1, n] in O(n), O(1)"""
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    return arr

def find_missing_number(nums):
    """LeetCode 268"""
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)

def find_duplicate(nums):
    """LeetCode 287: Floyd's Cycle Detection"""
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

def majority_element(nums):
    """LeetCode 169: Moore's Voting"""
    candidate = count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

def first_missing_positive(nums):
    """LeetCode 41 (HARD)"""
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
