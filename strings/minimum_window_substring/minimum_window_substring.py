# LeetCode #76 — Minimum Window Substring
#
# Given strings s and t, return the smallest substring of s that contains
# every character in t (including duplicates). If no such substring exists, return "".
#
# Example:
#   Input:  s = "ADOBECODEBANC", t = "ABC"
#   Output: "BANC"
#
#   Input:  s = "a", t = "aa"
#   Output: ""  (t has two a's but s only has one)

def min_window(s: str, t: str) -> str:
    pass


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("bba", "ab") == "ba"
    assert min_window("ADOBECODEBANC", "BANC") == "BANC"
    print("All tests passed!")
