# LeetCode #347 — Top K Frequent Elements
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. The answer is guaranteed to be unique.
#
# Example:
#   Input:  nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]

from typing import List
import heapq
from collections import Counter


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    pass


if __name__ == "__main__":
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    print("All tests passed!")
