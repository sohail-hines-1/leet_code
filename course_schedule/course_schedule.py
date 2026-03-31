from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    pass


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) == True
    assert can_finish(2, [[1, 0], [0, 1]]) == False
    assert can_finish(1, []) == True
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) == True
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) == False
    print("All tests passed!")
