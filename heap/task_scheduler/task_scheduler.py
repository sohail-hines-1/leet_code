# LeetCode #621 — Task Scheduler (namedtuple variant)
#
# Given a list of Task(name, count) named tuples and a cooldown n, return the
# minimum number of CPU intervals needed to execute all tasks. The CPU must
# wait at least n intervals between two executions of the same task; it may
# idle in between.
#
# Example:
#   Input:  tasks = [Task('A', 3), Task('B', 3)], n = 2
#   Output: 8   (A -> B -> idle -> A -> B -> idle -> A -> B)
#
#   Input:  tasks = [Task('A', 3), Task('B', 2), Task('C', 1)], n = 2
#   Output: 7   (A -> B -> C -> A -> B -> idle -> A)
#
#   Input:  tasks = [Task('A', 1), Task('B', 1), Task('C', 1)], n = 0
#   Output: 3
from collections import namedtuple

Task = namedtuple('Task', ['name', 'count'])


def least_interval(tasks: list[Task], n: int) -> int:
    pass


if __name__ == "__main__":
    assert least_interval([Task('A', 3), Task('B', 3)], 2) == 8
    assert least_interval([Task('A', 3), Task('B', 2), Task('C', 1)], 2) == 7
    assert least_interval([Task('A', 1), Task('B', 1), Task('C', 1)], 0) == 3
    assert least_interval([Task('A', 4)], 3) == 13  # A->idle->idle->idle->A->...
    print("All tests passed!")
