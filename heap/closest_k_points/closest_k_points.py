# Closest K Points to Origin (namedtuple variant)
#
# Given a list of Point(x, y) named tuples, return the k closest points to
# the origin (0, 0). Distance is Euclidean. Order of output does not matter.
#
# Example:
#   Input:  points = [Point(1, 3), Point(-2, 2)], k = 1
#   Output: [Point(-2, 2)]   (sqrt(8) < sqrt(10))
#
#   Input:  points = [Point(3, 3), Point(5, -1), Point(-2, 4)], k = 2
#   Output: [Point(3, 3), Point(-2, 4)]
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def k_closest(points: list[Point], k: int) -> list[Point]:
    pass


if __name__ == "__main__":
    result = k_closest([Point(1, 3), Point(-2, 2)], 1)
    assert len(result) == 1
    assert Point(-2, 2) in result

    result = k_closest([Point(3, 3), Point(5, -1), Point(-2, 4)], 2)
    assert len(result) == 2
    assert Point(3, 3) in result
    assert Point(-2, 4) in result

    result = k_closest([Point(0, 0), Point(1, 1), Point(2, 2)], 2)
    assert len(result) == 2
    assert Point(0, 0) in result
    assert Point(1, 1) in result

    print("All tests passed!")
