# LeetCode #873 — Length of Longest Fibonacci Subsequence
#
# Given a strictly increasing array of positive integers arr, return the length
# of the longest Fibonacci-like subsequence. A Fibonacci-like sequence has at
# least 3 elements where each element equals the sum of the two preceding ones.
# Return 0 if no such subsequence exists.
#
# Example:
#   Input:  arr = [1, 2, 3, 4, 5, 6, 7, 8]
#   Output: 5   (1, 2, 3, 5, 8)
#
#   Input:  arr = [1, 3, 7, 11, 12, 14, 18]
#   Output: 3   (1, 11, 12) or (3, 11, 14) or (7, 11, 18)

from typing import List


def len_longest_fib_subseq(arr: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert len_longest_fib_subseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5
    assert len_longest_fib_subseq([1, 3, 7, 11, 12, 14, 18]) == 3
    assert len_longest_fib_subseq([1, 2, 4, 8]) == 0  # no valid subsequence of length >= 3
    print("All tests passed!")
