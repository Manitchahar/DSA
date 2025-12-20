"""
Prefix Sum Pattern - Template Solutions
"""

def build_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def range_sum(prefix, i, j):
    """Sum of arr[i:j+1] inclusive"""
    return prefix[j + 1] - prefix[i]

def subarray_sum_equals_k(arr, k):
    """LeetCode 560: Count subarrays with sum = k"""
    count = prefix_sum = 0
    sum_count = {0: 1}
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    return count

def product_except_self(nums):
    """LeetCode 238: Product of array except self"""
    n = len(nums)
    result = [1] * n
    # Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    # Right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result

def max_subarray(arr):
    """LeetCode 53: Kadane's Algorithm"""
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global
