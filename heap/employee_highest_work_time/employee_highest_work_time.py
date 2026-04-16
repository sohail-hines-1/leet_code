# Employee Highest Work Time
#
# Given a list of Log(employee_id, start, end) named tuples representing work
# sessions, return the employee_id of the employee who worked the most total
# hours. If there is a tie, return the smaller employee_id.
#
# Example:
#   Input:  logs = [Log(1, 0, 5), Log(2, 0, 3), Log(1, 6, 10)]
#   Output: 1   (employee 1 worked 9 hours, employee 2 worked 3 hours)
#
#   Input:  logs = [Log(1, 0, 4), Log(2, 1, 5)]
#   Output: 1   (tie at 4 hours each — return smaller id)
from collections import namedtuple

Log = namedtuple('Log', ['employee_id', 'start', 'end'])


def highest_work_time(logs: list[Log]) -> int:
    pass


if __name__ == "__main__":
    assert highest_work_time([Log(1, 0, 5), Log(2, 0, 3), Log(1, 6, 10)]) == 1
    assert highest_work_time([Log(1, 0, 4), Log(2, 1, 5)]) == 1   # tie → smaller id
    assert highest_work_time([Log(3, 0, 2), Log(1, 0, 10)]) == 1
    assert highest_work_time([Log(2, 0, 8), Log(1, 0, 5), Log(2, 10, 13)]) == 2
    print("All tests passed!")
