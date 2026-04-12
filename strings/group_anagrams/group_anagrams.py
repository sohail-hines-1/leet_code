# LeetCode #49 — Group Anagrams
#
# Given an array of strings, group the anagrams together and return the groups
# in any order.
#
# Example:
#   Input:  strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    pass


if __name__ == "__main__":
    # assert group_anagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert group_anagrams([""]) == [[""]]
    print("All tests passed!")
