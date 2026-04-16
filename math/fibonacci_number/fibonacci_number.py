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

    first = 0                               # Note: lowest possible start values of 0, 1
    second = 1

    while n > 1:
        old_second = second                 # second will be pushed to first, so save it
        second = first + second             # compute the sum and assign to second
        first = old_second                  # assign the old-second to first
        n -= 1                              # Note: decrement AFTER

    return second


def fib_new(n: int) -> int:

    # Important pre-condition
    if n <= 1:
        return n

    # Note: no recursion needed
    first = 0
    second = 1
    fib_sum = 0
    for _ in range(0, n - 1):
        fib_sum = first + second        # Important: add before incrementing pointers
        tmp = first
        first = second
        second = first + tmp            # second = first + the previous value of first

    return fib_sum


if __name__ == "__main__":
    for fn in (fib, fib_new):
        assert fn(4) == 3
        assert fn(0) == 0
        assert fn(1) == 1
        assert fn(2) == 1
        assert fn(10) == 55
    print("All tests passed!")
