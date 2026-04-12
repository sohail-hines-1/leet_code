# LeetCode #139 — Word Break
#
# Given a string s and a dictionary of strings wordDict, return true if s
# can be segmented into space-separated dictionary words.
#
# Example:
#   Input:  s="leetcode", wordDict=["leet", "code"]
#   Output: True
#
#   Input:  s="applepenapple", wordDict=["apple", "pen"]
#   Output: True

from typing import List


def word_break(s: str, wordDict: List[str]) -> bool:
    pass


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) == True
    assert word_break("applepenapple", ["apple", "pen"]) == True
    print("All tests passed!")
