from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert merge([[1, 2]]) == [[1, 2]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    print("All tests passed!")
