# LeetCode #424 — Longest Repeating Character Replacement
#
# Given a string s and an integer k, you can replace at most k characters.
# Return the length of the longest substring containing the same letter
# you can get after performing the replacements.
#
# Example:
#   Input:  s = "ABAB", k = 2
#   Output: 4
from collections import Counter
from typing import List


def character_replacement(s: str, k: int) -> int:
    have = 0
    need = k
    left = 0
    right = 0
    max_window = 0

    while right < len(s):
        window_str = s[left:right + 1]
        char_counts = Counter(window_str)

        # get the most frequent character in our window
        max_val = max(char_counts.values())
        is_valid = (right - left + 1) - max_val <= k              # important criteria
        if is_valid:
            max_window = max(max_window, right - left + 1)
            right += 1
        else:
            while not is_valid and max_window > 0:
                max_window = max(max_window, right - left + 1)
                left += 1
                window_str = s[left:right + 1]
                char_counts = Counter(window_str)
                max_val = max(char_counts.values())
                is_valid = (right - left + 1) - max_val <= k

    return max_window



if __name__ == "__main__":
    assert character_replacement("ABABBA", 2) == 5
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AAAA", 2) == 4       # all same char, no replacements needed
    assert character_replacement("ABCDE", 1) == 2      # all different, k=1 gives window of 2
    assert character_replacement("AABABBA", 0) == 2    # no replacements allowed, longest run of same char
    assert character_replacement("AAABBC", 2) == 5     # replace 2 of B/C to extend AAA run
    print("All tests passed!")
