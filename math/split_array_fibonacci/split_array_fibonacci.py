# LeetCode #842 — Split Array into Fibonacci Sequence
#
# Given a string of digits, split it into a Fibonacci-like sequence of at least
# 3 numbers where each number (after the first two) equals the sum of the two
# preceding ones. Numbers must not have leading zeros (except "0" itself), and
# must fit within a 32-bit signed integer. Return any valid sequence, or [] if
# none exists.
#
# Example:
#   Input:  s = "123456579"
#   Output: [123, 456, 579]
#
#   Input:  s = "11235813"
#   Output: [1, 1, 2, 3, 5, 8, 13]
#
#   Input:  s = "112358130"
#   Output: []  (no valid split)

from typing import List


def split_into_fibonacci(s: str) -> List[int]:
    pass


if __name__ == "__main__":
    assert split_into_fibonacci("123456579") == [123, 456, 579]
    assert split_into_fibonacci("11235813") == [1, 1, 2, 3, 5, 8, 13]
    assert split_into_fibonacci("112358130") == []
    assert split_into_fibonacci("0123") == []   # leading zero
    print("All tests passed!")
