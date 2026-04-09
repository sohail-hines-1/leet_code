# Quick Sort
#
# Implement the quicksort algorithm. Given an unsorted list of integers,
# return a new list with all elements sorted in ascending order.
# Average time complexity: O(n log n). Worst case: O(n²).
#
# Example:
#   Input:  [3, 6, 8, 10, 1, 2, 1]
#   Output: [1, 1, 2, 3, 6, 8, 10]
#
#   Input:  [5, 4, 3, 2, 1]
#   Output: [1, 2, 3, 4, 5]

from typing import List

def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    p = nums[len(nums) - 1]                                 # Choosing the last element as the pivot
    left_array = [x for x in nums[:-1] if x < p]            # Elements less than the pivot, note that nums[:-1] excludes the pivot
    right_array = [x for x in nums[:-1] if x >= p]          # Elements greater than or equal to the pivot, note that nums[:-1] excludes the pivot

    return quick_sort(left_array) + [p] + quick_sort(right_array)

if __name__ == "__main__":
    assert quick_sort([3, 6, 8, 10, 1, 2, 4]) == [1, 2, 3, 4, 6, 8, 10]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
    assert quick_sort([-3, 0, 5, -1, 2]) == [-3, -1, 0, 2, 5]
    print("All tests passed!")
