# LeetCode #3 — Longest Substring Without Repeating Characters
#
# Given a string s, return the length of the longest substring that contains
# no repeating characters.
#
# Example:
#   Input:  s = "abcabcbb"
#   Output: 3   ("abc")
#
#   Input:  s = "bbbbb"
#   Output: 1   ("b")
#
#   Input:  s = "pwwkew"
#   Output: 3   ("wke")


def length_of_longest_substring(s: str) -> int:
    pass


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("au") == 2
    print("All tests passed!")
