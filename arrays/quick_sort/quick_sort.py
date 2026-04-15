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

def do_quick_sort(nums):
    if len(nums) < 2:
        return nums

    i = 0
    right = len(nums) - 1
    j = right
    p = nums[right]
    while i < j:
        
        # look for numbers greater than pivot
        while nums[i] <= p and i < j:
            i += 1

        # look for numbers less than the pivot
        if nums[i] > p:
            while nums[j] >= p and i < j:
                j -= 1

        # now nums[i] is greater than pivot and nums[j] is less than the pivot
        if nums[i] > nums[j]:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

    # now we need to swap the value at nums[i] with the pivot at nums[right]
    if i + 1 < len (nums):
        tmp = nums[i]
        nums[i] = p
        nums[right] = tmp

    # Note: nums[0:i] excludes nums[i] which is the PIVOT
    return do_quick_sort(nums[0:i]) + [nums[i]] + do_quick_sort(nums[i+1:])

def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    nums = do_quick_sort(nums)
    print (nums)

    return nums


if __name__ == "__main__":
    assert quick_sort([5,4,9,0,6,7,1]) == [0, 1, 4, 5, 6, 7, 9]
    assert quick_sort([7, 3, 9, 2, 8, 5, 3]) == [2, 3, 3, 5, 7, 8, 9]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
    assert quick_sort([-3, 0, 5, -1, 2]) == [-3, -1, 0, 2, 5]
    print("All tests passed!")
