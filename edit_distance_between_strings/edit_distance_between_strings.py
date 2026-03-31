def min_distance(word1: str, word2: str) -> int:
    pass


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "") == 0
    assert min_distance("a", "") == 1
    assert min_distance("", "a") == 1
    assert min_distance("abc", "abc") == 0
    assert min_distance("ab", "ba") == 2
    print("All tests passed!")
