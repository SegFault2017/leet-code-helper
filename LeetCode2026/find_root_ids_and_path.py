"""
You are given a collection of string blocks, each represented as a JSON object with fields {"id": string, "parentId": string | null}. A block is a root if it has no parent(parentId is null or the referenced parent does not appear).
"""

# Test 1: Empty collection
test_empty = []

# Test 2: Single root node
test_single_root = [
    {"id": "A", "parentId": None}
]

# Test 3: Linear chain (only "A" is root)
test_chain = [
    {"id": "A", "parentId": None},
    {"id": "B", "parentId": "A"},
    {"id": "C", "parentId": "B"}
]

# Test 4: Tree with branching (one root, multiple children)
test_branching_tree = [
    {"id": "root", "parentId": None},
    {"id": "child1", "parentId": "root"},
    {"id": "child2", "parentId": "root"},
    {"id": "grandchild", "parentId": "child1"}
]

# Test 5: Orphan node (parentId "X" doesn't exist → "B" is also a root)
test_orphan = [
    {"id": "A", "parentId": None},
    {"id": "B", "parentId": "X"}
]

# Test 6: Forest (multiple disconnected trees)
test_forest = [
    {"id": "A", "parentId": None},
    {"id": "B", "parentId": "A"},
    {"id": "C", "parentId": None},
    {"id": "D", "parentId": "C"}
]

# Test 7: Self-reference edge case
test_self_reference = [
    {"id": "A", "parentId": "A"}
]

# Test 8: All orphans (none of the parents exist)
test_all_orphans = [
    {"id": "A", "parentId": "Z"},
    {"id": "B", "parentId": "Y"},
    {"id": "C", "parentId": "X"}
]

# Test 9: Deep nesting
test_deep = [
    {"id": "L1", "parentId": None},
    {"id": "L2", "parentId": "L1"},
    {"id": "L3", "parentId": "L2"},
    {"id": "L4", "parentId": "L3"},
    {"id": "L5", "parentId": "L4"}
]

# Test 10: Mixed - some null parents, some orphans, some valid children
test_mixed = [
    {"id": "A", "parentId": None},      # Root (null parent)
    {"id": "B", "parentId": "A"},       # Child of A
    {"id": "C", "parentId": "MISSING"},  # Root (orphan)
    {"id": "D", "parentId": "C"},       # Child of C
    {"id": "E", "parentId": None}       # Root (null parent)
]
