# LeetCode #21 — Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new sorted list by splicing
# together the nodes of the two lists.
#
# Example:
#   Input:  list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    pass


if __name__ == "__main__":
    # assert merge_two_lists([1,2,4], [1,3,4]) produces [1,1,2,3,4,4]
    assert merge_two_lists(None, None) is None
    print("All tests passed!")
