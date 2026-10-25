"""Problem 1.3: Valid Anagram — my solution.

Source: https://leetcode.com/problems/valid-anagram/
Status: I — solved independently without hints, as confirmed by the user
Submission link:
Submission date:
Submission result: LeetCode acceptance not yet confirmed
Local verification: 2026-10-25 — 2 passed, 0 failed
Time spent: not recorded
Assistance used: problem description and test scaffold only; no solution hints
To review again?: No

Approach and reasoning:
Sort each string's characters, join them into strings, and compare the results.
Anagrams contain the same characters with the same multiplicities, so sorting
produces identical strings exactly when the inputs are anagrams. Repeated
characters are preserved. The original strings are unchanged.

Time complexity (n = len(s), m = len(t)):
O(n log n + m log m) worst-case time for sorting. Joining takes O(n + m),
and comparison takes at most O(min(n, m)), so sorting dominates.
For equal-length strings this simplifies to O(n log n).

Auxiliary space:
O(n + m) for the sorted character lists, sorting workspace, and joined strings.
These costs describe isAnagram, not the local test harness.

Mistakes and lessons:
- sorted() returns a list of characters; join() builds a string from that list.
- Equality checks both character values and their multiplicities after sorting.
- Keep the method named isAnagram to match LeetCode and the local runner.
- Removed the unreachable scaffold exception after return.

Comparison with the agent solution:
My approach sorts strings; the agent uses 26 character counters for the fixed
lowercase alphabet, taking O(n + m) time and O(1) auxiliary space.
See agent-solution.md for the counting implementation and Unicode follow-up.
Review history:
- 2026-10-25: independently completed without hints; both local examples passed.

Run from the repository root:
    python3 problems/week1/1-3-0242-valid-anagram/my-solution.py

Each example runs even if an earlier example fails or raises an error.
Run without -O, which disables assertions. Submit the Solution class and
any required imports to LeetCode; keep the local harness here.
Passing these examples does not confirm LeetCode acceptance.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings to compare their characters and multiplicities.
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        return s_sorted == t_sorted


def run_examples() -> None:
    """Compare results with the two examples from the problem."""
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]
    passed = 0
    failed = 0

    for number, (s, t, expected) in enumerate(cases, start=1):
        try:
            actual = Solution().isAnagram(s, t)
            assert isinstance(actual, bool), f"expected a bool, got {actual!r}"
            assert actual == expected, f"expected {expected}, got {actual!r}"
        except AssertionError as error:
            failed += 1
            print(f"Example {number} FAILED: {error}")
            print(f"  s={s!r}, t={t!r}, expected={expected}")
        except Exception as error:
            failed += 1
            print(f"Example {number} ERROR: {type(error).__name__}: {error}")
            print(f"  s={s!r}, t={t!r}, expected={expected}")
        else:
            passed += 1
            print(f"Example {number} PASSED: {actual}")

    print(f"\nResults: {passed} passed, {failed} failed, {len(cases)} total.")


if __name__ == "__main__":
    run_examples()
