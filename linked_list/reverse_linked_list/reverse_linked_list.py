# LeetCode #206 — Reverse Linked List
#
# Given the head of a singly linked list, reverse the list and return the new head.
#
# Example:
#   Input:  1 → 2 → 3 → 4 → 5
#   Output: 5 → 4 → 3 → 2 → 1
#
#   Input:  1 → 2
#   Output: 2 → 1

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:

    # important initial state
    current = head
    prev = None

    # key takeaway is that the right side var is always reassigned in the next line

    # important exit condition focuses on CURRENT which STARTS at HEAD
    while current is not None:
        # Note: 4 total assignments
        saved_next = current.next
        current.next = prev
        prev = current
        current = saved_next

    # important: return prev, NOT current
    return prev

# Helpers
def to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def to_linked_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    assert to_list(reverse_list(to_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(to_linked_list([1, 2]))) == [2, 1]
    assert to_list(reverse_list(to_linked_list([1]))) == [1]
    assert to_list(reverse_list(to_linked_list([]))) == []
    assert to_list(reverse_list(to_linked_list([1, 2, 3]))) == [3, 2, 1]
    print("All tests passed!")
