from typing import List


def binary_search(nums: List[int], target: int) -> int:
    pass


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1
    assert binary_search([1, 3, 5, 7, 9, 11], 1) == 0
    assert binary_search([1, 3, 5, 7, 9, 11], 11) == 5
    print("All tests passed!")
