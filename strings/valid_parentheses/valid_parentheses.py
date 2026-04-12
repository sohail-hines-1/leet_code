# LeetCode #20 — Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid (brackets closed in correct order).
#
# Example:
#   Input:  s = "()"       → True
#   Input:  s = "()[]{}"   → True
#   Input:  s = "(]"       → False

from typing import List


def is_valid(s: str) -> bool:
    pass


if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    print("All tests passed!")
