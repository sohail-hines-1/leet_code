from typing import List


def binary_search(nums: List[int], target: int) -> int:
# split the list and call recursive func
    return b_search_recursive(nums, 0, len(nums), target)


def b_search_recursive(nums: List[int], start, end, target):
    if end > start + 3:
        result = b_search_recursive(nums, start, end // 2, target)
        if (result != -1):
            return result

        return b_search_recursive(nums, end // 2 + 1, end, target)
    else:
        for i in range (start, end):
            if nums[i] == target:
                return i
        return -1

if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1
    assert binary_search([1, 3, 5, 7, 9, 11], 1) == 0
    assert binary_search([1, 3, 5, 7, 9, 11], 11) == 5
    print("All tests passed!")
