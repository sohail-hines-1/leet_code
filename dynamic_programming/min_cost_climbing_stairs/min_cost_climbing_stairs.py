# Min Cost Climbing Stairs
#
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can climb either one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
#
# Example:
#   Input:  cost = [10, 15, 20]
#   Output: 15
#   Explanation: You start at index 1, pay 15, and climb two steps to reach the top.
#
#   Input:  cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#   Output: 6

from typing import List

class Climber:
    @classmethod
    def do_min_cost_climbing(cls, costs: List[int], position, step_size, cost):
        if position + step_size <= len(costs):
            key = position
            if key not in cls.min_costs:
                cls.min_costs[key] = costs[key]
            cost += cls.do_min_cost_climbing(costs, position + step_size, step_size, costs[position])

        return cost

    @classmethod
    def min_cost_climbing(cls, costs: List[int]) -> int:
        cls.min_costs = {}
        min_cost = min(
            cls.do_min_cost_climbing(costs, 0, 1, 0),
            cls.do_min_cost_climbing(costs, 0, 2, 0),
            cls.do_min_cost_climbing(costs, 1, 1, 0),
            cls.do_min_cost_climbing(costs, 1, 2, 0))
        return min_cost

if __name__ == "__main__":
    climber = Climber()

    assert climber.min_cost_climbing([5, 12, 17, 25, 32]) == 22
    assert climber.min_cost_climbing([10, 15, 20]) == 10
#    assert climber.min_cost_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    print("All tests passed!")
