import pytest
from add_two_numbers import ListNode, add_two_numbers


def to_linked_list(nums: list[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next


def to_list(node: ListNode) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# --- Tests ---

def test_example_1():
    # 342 + 465 = 807
    l1 = to_linked_list([2, 4, 3])
    l2 = to_linked_list([5, 6, 4])
    assert to_list(add_two_numbers(l1, l2)) == [7, 0, 8]


def test_example_2():
    # 0 + 0 = 0
    l1 = to_linked_list([0])
    l2 = to_linked_list([0])
    assert to_list(add_two_numbers(l1, l2)) == [0]


def test_example_3():
    # 9999999 + 9999 = 10009998
    l1 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = to_linked_list([9, 9, 9, 9])
    assert to_list(add_two_numbers(l1, l2)) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_carry_at_end():
    # 99 + 1 = 100
    l1 = to_linked_list([9, 9])
    l2 = to_linked_list([1])
    assert to_list(add_two_numbers(l1, l2)) == [0, 0, 1]


def test_different_lengths():
    # 99 + 1 = 100, l2 is shorter
    l1 = to_linked_list([1, 0, 0])
    l2 = to_linked_list([9, 9])
    # 001 + 099 = 100 → stored reversed: [0, 0, 1]
    assert to_list(add_two_numbers(l1, l2)) == [0, 0, 1]


def test_single_digit_no_carry():
    # 3 + 4 = 7
    l1 = to_linked_list([3])
    l2 = to_linked_list([4])
    assert to_list(add_two_numbers(l1, l2)) == [7]


def test_single_digit_with_carry():
    # 5 + 5 = 10
    l1 = to_linked_list([5])
    l2 = to_linked_list([5])
    assert to_list(add_two_numbers(l1, l2)) == [0, 1]
