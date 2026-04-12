# LeetCode #91 — Decode Ways
#
# A string of digits can be decoded where '1'→'A' ... '26'→'Z'.
# Return the number of ways to decode the string.
#
# Example:
#   Input:  "12"
#   Output: 2
#
#   Input:  "226"
#   Output: 3
#
#   Input:  "06"
#   Output: 0

from typing import List


def num_decodings(s: str) -> int:
    pass


if __name__ == "__main__":
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    print("All tests passed!")
