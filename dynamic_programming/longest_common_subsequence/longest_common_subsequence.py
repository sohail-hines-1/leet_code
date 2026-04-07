# LeetCode #1143 — Longest Common Subsequence
#
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence is a sequence derived from another by deleting some characters without
# changing the order of the remaining characters.
#
# Example:
#   Input:  text1 = "abcde", text2 = "ace"
#   Output: 3   ("ace" is a common subsequence)
#
#   Input:  text1 = "abc", text2 = "def"
#   Output: 0   (no common subsequence)

def longest_common_subsequence(text1: str, text2: str) -> int:
    pass


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("bl", "yby") == 1
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("abcba", "abcbcba") == 5
    print("All tests passed!")
