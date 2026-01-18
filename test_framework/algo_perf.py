#!/usr/bin/env python3
"""
Test harness for the 'find roots' algorithm.
A block is a root if:
  1. parentId is None, OR
  2. parentId references an ID that doesn't exist in the collection
"""

from typing import List, Dict, Set, Optional

# =============================================================================
# YOUR ALGORITHM - IMPLEMENT THIS FUNCTION
# =============================================================================


def find_roots(blocks: List[Dict[str, Optional[str]]]) -> Set[str]:
    """
    Find all root block IDs from the collection.
    
    Args:
        blocks: List of blocks, each with {"id": str, "parentId": str | None}
    
    Returns:
        Set of IDs that are roots
    """
    # TODO: Implement your algorithm here
    pass


# =============================================================================
# TEST CASES
# =============================================================================

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
        "expected": {"A"}  # Self-reference means parent doesn't validly exist
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
        "expected": set()  # All parents exist, so no roots
    },
    {
        "name": "Large flat structure (all roots)",
        "input": [
            {"id": f"node_{i}", "parentId": None} for i in range(10)
        ],
        "expected": {f"node_{i}" for i in range(10)}
    },
]


# =============================================================================
# TEST RUNNER
# =============================================================================

def run_tests(algorithm=find_roots, verbose: bool = True) -> Dict[str, int]:
    """
    Run all test cases against the provided algorithm.
    
    Args:
        algorithm: Function that takes blocks and returns set of root IDs
        verbose: If True, print detailed output for each test
    
    Returns:
        Dictionary with 'passed' and 'failed' counts
    """
    passed = 0
    failed = 0
    failures = []

    print("=" * 60)
    print("RUNNING TESTS")
    print("=" * 60)
    print()

    for i, test in enumerate(TEST_CASES, 1):
        name = test["name"]
        input_data = test["input"]
        expected = test["expected"]

        try:
            result = algorithm(input_data)

            # Convert to set if returned as list
            if isinstance(result, list):
                result = set(result)

            if result == expected:
                passed += 1
                status = "✓ PASS"
                if verbose:
                    print(f"Test {i:2d}: {status} - {name}")
            else:
                failed += 1
                status = "✗ FAIL"
                failures.append({
                    "name": name,
                    "input": input_data,
                    "expected": expected,
                    "actual": result
                })
                if verbose:
                    print(f"Test {i:2d}: {status} - {name}")
                    print(f"         Expected: {expected}")
                    print(f"         Actual:   {result}")

        except Exception as e:
            failed += 1
            status = "✗ ERROR"
            failures.append({
                "name": name,
                "input": input_data,
                "expected": expected,
                "actual": f"Exception: {e}"
            })
            if verbose:
                print(f"Test {i:2d}: {status} - {name}")
                print(f"         Exception: {e}")

    # Summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    total = passed + failed
    print(f"Passed: {passed}/{total}")
    print(f"Failed: {failed}/{total}")

    if passed == total:
        print("\n🎉 All tests passed!")
    elif failures:
        print(f"\n❌ {failed} test(s) failed")

    return {"passed": passed, "failed": failed, "total": total}


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    run_tests()
