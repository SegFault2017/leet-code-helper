#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict


class GNode:
    def __init__(self) -> None:
        self.inDeg = 0
        self.children = []
        return


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Strategy 1: Topological sort
        Runtime:O(|E| + |V|)
        Spacetime: O(|E| + |V|)

        Args:
            numCourses (int): # of courses
            prerequisites (List[List[int]]): list of edges

        Returns:
            List[int]: return a list of course ordering 
        """
        n = len(prerequisites)

        graph = defaultdict(GNode)
        ordered, sources = [], []
        removed = 0
        for next, prev in prerequisites:
            graph[prev].children.append(next)
            graph[next].inDeg += 1

        for i in range(numCourses):
            if i not in graph or graph[i].inDeg == 0:
                sources.append(i)

        while sources:
            source = sources.pop(0)
            ordered.append(source)
            if source not in graph:
                continue
            for child in graph[source].children:
                childNode = graph[child]
                childNode.inDeg -= 1
                removed += 1
                if childNode.inDeg == 0:
                    sources.append(child)
        if removed != n:
            return []

        return ordered

# @lc code=end
