# LeetCode #12 — Integer to Roman
#
# Given an integer, convert it to a Roman numeral string.
# Symbol values: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Subtraction forms: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
# Input is guaranteed to be in range [1, 3999].
#
# Example:
#   Input:  num = 3749
#   Output: "MMMDCCXLIX"   (MMM=3000, DCC=700, XL=40, IX=9)
#
#   Input:  num = 58
#   Output: "LVIII"   (L=50, V=5, III=3)
#
#   Input:  num = 1994
#   Output: "MCMXCIV"   (M=1000, CM=900, XC=90, IV=4)


def int_to_roman(num: int) -> str:
    pass


if __name__ == "__main__":
    assert int_to_roman(3) == "III"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(58) == "LVIII"
    assert int_to_roman(1994) == "MCMXCIV"
    assert int_to_roman(3749) == "MMMDCCXLIX"
    print("All tests passed!")
