"""Problem 2.1: Valid Palindrome — my solution.

Source: https://leetcode.com/problems/valid-palindrome/
Status: implemented; completion outcome not recorded
Submission link:
Submission date:
Submission result: not submitted
Time spent:
Assistance used: problem scaffold and Python syntax guidance on isalnum(),
lower() and reverse slicing; AI complexity review.
To review again?: No — update after the attempt

Approach and reasoning:
Keep only alphanumeric characters and convert them to lowercase. Copy the first
half and the equally sized last half, reverse the last half, and compare them.
For odd lengths the middle character needs no comparison. Return True when the
cleaned string contains zero or one character.

Time complexity (n = len(s), m = len(cleaned), m <= n):
O(n). Filtering scans the input; joining, lowercasing, copying halves, reversing
and comparing take O(m) each. These operations are sequential, so their costs
add to O(n + m) = O(n), rather than multiplying.

Auxiliary space:
O(n) in the worst case. The cleaned string, temporary construction storage,
copied halves and reversed second half use O(m) space in total. Constant factors
from multiple copies do not change the linear bound. The returned bool is O(1).
These costs describe isPalindrome, not the local test harness.
Mistakes and lessons:
Comparison with the agent solution: pending.
Review history:
- 2026-11-13: existing local checks — 8 passed, 0 failed.

Run from the repository root:
    python3 problems/week2/2-1-0125-valid-palindrome/my-solution.py

Each case runs even if an earlier case fails. Run without -O, which disables
assertions. Submit only the Solution class and required imports to LeetCode.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumerical characters and lower
        cleaned = "".join(char for char in s if char.isalnum()).lower()
        first_half_cleaned = cleaned[: len(cleaned) // 2]
        second_half_cleaned = cleaned[-len(first_half_cleaned):]
        # reverse second half
        reverse_second_half_cleaned = second_half_cleaned[::-1]
        return first_half_cleaned == reverse_second_half_cleaned if len(cleaned) > 1 else True


def run_examples() -> None:
    """Run three source examples and additional local edge cases."""
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        # Additional local cases, not quoted LeetCode examples.
        ("0P", False),
        ("a", True),
        (".,!", True),
        ("1a2A1", True),
        ("ab", False),
    ]
    passed = 0
    failed = 0
    for number, (s, expected) in enumerate(cases, start=1):
        try:
            actual = Solution().isPalindrome(s)
            assert isinstance(actual, bool), f"expected a bool, got {actual!r}"
            assert actual == expected, f"expected {expected}, got {actual!r}"
        except AssertionError as error:
            failed += 1
            print(f"Case {number} FAILED: {error}")
            print(f"  s={s!r}")
        except Exception as error:
            failed += 1
            print(f"Case {number} ERROR: {type(error).__name__}: {error}")
            print(f"  s={s!r}, expected={expected}")
        else:
            passed += 1
            print(f"Case {number} PASSED: {actual}")
    print(f"\nResults: {passed} passed, {failed} failed, {len(cases)} total.")


if __name__ == "__main__":
    run_examples()
