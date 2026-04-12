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
    from collections import Counter
    needs = Counter(t)
    have = {}
    satisfied = 0
    required = len(needs)
    left = 0
    min_length = float('inf')
    min_left, min_right = 0, 0

    for right in range(len(s)):
        c = s[right]
        if c in needs:
            have[c] = have.get(c, 0) + 1
            if have[c] == needs[c]:
                satisfied += 1

        while satisfied == required:
            # snapshot the window
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left, min_right = left, right
            # attempt to shrink left
            if s[left] in needs:
                have[s[left]] -= 1
                if have[s[left]] < needs[s[left]]:
                    satisfied -= 1
            left += 1

    return s[min_left:min_right + 1] if min_length != float('inf') else ""

def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

if __name__ == "__main__":
    assert min_window("AABCDDBEAXYCZABCDEABCDZZZ", "ABCDE") == "ABCDE"
    assert min_window("BCAB", "AB") == "AB"
    assert min_window("bba", "ab") == "ba"
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("XAYBZCDPQRSTABCDEFGHIJKLM", "ABCD") == "ABCD"
    assert min_window("a", "aa") == ""
    print("All tests passed!")
