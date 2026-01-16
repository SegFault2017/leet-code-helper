#!/usr/bin/env python3
"""
Algorithm implementation for the 'find roots' problem.

A block is a root if:
  1. parentId is None, OR
  2. parentId references an ID that doesn't exist in the collection
"""

from typing import List, Dict, Set, Optional


def find_roots(blocks: List[Dict[str, Optional[str]]]) -> Set[str]:
    """
    Find all root block IDs from the collection.
    
    Args:
        blocks: List of blocks, each with {"id": str, "parentId": str | None}
    
    Returns:
        Set of IDs that are roots
    
    Example:
        >>> find_roots([{"id": "A", "parentId": None}, {"id": "B", "parentId": "A"}])
        {"A"}
    """
    # TODO: Implement your algorithm here

    # Hint: You'll likely need to:
    # 1. Build a set of all existing IDs
    # 2. Check each block to see if it's a root
    parents = set()
    all_ids = set()
    for block in blocks:
        id = block["id"]
        all_ids.add(id)
    for block in blocks:
        block_id = block["id"]
        parent_id = block["parentId"]
            
        if parent_id is None or parent_id not in all_ids:
            parents.add(block_id)
        
        if block_id == parent_id:
            parents.add(block_id)
    
    return parents 
    
    