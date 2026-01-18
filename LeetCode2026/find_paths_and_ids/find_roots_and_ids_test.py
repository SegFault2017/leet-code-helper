#!/usr/bin/env python3
"""
Test cases for the 'find roots' algorithm.

A block is a root if:
  1. parentId is None, OR
  2. parentId references an ID that doesn't exist in the collection
"""

TEST_CASES = [
    {
        "name": "Empty collection",
        "input": [],
        "expected": set()
    },
    {
        "name": "Single root node",
        "input": [
            {"id": "A", "parentId": None}
        ],
        "expected": {"A"}
    },
    {
        "name": "Linear chain",
        "input": [
            {"id": "A", "parentId": None},
            {"id": "B", "parentId": "A"},
            {"id": "C", "parentId": "B"}
        ],
        "expected": {"A"}
    },
    {
        "name": "Tree with branching",
        "input": [
            {"id": "root", "parentId": None},
            {"id": "child1", "parentId": "root"},
            {"id": "child2", "parentId": "root"},
            {"id": "grandchild", "parentId": "child1"}
        ],
        "expected": {"root"}
    },
    {
        "name": "Orphan node (missing parent)",
        "input": [
            {"id": "A", "parentId": None},
            {"id": "B", "parentId": "X"}
        ],
        "expected": {"A", "B"}
    },
    {
        "name": "Forest (multiple trees)",
        "input": [
            {"id": "A", "parentId": None},
            {"id": "B", "parentId": "A"},
            {"id": "C", "parentId": None},
            {"id": "D", "parentId": "C"}
        ],
        "expected": {"A", "C"}
    },
    {
        "name": "Self-reference",
        "input": [
            {"id": "A", "parentId": "A"}
        ],
        "expected": {"A"}
    },
    {
        "name": "All orphans",
        "input": [
            {"id": "A", "parentId": "Z"},
            {"id": "B", "parentId": "Y"},
            {"id": "C", "parentId": "X"}
        ],
        "expected": {"A", "B", "C"}
    },
    {
        "name": "Deep nesting",
        "input": [
            {"id": "L1", "parentId": None},
            {"id": "L2", "parentId": "L1"},
            {"id": "L3", "parentId": "L2"},
            {"id": "L4", "parentId": "L3"},
            {"id": "L5", "parentId": "L4"}
        ],
        "expected": {"L1"}
    },
    {
        "name": "Mixed roots",
        "input": [
            {"id": "A", "parentId": None},
            {"id": "B", "parentId": "A"},
            {"id": "C", "parentId": "MISSING"},
            {"id": "D", "parentId": "C"},
            {"id": "E", "parentId": None}
        ],
        "expected": {"A", "C", "E"}
    },
    {
        "name": "Circular reference",
        "input": [
            {"id": "A", "parentId": "C"},
            {"id": "B", "parentId": "A"},
            {"id": "C", "parentId": "B"}
        ],
        "expected": set()
    },
    {
        "name": "Large flat structure (all roots)",
        "input": [
            {"id": f"node_{i}", "parentId": None} for i in range(10)
        ],
        "expected": {f"node_{i}" for i in range(10)}
    },
]
