# LeetCode #19 — Remove Nth Node From End of List
#
# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.
#
# Example:
#   Input:  head = [1,2,3,4,5], n = 2
#   Output: [1,2,3,5]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    pass


if __name__ == "__main__":
    # assert remove_nth_from_end([1,2,3,4,5], 2) == [1,2,3,5]
    assert remove_nth_from_end(ListNode(1), 1) is None
    print("All tests passed!")
