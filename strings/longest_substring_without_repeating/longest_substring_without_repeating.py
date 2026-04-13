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
    char_counts = {}
    left = 0
    right = 0
    longest = 0
    while right < len(s):
        if s[right] not in char_counts:
            char_counts[s[right]] = 0
        char_counts[s[right]] += 1

        # add to longest only if this is not a duplicate
        if char_counts[s[right]] == 1:
            longest = right - left + 1

        # we have duplicates now, so try to trim from left until all dupes are gone.
        # Note: we loop while checking for s[right] since left will be changing!
        while char_counts[s[right]] > 1:
            char_counts[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)    # Note: update longest AFTER left trim
        right += 1

    return longest


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("au") == 2
    print("All tests passed!")
