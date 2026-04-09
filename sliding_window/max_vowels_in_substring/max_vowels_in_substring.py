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

vowels = {"a", "e", "i", "o", "u"}

def vowel_counter(str):
    return len([char for char in str if char in vowels])

def max_vowels(s: str, k: int) -> int:
    max_vowels = 0
    e = len(s) - k
    for i in range(0, e + 1):
        substr = s[i : i + k]
        max_vowels = max(max_vowels, vowel_counter(substr))

    return max_vowels

if __name__ == "__main__":
    assert max_vowels("abciiidef", 3) == 3
    assert max_vowels("aeiou", 2) == 2
    assert max_vowels("leetcode", 3) == 2
    assert max_vowels("rhythms", 4) == 0
    assert max_vowels("tryhard", 4) == 1
    print("All tests passed!")
