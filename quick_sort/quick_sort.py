from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    pass


if __name__ == "__main__":
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
    assert quick_sort([-3, 0, 5, -1, 2]) == [-3, -1, 0, 2, 5]
    print("All tests passed!")
