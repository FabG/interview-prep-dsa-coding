"""Problem 1.5: Product of Array Except Self — my solution.

Source: https://leetcode.com/problems/product-of-array-except-self/
Status: P — partial; 6/6 local cases pass, but O(n) time requirement not met
Submission link:
Submission date:
Submission result: LeetCode acceptance not confirmed
Local verification: 2026-11-01 — 6 passed, 0 failed
Time spent:
Assistance used: scaffold and AI complexity review; agent reference available.
Whether the reference was used for implementation is not recorded.
To review again?: Yes — optimize to meet O(n) time

Approach and reasoning:
For each position, create slices of the values before and after it, calculate
those products with math.prod, and append their product to the output list.

Time complexity (n = len(nums)):
O(n^2). Each of n iterations copies and scans up to n - 1 values in slices.
The repeated slicing and multiplication are linear per iteration, so this
implementation does not meet the required O(n) time bound.

Auxiliary space:
O(n) peak extra space, excluding output, because slicing creates temporary lists.
Output space is O(n), and total peak extra space including output is still O(n).
Temporary slices are released between operations; O(n^2) cumulative copying
across the run does not imply O(n^2) simultaneously live memory.
These bounds use the problem's bounded arithmetic model and exclude the harness.
Constraint: do not use division.
Mistakes and lessons:
Comparison with the agent solution:
The agent reuses running prefix/suffix products in two passes: O(n) time and
O(1) auxiliary space excluding output, avoiding repeated slices and scans.
Review history:
- 2026-11-01: all 6 local cases pass; complexity review identified required optimization.

Run from the repository root:
    python3 problems/week1/1-5-0238-product-of-array-except-self/my-solution.py

Each case runs even if an earlier case fails. Run without -O, which disables
assertions. Submit only the Solution class and required imports to LeetCode.
These checks verify outputs, not runtime complexity or the no-division rule.
"""

import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        sum_list = list()
        for i in range(len(nums)):
            if i > 0 and i < len(nums):
                prod_i = math.prod(nums[:i]) * math.prod(nums[i + 1:])
            elif i == 0:
                prod_i = math.prod(nums[i + 1:])
            else:
                prod_i = math.prod(nums[:i])
            sum_list.append(prod_i)

            #left_product = math.prod(nums[:i]) if i > 0 else 1
            #right_product = math.prod(nums[i + 1:]) if i < len(nums) - 1 else 1
            #sum_list.append(left_product * right_product)
        return sum_list
        raise NotImplementedError("Add your productExceptSelf implementation, then run this file again.")


def run_examples() -> None:
    """Run two source examples and additional local edge cases."""
    cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        # Additional local cases, not quoted LeetCode examples.
        ([2, 3], [3, 2]),
        ([0, 2, 0], [0, 0, 0]),
        ([-1, -2, -3], [6, 3, 2]),
        ([1, 1, 1], [1, 1, 1]),
    ]
    passed = 0
    failed = 0
    for number, (nums, expected) in enumerate(cases, start=1):
        try:
            actual = Solution().productExceptSelf(nums.copy())
            assert isinstance(actual, list), f"expected a list, got {actual!r}"
            assert all(type(value) is int for value in actual), (
                f"expected integer results, got {actual!r}"
            )
            assert actual == expected, f"expected {expected!r}, got {actual!r}"
        except AssertionError as error:
            failed += 1
            print(f"Case {number} FAILED: {error}")
            print(f"  nums={nums!r}")
        except Exception as error:
            failed += 1
            print(f"Case {number} ERROR: {type(error).__name__}: {error}")
            print(f"  nums={nums!r}, expected={expected!r}")
        else:
            passed += 1
            print(f"Case {number} PASSED: {actual!r}")
    print(f"\nResults: {passed} passed, {failed} failed, {len(cases)} total.")


if __name__ == "__main__":
    run_examples()
