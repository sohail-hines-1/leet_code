# LeetCode #424 — Longest Repeating Character Replacement
#
# Given a string s and an integer k, you can replace at most k characters.
# Return the length of the longest substring containing the same letter
# you can get after performing the replacements.
#
# Example:
#   Input:  s = "ABAB", k = 2
#   Output: 4

from typing import List


def character_replacement(s: str, k: int) -> int:
    pass


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    print("All tests passed!")
