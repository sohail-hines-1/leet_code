# LeetCode #17 — Letter Combinations of a Phone Number
#
# Given a string containing digits 2-9, return all possible letter combinations
# that the number could represent (T9/phone keypad mapping).
#
# Example:
#   Input:  digits = "23"
#   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

from typing import List


def letter_combinations(digits: str) -> List[str]:
    pass


if __name__ == "__main__":
    assert letter_combinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert letter_combinations("") == []
    print("All tests passed!")
