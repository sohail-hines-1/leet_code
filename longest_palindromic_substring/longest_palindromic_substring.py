def longest_palindrome(s: str) -> str:

    offset = 1
    saved_size = 0
    saved_offset = 0
    saved_origin = -1
    is_odd = False

    # check for even length palindrome expansion
    for origin in range (0, len(s)):
        size = 0
        offset = 0

        if origin - offset < 0:
            continue
        if origin + offset + 1 >= len(s):
            continue

        while s[origin - offset] == s[origin + offset + 1]:
            size += 1
            if size > saved_size:
                saved_size = size
                saved_origin = origin
                saved_offset = offset
            offset += 1
            if origin + offset + 1 >= len(s):
                break

    for origin in range (1, len(s) - 1):
        size = 0
        offset = 0
        while s[origin - offset] == s[origin + offset]:
            size += 1
            if size > saved_size:
                saved_size = size
                saved_origin = origin
                saved_offset = offset
                is_odd = True
            offset += 1
            if origin + offset >= len(s):
                break

    if saved_origin == -1:
        return s[0]
    elif is_odd:
        return s[saved_origin - saved_offset : saved_origin + saved_offset + 1]
    else:
        return s[saved_origin - saved_offset : saved_origin + saved_offset + 2]



if __name__ == "__main__":
    assert longest_palindrome("aabbaa") == "aabbaa"
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("abcba") == "abcba"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("ac") in ("a", "c")
    print("All tests passed!")
