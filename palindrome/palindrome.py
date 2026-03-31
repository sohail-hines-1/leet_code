def is_palindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    assert is_palindrome("Racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == False
    assert is_palindrome("Level") == True
    assert is_palindrome("level") == True
    print("All tests passed!")
