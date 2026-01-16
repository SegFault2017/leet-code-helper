#!/usr/bin/env python3
"""
Generic test runner that works with any algorithm and test cases.

Usage:
    from test_runner import TestRunner
    
    runner = TestRunner(algorithm_func, test_cases)
    runner.run()
"""

from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import time


class TestStatus(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"


@dataclass
class TestResult:
    name: str
    status: TestStatus
    expected: Any
    actual: Any
    error: Optional[str] = None
    execution_time: float = 0.0


class TestRunner:
    """
    Generic test runner for algorithm testing.
    
    Args:
        algorithm: Function to test
        test_cases: List of test case dicts with 'name', 'input', 'expected'
        comparator: Optional custom comparison function (default: ==)
        normalizer: Optional function to normalize output before comparison
    """

    def __init__(
        self,
        algorithm: Callable,
        test_cases: List[Dict[str, Any]],
        comparator: Optional[Callable[[Any, Any], bool]] = None,
        normalizer: Optional[Callable[[Any], Any]] = None
    ):
        self.algorithm = algorithm
        self.test_cases = test_cases
        self.comparator = comparator or self._default_comparator
        self.normalizer = normalizer or self._default_normalizer
        self.results: List[TestResult] = []

    @staticmethod
    def _default_comparator(expected: Any, actual: Any) -> bool:
        """Default comparison using equality."""
        return expected == actual

    @staticmethod
    def _default_normalizer(value: Any) -> Any:
        """Default normalizer - convert lists to sets for unordered comparison."""
        if isinstance(value, list):
            try:
                return set(value)
            except TypeError:
                return value
        return value

    def run_single(self, test_case: Dict[str, Any]) -> TestResult:
        """Run a single test case."""
        name = test_case["name"]
        input_data = test_case["input"]
        expected = test_case["expected"]

        try:
            start_time = time.perf_counter()

            # Handle both single input and multiple inputs
            if isinstance(input_data, dict) and "_args" in input_data:
                result = self.algorithm(*input_data["_args"])
            elif isinstance(input_data, dict) and "_kwargs" in input_data:
                result = self.algorithm(**input_data["_kwargs"])
            else:
                result = self.algorithm(input_data)

            execution_time = time.perf_counter() - start_time

            # Normalize outputs
            normalized_result = self.normalizer(result)
            normalized_expected = self.normalizer(expected)

            # Compare
            if self.comparator(normalized_expected, normalized_result):
                return TestResult(
                    name=name,
                    status=TestStatus.PASS,
                    expected=expected,
                    actual=result,
                    execution_time=execution_time
                )
            else:
                return TestResult(
                    name=name,
                    status=TestStatus.FAIL,
                    expected=expected,
                    actual=result,
                    execution_time=execution_time
                )

        except Exception as e:
            return TestResult(
                name=name,
                status=TestStatus.ERROR,
                expected=expected,
                actual=None,
                error=str(e)
            )

    def run(self, verbose: bool = True, show_timing: bool = False) -> Dict[str, int]:
        """
        Run all test cases.
        
        Args:
            verbose: Print detailed output for each test
            show_timing: Show execution time for each test
        
        Returns:
            Summary dict with 'passed', 'failed', 'errors', 'total'
        """
        self.results = []

        print("=" * 60)
        print("RUNNING TESTS")
        print("=" * 60)
        print()

        for i, test_case in enumerate(self.test_cases, 1):
            result = self.run_single(test_case)
            self.results.append(result)

            if verbose:
                self._print_result(i, result, show_timing)

        return self._print_summary()

    def _print_result(self, index: int, result: TestResult, show_timing: bool):
        """Print a single test result."""
        status_symbols = {
            TestStatus.PASS: "✓",
            TestStatus.FAIL: "✗",
            TestStatus.ERROR: "⚠"
        }

        symbol = status_symbols[result.status]
        timing = f" ({result.execution_time*1000:.2f}ms)" if show_timing else ""

        print(
            f"Test {index:2d}: {symbol} {result.status.value} - {result.name}{timing}")

        if result.status == TestStatus.FAIL:
            print(f"         Expected: {result.expected}")
            print(f"         Actual:   {result.actual}")
        elif result.status == TestStatus.ERROR:
            print(f"         Error: {result.error}")

    def _print_summary(self) -> Dict[str, int]:
        """Print test summary and return counts."""
        passed = sum(1 for r in self.results if r.status == TestStatus.PASS)
        failed = sum(1 for r in self.results if r.status == TestStatus.FAIL)
        errors = sum(1 for r in self.results if r.status == TestStatus.ERROR)
        total = len(self.results)

        print()
        print("=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"Passed:  {passed}/{total}")
        print(f"Failed:  {failed}/{total}")
        print(f"Errors:  {errors}/{total}")

        if passed == total:
            print("\n🎉 All tests passed!")
        else:
            print(f"\n❌ {failed + errors} test(s) did not pass")

        return {
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "total": total
        }

    def get_failures(self) -> List[TestResult]:
        """Return list of failed/errored tests."""
        return [r for r in self.results if r.status != TestStatus.PASS]
