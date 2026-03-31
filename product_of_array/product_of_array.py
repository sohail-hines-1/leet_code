from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    sum = 1
    current_index = 0
    results = [0] * len(nums)

    while current_index < len(nums):
        for i in range(0, len(nums)):
            if i == current_index:
                continue
            sum *= nums[i]
            results [current_index] = sum
        sum = 1
        current_index += 1
    return results


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert product_except_self([0, 0]) == [0, 0]
    print("All tests passed!")
