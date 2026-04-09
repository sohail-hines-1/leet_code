# LeetCode #8 — String to Integer (atoi)
#
# Implement atoi which converts a string to a 32-bit signed integer.
# Rules:
#   1. Ignore leading whitespace.
#   2. Read an optional '+' or '-' sign.
#   3. Read digits until a non-digit character or end of string.
#   4. Clamp the result to the 32-bit signed integer range [-2^31, 2^31 - 1].
#   5. Return 0 if no valid conversion is possible.
#
# Example:
#   Input:  s = "42"
#   Output: 42
#
#   Input:  s = "   -042"
#   Output: -42
#
#   Input:  s = "1337c0d3"
#   Output: 1337
#
#   Input:  s = "words and 987"
#   Output: 0


def my_atoi(s: str) -> int:
    pass


if __name__ == "__main__":
    assert my_atoi("42") == 42
    assert my_atoi("   -042") == -42
    assert my_atoi("1337c0d3") == 1337
    assert my_atoi("words and 987") == 0
    assert my_atoi("-91283472332") == -2**31        # clamp to INT_MIN
    assert my_atoi("91283472332") == 2**31 - 1      # clamp to INT_MAX
    print("All tests passed!")
