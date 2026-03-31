from typing import List


def trap(height: List[int]) -> int:
    max_value = max(height)
    trapped = 0
    trapping = False

    for j in range(max_value, 0, -1):
        trapping = False
        pending = 0
        for i in range(0, len(height)):
            if height[i] >= j:
                trapped += pending
                pending = 0
                trapping = True
            elif trapping:
                pending += 1

    return trapped

if __name__ == "__main__":
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([1, 0, 1]) == 1
    assert trap([3, 0, 2, 0, 4]) == 7
    assert trap([0]) == 0
    print("All tests passed!")
