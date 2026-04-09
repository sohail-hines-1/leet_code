# Maximum Number of Vowels in a Substring of Given Length (LeetCode 1456) — Medium
#
# Given a string s and an integer k, return the maximum number of vowel
# letters in any substring of s with length k.
# Vowel letters are: 'a', 'e', 'i', 'o', 'u'.
#
# Example:
#   Input:  s = "abciiidef", k = 3
#   Output: 3
#   Explanation: The substring "iii" contains 3 vowel letters.
#
#   Input:  s = "aeiou", k = 2
#   Output: 2
#
#   Input:  s = "leetcode", k = 3
#   Output: 2


def max_vowels(s: str, k: int) -> int:
    pass


if __name__ == "__main__":
    assert max_vowels("abciiidef", 3) == 3
    assert max_vowels("aeiou", 2) == 2
    assert max_vowels("leetcode", 3) == 2
    assert max_vowels("rhythms", 4) == 0
    assert max_vowels("tryhard", 4) == 1
    print("All tests passed!")
