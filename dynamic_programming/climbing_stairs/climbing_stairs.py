# LeetCode #70 — Climbing Stairs
#
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Example:
#   Input:  n = 3
#   Output: 3
#   Explanation: 1+1+1, 1+2, 2+1
#
#   Input:  n = 5
#   Output: 8

def do_climb_stairs(param, target):
    if param == target:
        return 1

    count = 0

    if param + 1 > target:
        return 0
    else:
        count += do_climb_stairs(param + 1, target)

    if param + 2 > target:
        return count
    else:
        count += do_climb_stairs(param + 2, target)

    return count

def climbing_stairs(n: int) -> int:
    return do_climb_stairs(0, n)

if __name__ == "__main__":
    assert climbing_stairs(1) == 1
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(4) == 5
    assert climbing_stairs(5) == 8
    assert climbing_stairs(10) == 89
    print("All tests passed!")
