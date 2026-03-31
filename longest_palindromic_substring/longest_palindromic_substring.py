def longest_palindrome(s: str) -> str:
    pass


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("abcba") == "abcba"
    assert longest_palindrome("ac") in ("a", "c")
    print("All tests passed!")
