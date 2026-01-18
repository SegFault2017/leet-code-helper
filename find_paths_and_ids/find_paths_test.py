#!/usr/bin/env python3
"""
Test cases for the 'find path to target' algorithm.

Given a collection of blocks and a target ID, return the path of IDs
from the root to that target.

A block is a root if:
  1. parentId is None, OR
  2. parentId references an ID that doesn't exist in the collection
"""

TEST_CASES = [
    # ===================
    # Basic Cases
    # ===================
    {
        "name": "Empty collection",
        "input": {"_args": [[], "A"]},
        "expected": []
    },
    {
        "name": "Target not found",
        "input": {"_args": [
            [{"id": "A", "parentId": None}],
            "Z"
        ]},
        "expected": []
    },
    {
        "name": "Target is the root",
        "input": {"_args": [
            [{"id": "A", "parentId": None}],
            "A"
        ]},
        "expected": ["A"]
    },
    {
        "name": "Target is direct child of root",
        "input": {"_args": [
            [
                {"id": "A", "parentId": None},
                {"id": "B", "parentId": "A"}
            ],
            "B"
        ]},
        "expected": ["A", "B"]
    },

    # ===================
    # Linear Chains
    # ===================
    {
        "name": "Linear chain - target at end",
        "input": {"_args": [
            [
                {"id": "A", "parentId": None},
                {"id": "B", "parentId": "A"},
                {"id": "C", "parentId": "B"},
                {"id": "D", "parentId": "C"}
            ],
            "D"
        ]},
        "expected": ["A", "B", "C", "D"]
    },
    {
        "name": "Linear chain - target in middle",
        "input": {"_args": [
            [
                {"id": "A", "parentId": None},
                {"id": "B", "parentId": "A"},
                {"id": "C", "parentId": "B"},
                {"id": "D", "parentId": "C"}
            ],
            "B"
        ]},
        "expected": ["A", "B"]
    },

    # ===================
    # Branching Trees
    # ===================
    {
        "name": "Branching tree - left branch",
        "input": {"_args": [
            [
                {"id": "root", "parentId": None},
                {"id": "left", "parentId": "root"},
                {"id": "right", "parentId": "root"},
                {"id": "left_child", "parentId": "left"}
            ],
            "left_child"
        ]},
        "expected": ["root", "left", "left_child"]
    },
    {
        "name": "Branching tree - right branch",
        "input": {"_args": [
            [
                {"id": "root", "parentId": None},
                {"id": "left", "parentId": "root"},
                {"id": "right", "parentId": "root"},
                {"id": "right_child", "parentId": "right"}
            ],
            "right_child"
        ]},
        "expected": ["root", "right", "right_child"]
    },

    # ===================
    # Orphan Cases
    # ===================
    {
        "name": "Target is an orphan (missing parent)",
        "input": {"_args": [
            [
                {"id": "A", "parentId": None},
                {"id": "B", "parentId": "MISSING"}
            ],
            "B"
        ]},
        "expected": ["B"]
    },
    {
        "name": "Orphan with children",
        "input": {"_args": [
            [
                {"id": "A", "parentId": "MISSING"},
                {"id": "B", "parentId": "A"},
                {"id": "C", "parentId": "B"}
            ],
            "C"
        ]},
        "expected": ["A", "B", "C"]
    },

    # ===================
    # Forest (Multiple Trees)
    # ===================
    {
        "name": "Forest - target in first tree",
        "input": {"_args": [
            [
                {"id": "A", "parentId": None},
                {"id": "B", "parentId": "A"},
                {"id": "C", "parentId": None},
                {"id": "D", "parentId": "C"}
            ],
            "B"
        ]},
        "expected": ["A", "B"]
    },
    {
        "name": "Forest - target in second tree",
        "input": {"_args": [
            [
                {"id": "A", "parentId": None},
                {"id": "B", "parentId": "A"},
                {"id": "C", "parentId": None},
                {"id": "D", "parentId": "C"}
            ],
            "D"
        ]},
        "expected": ["C", "D"]
    },

    # ===================
    # Edge Cases
    # ===================
    {
        "name": "Self-reference",
        "input": {"_args": [
            [{"id": "A", "parentId": "A"}],
            "A"
        ]},
        "expected": ["A"]  # Self-reference is its own root
    },
    {
        "name": "Circular reference - target in cycle",
        "input": {"_args": [
            [
                {"id": "A", "parentId": "C"},
                {"id": "B", "parentId": "A"},
                {"id": "C", "parentId": "B"}
            ],
            "A"
        ]},
        "expected": []  # No valid path (infinite loop) or handle gracefully
    },
    {
        "name": "Deep nesting (10 levels)",
        "input": {"_args": [
            [{"id": f"L{i}", "parentId": None if i == 0 else f"L{i-1}"}
                for i in range(10)],
            "L9"
        ]},
        "expected": [f"L{i}" for i in range(10)]
    },
]
