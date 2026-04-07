# LeetCode #58 — Length of Last Word
#
# Given a string s consisting of words and spaces, return the length of the last word.
# A word is a maximal substring consisting of non-space characters only.
#
# Example:
#   Input:  s = "Hello World"
#   Output: 5
#
#   Input:  s = "   fly me   to   the moon  "
#   Output: 4  (trailing spaces are ignored)

def length_of_last_word(s: str) -> int:
    length = 0
    for i in range(0, len(str)):
        if s[i] != ' ':
            length += 1
        else:
            length = 0

    return length

if __name__ == "__main__":
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    assert length_of_last_word("luffy is still joyboy") == 6
    assert length_of_last_word("a") == 1
    print("All tests passed!")
