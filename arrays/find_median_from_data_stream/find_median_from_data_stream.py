# LeetCode #295 — Find Median from Data Stream
#
# Design a data structure that supports adding integers and finding the median
# of all elements seen so far. The median is the middle value in a sorted list;
# if the list has even length, the median is the average of the two middle values.
#
# Example:
#   add_num(1), add_num(2) → find_median() == 1.5
#   add_num(3)             → find_median() == 2.0

from sortedcontainers import SortedList
class MedianFinder:
    all_nums = SortedList()

    def __init__(self):
        self.all_nums.clear()

    def add_num(self, num: int) -> None:
        self.all_nums.add(num)

    def find_median(self) -> float:
        if len(self.all_nums) % 2 == 0:
            med_index = (len(self.all_nums) - 1) // 2
            v1 = self.all_nums[med_index]
            v2 = self.all_nums[med_index + 1]
            return (v2 + v1) / 2
        else:
            med_index = len(self.all_nums) // 2
            return float(self.all_nums[med_index])

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
