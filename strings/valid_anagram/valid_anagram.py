# LeetCode #242 — Valid Anagram
#
# Given two strings s and t, return True if t is an anagram of s, False otherwise.
# An anagram uses all the original letters exactly once.
#
# Example:
#   Input:  s = "anagram", t = "nagaram"
#   Output: True

from typing import List


def is_anagram(s: str, t: str) -> bool:
    pass


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    print("All tests passed!")
