# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a generic Python test framework designed for LeetCode-style algorithm problems. The framework separates algorithm implementations from test cases, making it easy to develop and verify solutions.

## Running Tests

### Basic Usage
```bash
# Run tests with default files (algorithm.py, test_cases.py)
python main.py

# Run specific algorithm and test files
python main.py -a my_solution.py -f my_function -t my_tests.py

# Show execution timing for each test
python main.py --timing

# Quiet mode (only show summary)
python main.py --quiet
```

### Standalone Test Runner
```bash
# Run the self-contained test harness (legacy)
python algo_perf.py
```

## Architecture

### Core Components

**test_runner.py** - Generic test runner engine
- `TestRunner` class handles test execution with customizable comparison and normalization
- Supports three test input formats:
  - Single value: `algorithm(input_data)`
  - Args list: `algorithm(*input_data["_args"])`
  - Kwargs dict: `algorithm(**input_data["_kwargs"])`
- Default behavior converts lists to sets for unordered comparison
- Returns `TestResult` objects with status (PASS/FAIL/ERROR), timing, and error details

**main.py** - CLI entry point
- Provides `run_tests()` for programmatic use with in-memory algorithm/test_cases
- Provides `run_from_files()` for loading algorithm and tests from separate files
- Uses dynamic module loading via `importlib.util.spec_from_file_location()`
- Exit code 1 if any tests fail or error, 0 if all pass

### File Structure Pattern

**algorithm.py** - Algorithm implementation stub
- Contains the function to be tested (e.g., `find_roots()`)
- Implement your solution here

**test_cases.py** - Test case definitions
- Exports `TEST_CASES` list of dicts with structure:
  ```python
  {
      "name": "Test description",
      "input": input_data,  # or {"_args": [...]} or {"_kwargs": {...}}
      "expected": expected_output
  }
  ```

**algo_perf.py** - Legacy self-contained test harness
- Contains both algorithm and test cases in a single file
- Useful for standalone problem solving without dependencies

## Key Behaviors

### Test Case Input Formats
The test runner supports multiple input patterns:
- Direct input: `"input": [1, 2, 3]` calls `algorithm([1, 2, 3])`
- Multiple args: `"input": {"_args": [arg1, arg2]}` calls `algorithm(arg1, arg2)`
- Keyword args: `"input": {"_kwargs": {"key": "value"}}` calls `algorithm(key="value")`

### Output Normalization
By default, the test runner normalizes list outputs to sets for unordered comparison. Override with custom `normalizer` if needed.

### Custom Comparison
Pass a `comparator` function to `TestRunner` for non-equality comparisons (e.g., floating-point tolerance, structural equivalence).

## Typical Development Workflow

1. Implement algorithm in `algorithm.py` (or custom file)
2. Define test cases in `test_cases.py` (or custom file)
3. Run `python main.py` to verify solution
4. Use `--timing` flag to analyze performance
5. For quick iterations, modify `algo_perf.py` as a self-contained workspace
