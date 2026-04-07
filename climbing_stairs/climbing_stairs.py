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
#    assert climbing_stairs(1) == 1
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(4) == 5
    assert climbing_stairs(5) == 8
    assert climbing_stairs(10) == 89
    print("All tests passed!")
