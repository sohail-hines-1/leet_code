class MedianFinder:
    def __init__(self):
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5

    mf.add_num(3)
    assert mf.find_median() == 2.0

    mf2 = MedianFinder()
    mf2.add_num(6)
    assert mf2.find_median() == 6.0
    mf2.add_num(10)
    assert mf2.find_median() == 8.0
    mf2.add_num(2)
    assert mf2.find_median() == 6.0
    mf2.add_num(5)
    assert mf2.find_median() == 5.5

    print("All tests passed!")
