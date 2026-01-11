#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

from collections import defaultdict
from typing import Dict


class GNode:
    def __init__(self):
        self.inDeg = 0
        self.children = []


class Solution:
    def topologicalSort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        graph = defaultdict(GNode)
        for next, prev in prerequisites:
            graph[prev].children.append(next)
            graph[next].inDeg += 1

        sources = []
        removed = 0
        for key, _ in graph.items():
            node = graph[key]
            if node.inDeg == 0:
                sources.append(key)
        while sources:
            source = sources.pop(0)
            for child in graph[source].children:
                childNode = graph[child]
                childNode.inDeg -= 1
                removed += 1
                if childNode.inDeg == 0:
                    sources.append(child)
        print(removed)
        if removed != len(prerequisites):
            return False
        return True

    def postOrderDfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Strategy 1: Post order DFS
        Runtime: O(|e| + v), wwhere e is the length of prerequisites and v 
        numCourses
        Space: O(n)

        Args:
            numCourses (int): the total of courses can take
            prerequisites (List[List[int]]): the constraints

        Returns:
            bool: determine whether a student can finished all courses
        """
        courseDict = defaultdict(list)

        for nextC, prev in prerequisites:
            courseDict[prev].append(nextC)

        checked, path = [False] * numCourses, [False] * numCourses

        def isCyclic(course: int) -> bool:
            if checked[course] or course not in courseDict:
                return False

            if path[course]:
                return True

            has = False
            path[course] = True
            for nextC in courseDict[course]:
                has = isCyclic(nextC)
                if has:
                    break

            path[course] = False
            checked[course] = True
            return has

        for i in range(numCourses):
            if isCyclic(i):
                return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.topologicalSort(numCourses, prerequisites)
        # @lc code=end
