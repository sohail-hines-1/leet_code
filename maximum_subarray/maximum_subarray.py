from typing import List


def max_subarray(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1]) == -1
    assert max_subarray([-2, -1]) == -1
    print("All tests passed!")
