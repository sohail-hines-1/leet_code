# LeetCode #13 — Roman to Integer
#
# Given a Roman numeral string, convert it to an integer.
# Symbol values: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Subtraction rules: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
# (a smaller value preceding a larger value means subtraction)
#
# Example:
#   Input:  s = "III"
#   Output: 3
#
#   Input:  s = "LVIII"
#   Output: 58   (L=50, V=5, III=3)
#
#   Input:  s = "MCMXCIV"
#   Output: 1994   (M=1000, CM=900, XC=90, IV=4)


def roman_to_int(s: str) -> int:
    pass


if __name__ == "__main__":
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    print("All tests passed!")
