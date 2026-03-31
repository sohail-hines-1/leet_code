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
    test_cases = ["Racecar", "hello", "A man a plan a canal Panama", "Level", "level"]
    for word in test_cases:
        print(f"{word!r} -> {is_palindrome(word)}")
