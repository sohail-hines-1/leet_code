# Is Prime
#
# Given an integer n, return True if n is a prime number, False otherwise.
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
#
# Example:
#   Input:  n = 7
#   Output: True
#
#   Input:  n = 9
#   Output: False  (9 = 3 × 3)

def is_prime(n: int) -> bool:
    if n == 2:
        return True

    if n < 2:
        return False

    if n % 2 == 0:
        return False

    for i in range (n, 2, -1):
        if i != n and n % i == 0:
            return False

    return True

if __name__ == "__main__":
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(13) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(97) == True
    assert is_prime(100) == False
    print("All tests passed!")
