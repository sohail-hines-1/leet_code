def longest_common_subsequence(text1: str, text2: str) -> int:
    pass


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("bl", "yby") == 1
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("abcba", "abcbcba") == 5
    print("All tests passed!")
