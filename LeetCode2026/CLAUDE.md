# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a LeetCode problem-solving repository using Python 3.13. Individual solutions are stored at the root level with the naming convention `{problem_number}_{problem_name}.py` (e.g., `337_house_robber_iii.py`).

## Running Tests

The `test_framework/` directory contains a generic test harness for algorithm problems:

```bash
# Run tests (test file auto-detected as <algorithm>_test.py)
cd test_framework
python main.py -a ../solution.py -f solve
python main.py --timing                           # Show execution timing
python main.py --quiet                            # Summary only
```

## Test Framework Architecture

**test_runner.py** - Core test engine with `TestRunner` class:
- Supports three input formats: single value, `_args` list, `_kwargs` dict
- Default normalizer converts lists to sets for unordered comparison
- Custom `comparator` and `normalizer` functions supported

**Test case structure:**
```python
TEST_CASES = [
    {"name": "Test name", "input": data, "expected": result},
    {"name": "Multi-arg", "input": {"_args": [arg1, arg2]}, "expected": result},
]
```

## Development Workflow

1. Create solution file at root (e.g., `123_problem_name.py`)
2. Create corresponding test file (e.g., `123_problem_name_test.py`)
3. Run with: `python test_framework/main.py -a 123_problem_name.py -f solve`
