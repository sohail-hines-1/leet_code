# LeetCode #269 — Alien Dictionary
#
# Given a sorted list of words in an alien language, derive the order of the
# alphabet. Return a string of unique characters in topological order, or ""
# if no valid ordering exists.
#
# Example:
#   Input:  words = ["wrt","wrf","er","ett","rftt"]
#   Output: "wertf"

from typing import List
from collections import defaultdict, deque


def alien_order(words: List[str]) -> str:
    pass


if __name__ == "__main__":
    assert alien_order(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert alien_order(["z", "x"]) == "zx"
    print("All tests passed!")
