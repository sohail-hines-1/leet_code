def min_window(s: str, t: str) -> str:
    pass


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("bba", "ab") == "ba"
    assert min_window("ADOBECODEBANC", "BANC") == "BANC"
    print("All tests passed!")
