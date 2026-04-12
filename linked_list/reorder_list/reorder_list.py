# LeetCode #143 — Reorder List
#
# Given a linked list L0 → L1 → … → Ln-1 → Ln, reorder it in-place to:
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
#
# Example:
#   Input:  head = [1,2,3,4]
#   Output: [1,4,2,3]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    pass


if __name__ == "__main__":
    # node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    # reorder_list(node)  # in-place: [1,4,2,3]
    pass
