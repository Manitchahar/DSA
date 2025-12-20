"""
Sliding Window Pattern - Template Solutions
"""
from collections import defaultdict, Counter

# --- Fixed Size Window ---
def max_sum_subarray_k(arr, k):
    if len(arr) < k: return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# --- Variable Size Window ---
def min_subarray_len(target, nums):
    left = current_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0

def longest_substring_without_repeating(s):
    char_index = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

def minimum_window_substring(s, t):
    """LeetCode 76 (HARD)"""
    if not s or not t: return ""
    need, have = Counter(t), defaultdict(int)
    required, formed, left = len(need), 0, 0
    min_len, result = float('inf'), (0, 0)
    
    for right in range(len(s)):
        have[s[right]] += 1
        if s[right] in need and have[s[right]] == need[s[right]]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    return s[result[0]:result[1]+1] if min_len != float('inf') else ""
