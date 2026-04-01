from typing import List

def do_binary_search(nums: List[int], start: int, end: int, target: int) -> int:
    mid = start + (end - start) // 2

    if end - start <= 1:
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    if nums[mid] >= target:
        return do_binary_search(nums, start, mid, target)
    else:
        return do_binary_search(nums, mid + 1, end, target)

def binary_search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    return do_binary_search(nums, start, end, target)


if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9, 11], 11) == 5
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1
    assert binary_search([1, 3, 5, 7, 9, 11], 1) == 0
    print("All tests passed!")
