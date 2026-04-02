def longest_palindrome(s: str) -> str:
    results = [0] * len(s)
    largest_index = 0
    largest_offset = 0
    offset = 0
    is_even = False

    for origin in range (1, len(s)):
        curr_size = 0

        if origin - offset < 0:
            break
        if origin + offset >= len(s):
            break

        offset = 0
        while s[origin - offset] == s[origin + offset]:
            if offset > largest_offset:
                largest_offset = offset
                largest_index = origin
            offset += 1
            if origin - offset < 0:
                break
            if origin + offset >= len(s):
                break

        offset = 0
        while s[origin] == s[origin + offset]:
            if offset > largest_offset:
                largest_offset = offset
                largest_index = origin
                is_even = True
            offset += 1
            if origin - offset < 0:
                break
            if origin + offset >= len(s):
                break

    if is_even:
        return s[largest_index : largest_index + largest_offset + 1]
    else:
        return s[largest_index - largest_offset : largest_index + largest_offset + 1]

if __name__ == "__main__":
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("abcba") == "abcba"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ("a", "c")
    print("All tests passed!")
