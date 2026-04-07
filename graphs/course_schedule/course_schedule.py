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
    deps = {}
    can_finish = True
    max_courses = 0
    for i in range (len(prerequisites)):
        dep = prerequisites[i]
        if not dep[1] in deps:
            deps[dep[0]] = dep[1]
        else:
            can_finish = False

    return can_finish

if __name__ == "__main__":
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) == True
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) == False
    assert can_finish(2, [[1, 0], [0, 1]]) == False
    assert can_finish(2, [[1, 0]]) == True
    assert can_finish(1, []) == True
    print("All tests passed!")
