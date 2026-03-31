from typing import List


def num_islands(grid: List[List[str]]) -> int:
    pass


if __name__ == "__main__":
    assert num_islands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]) == 1

    assert num_islands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]) == 3

    assert num_islands([["1"]]) == 1
    assert num_islands([["0"]]) == 0

    assert num_islands([
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]) == 5
    print("All tests passed!")
