from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    pass


# Helpers
def build_list_with_cycle(values: list, cycle_pos: int) -> Optional[ListNode]:
    """Build a linked list where the tail connects back to node at cycle_pos (-1 = no cycle)."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


if __name__ == "__main__":
    # cycle at index 1: 3 -> 2 -> 0 -> 4 -> (back to 2)
    assert has_cycle(build_list_with_cycle([3, 2, 0, 4], 1)) == True
    # cycle at index 0: 1 -> 2 -> (back to 1)
    assert has_cycle(build_list_with_cycle([1, 2], 0)) == True
    # single node, no cycle
    assert has_cycle(build_list_with_cycle([1], -1)) == False
    # no cycle
    assert has_cycle(build_list_with_cycle([1, 2, 3, 4, 5], -1)) == False
    # empty list
    assert has_cycle(None) == False
    print("All tests passed!")
