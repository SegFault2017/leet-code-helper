#!/usr/bin/env python3
"""
Algorithm implementation for the 'find path to target' problem.

Given a collection of blocks and a target ID, return the path of IDs
from the root to that target.

A block is a root if:
  1. parentId is None, OR
  2. parentId references an ID that doesn't exist in the collection
"""

from typing import List, Dict, Set, Optional


def find_path(blocks: List[Dict[str, Optional[str]]], target: str) -> List[str]:
    """
    Find the path from root to target ID.
    
    Args:
        blocks: List of blocks, each with {"id": str, "parentId": str | None}
        target: The target ID to find the path to
    
    Returns:
        List of IDs from root to target (inclusive), or empty list if not found
    
    Examples:
        >>> find_path([{"id": "A", "parentId": None}, {"id": "B", "parentId": "A"}], "B")
        ["A", "B"]
        
        >>> find_path([{"id": "A", "parentId": None}], "Z")
        []
    """
    # TODO: Implement your algorithm here

    # =================================================================
    # HINTS - Consider the following approach:
    # =================================================================
    #
    # 1. BUILD A LOOKUP MAP
    #    - Create a map from id -> parentId for O(1) parent lookup
    #    - Create a set of all existing IDs
    #
    # 2. CHECK IF TARGET EXISTS
    #    - If target not in all_ids, return []
    #
    # 3. TRACE PATH UPWARD (child -> parent -> grandparent -> ... -> root)
    #    - Start from target
    #    - Keep moving to parent until you hit a root
    #    - A node is a root if parentId is None or parentId not in all_id   s
    #
    # 4. REVERSE THE PATH
    #    - You traced child->root, but need root->child
    #
    # 5. HANDLE CYCLES
    #    - What if there's a circular reference? (A->B->C->A)
    #    - Use a visited set to detect cycles
    #    - If cycle detected, return [] (no valid path to root)
    #
    # =================================================================
    # DATA STRUCTURES TO CONSIDER:
    # =================================================================
    #
    # - dict: id -> parentId mapping for O(1) lookup
    # - set: all existing IDs for O(1) existence check
    # - set: visited nodes for cycle detection
    # - list: to build the path
    #
    # =================================================================
    # COMPLEXITY ANALYSIS:
    # =================================================================
    #
    # Time Complexity:  O(?)
    #   - Building the map: ?
    #   - Tracing the path: ?
    #
    # Space Complexity: O(?)
    #   - Map storage: ?
    #   - Path storage: ?
    #
    # =================================================================
    
    all_ids = set()
    c_to_p = {}
    visited = {}
    
    for block in blocks:
        block_id, parent_id = block["id"], block["parent_id"]
        all_ids.add(block_id)
        c_to_p[block_id] = parent_id
        visited[block_id] = False
    
    if target not in all_ids:
        return False

    current = target
    parent = c_to_p[current]
    path = [current]
    visited[current] = True
    while parent and not visited[parent]:
        current = parent
        path.append(current)
        visited[current] = True
        parent = c_to_p[current]
    return path 