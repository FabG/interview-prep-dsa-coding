"""Problem 1.2: Contains Duplicate — my solution.

Source: https://leetcode.com/problems/contains-duplicate/
Status: I — solved independently, as confirmed by the user; all 3 local examples pass
Submission link:
Submission date:
Submission result: LeetCode acceptance not yet confirmed
Local verification: 2026-10-25 — 3 passed, 0 failed
Time spent: not recorded
Assistance used: no solution hints needed, as confirmed by the user.
Python syntax discussion and test scaffolding are recorded separately from solving.
To review again?: No

Approach and reasoning:
Build unique_nums = set(nums), which retains one copy of each distinct value.
If nums is longer than unique_nums, at least one value appeared more than once;
otherwise all values were distinct. Return the length comparison as a boolean.
The original list is unchanged, and element order does not matter here.

Time complexity (n = len(nums)):
O(n) average time to build the set. Both len calls and the comparison are O(1).
Pathological hash collisions can make set construction O(n^2) in the worst case.
The current implementation processes the entire list before comparing lengths.

Auxiliary space:
O(k), where k is the number of distinct values; O(n) in the worst case.
These costs describe containsDuplicate, not the local test harness.

Mistakes and lessons:
- set(nums) removes duplicate values in a new collection.
- Sets do not preserve list order; this problem only needs the distinct count.
- A comparison already returns True or False, so it can be returned directly.
- The scaffold's raise after return is unreachable and can be removed.

Comparison with the supplied LeetCode solution:
Same set construction and length comparison; identical behavior and complexity.
Captured in agent-solution.md from user-provided code; exact source URL and
acceptance status were not provided. The supplied version omits the unreachable
scaffold exception after return.
Review history:
- 2026-10-25: independently solved, as confirmed by the user; all 3 examples passed.
  Compared with the user-supplied LeetCode solution: same algorithm.
  No further review requested.

Run from the repository root:
    python3 problems/week1/1-2-0217-contains-duplicate/my-solution.py

Each example runs even if an earlier example fails or raises an error.
Run without -O, which disables assertions. Submit the Solution class and
any required imports to LeetCode; keep the local harness here.
Passing these examples does not confirm a LeetCode acceptance.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Idea: convert list to set to remove duplicates
        # and compare the size of the list and set - if they don't match we know there was a dup somewhere
        unique_nums = set(nums)
        return len(nums) > len(unique_nums)
        raise NotImplementedError("Add your containsDuplicate implementation, then run this file again.")


def run_examples() -> None:
    """Compare your results with the three examples from the problem."""
    cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
    passed = 0
    failed = 0

    for number, (nums, expected) in enumerate(cases, start=1):
        try:
            actual = Solution().containsDuplicate(nums.copy())
            assert isinstance(actual, bool), (
                f"expected a bool, got {actual!r}"
            )
            assert actual == expected, (
                f"expected {expected}, got {actual!r}"
            )
        except AssertionError as error:
            failed += 1
            print(f"Example {number} FAILED: {error}")
            print(f"  nums={nums}, expected={expected}")
        except Exception as error:
            failed += 1
            print(f"Example {number} ERROR: {type(error).__name__}: {error}")
            print(f"  nums={nums}, expected={expected}")
        else:
            passed += 1
            print(f"Example {number} PASSED: {actual}")

    print(f"\nResults: {passed} passed, {failed} failed, {len(cases)} total.")


if __name__ == "__main__":
    run_examples()
