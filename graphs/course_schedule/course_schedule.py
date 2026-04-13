# LeetCode #207 — Course Schedule
#
# There are numCourses courses labeled 0 to numCourses-1.
# Given a list of prerequisite pairs [a, b] meaning you must take course b before a,
# return True if you can finish all courses, or False if there is a cycle.
#
# Example:
#   Input:  numCourses = 2, prerequisites = [[1, 0]]
#   Output: True   (take 0 then 1)
#
#   Input:  numCourses = 2, prerequisites = [[1, 0], [0, 1]]
#   Output: False  (cycle: 0 requires 1, 1 requires 0)

from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    

if __name__ == "__main__":
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) == True       # simple chain, no cycle
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) == False       # 3-node cycle
    assert can_finish(2, [[1, 0], [0, 1]]) == False               # 2-node cycle
    assert can_finish(2, [[1, 0]]) == True                        # single prerequisite
    assert can_finish(1, []) == True                              # single course, no prereqs
    assert can_finish(5, []) == True                              # many courses, no prereqs
    assert can_finish(6, [[1,0],[2,1],[3,2],[4,3],[5,4]]) == True  # long chain, no cycle
    assert can_finish(4, [[1,0],[2,0],[3,1],[3,2]]) == True        # diamond shape, no cycle
    assert can_finish(4, [[1,0],[2,1],[0,2],[3,0]]) == False       # cycle among first 3 nodes
    assert can_finish(6, [[1,0],[2,1],[1,2],[4,3],[5,4]]) == False # cycle in one component, not the other
    print("All tests passed!")
