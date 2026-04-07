# LeetCode #983 — Minimum Cost For Tickets
#
# You have a list of days you need to travel this year (1–365).
# Train passes are available for 1 day ($costs[0]), 7 days ($costs[1]), 30 days ($costs[2]).
# Return the minimum cost to travel on all the given days.
#
# Example:
#   Input:  days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]
#   Output: 11   (1-day on day 1, 7-day on day 4 covers 4–10, 1-day on day 20)
#
#   Input:  days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2, 7, 15]
#   Output: 17

from typing import List


def min_cost_tickets(days: List[int], costs: List[int]) -> int:
    pass


if __name__ == "__main__":
    # costs: [1-day, 7-day, 30-day]
    assert min_cost_tickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
    assert min_cost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17
    assert min_cost_tickets([1], [2, 7, 15]) == 2
    assert min_cost_tickets([1, 365], [2, 7, 15]) == 4
    print("All tests passed!")
