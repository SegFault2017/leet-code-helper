#!/usr/bin/env python3
"""
Main entry point for running tests.

Usage:
    python main.py -a solution.py -f solve    # Test file auto-detected as solution_test.py
    python main.py -a solution.py -f solve --timing
    python main.py -a solution.py -f solve --quiet
"""

import argparse
import importlib.util
import sys
from typing import Callable, List, Dict, Any

from test_runner import TestRunner


def load_module_from_file(file_path: str, module_name: str = "custom_module"):
    """Dynamically load a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {file_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def run_tests(
    algorithm: Callable,
    test_cases: List[Dict[str, Any]],
    verbose: bool = True,
    show_timing: bool = False
) -> Dict[str, int]:
    """
    Run tests with the given algorithm and test cases.
    
    Args:
        algorithm: Function to test
        test_cases: List of test case dicts
        verbose: Print detailed output
        show_timing: Show execution time
    
    Returns:
        Summary dict with pass/fail counts
    """
    runner = TestRunner(algorithm, test_cases)
    return runner.run(verbose=verbose, show_timing=show_timing)


def run_from_files(
    algorithm_file: str,
    algorithm_name: str,
    test_cases_file: str,
    test_cases_name: str = "TEST_CASES",
    verbose: bool = True,
    show_timing: bool = False
) -> Dict[str, int]:
    """
    Run tests by loading algorithm and test cases from files.
    
    Args:
        algorithm_file: Path to file containing the algorithm
        algorithm_name: Name of the function in the algorithm file
        test_cases_file: Path to file containing test cases
        test_cases_name: Name of the test cases variable (default: TEST_CASES)
        verbose: Print detailed output
        show_timing: Show execution time
    
    Returns:
        Summary dict with pass/fail counts
    
    Example:
        run_from_files(
            algorithm_file="my_solution.py",
            algorithm_name="solve",
            test_cases_file="my_solution_test.py"
        )
    """
    # Load algorithm
    algo_module = load_module_from_file(algorithm_file, "algo_module")
    if not hasattr(algo_module, algorithm_name):
        raise AttributeError(
            f"Algorithm '{algorithm_name}' not found in {algorithm_file}")
    algorithm = getattr(algo_module, algorithm_name)

    # Load test cases
    test_module = load_module_from_file(test_cases_file, "test_module")
    if not hasattr(test_module, test_cases_name):
        raise AttributeError(
            f"Test cases '{test_cases_name}' not found in {test_cases_file}")
    test_cases = getattr(test_module, test_cases_name)

    return run_tests(algorithm, test_cases, verbose, show_timing)


def main():
    parser = argparse.ArgumentParser(description="Run algorithm tests")
    parser.add_argument(
        "--algorithm", "-a",
        required=True,
        help="Path to algorithm file"
    )
    parser.add_argument(
        "--function", "-f",
        required=True,
        help="Function name in algorithm file"
    )
    parser.add_argument(
        "--timing",
        action="store_true",
        help="Show execution time for each test"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only show summary, not individual test results"
    )

    args = parser.parse_args()

    # Derive test file from algorithm file: solution.py -> solution_test.py
    test_file = args.algorithm.replace(".py", "_test.py")

    try:
        result = run_from_files(
            algorithm_file=args.algorithm,
            algorithm_name=args.function,
            test_cases_file=test_file,
            verbose=not args.quiet,
            show_timing=args.timing
        )

        # Exit with error code if any tests failed
        sys.exit(0 if result["failed"] == 0 and result["errors"] == 0 else 1)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        sys.exit(1)
    except (ImportError, AttributeError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
