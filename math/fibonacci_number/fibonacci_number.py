# LeetCode #509 — Fibonacci Number
#
# Given n, return F(n) where F(0) = 0, F(1) = 1, and
# F(n) = F(n - 1) + F(n - 2) for n > 1.
#
# Example:
#   Input:  n = 4
#   Output: 3   (0, 1, 1, 2, 3)
#
#   Input:  n = 10
#   Output: 55
def fib(n: int) -> int:
    if n == 0:
        return 0

    first = 0
    second = 1

    while n > 1:
        temp = second
        second = first + second
        first = temp
        n -= 1

    return second



if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(4) == 3
    assert fib(10) == 55
    print("All tests passed!")
