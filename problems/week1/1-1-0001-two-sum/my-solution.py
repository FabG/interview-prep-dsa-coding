"""Problem 1.1: Two Sum — my solution.

Source: https://leetcode.com/problems/two-sum/
Submission link: https://leetcode.com/problems/two-sum/post-solution/?submissionId=2181677682
Code provenance: pasted by the user from their submission; imported verbatim.
Status: guided solution; all 3 local problem examples pass
Submission date: 2026-10-25 (user-recorded)
Submission result: LeetCode acceptance not yet confirmed
Local verification: 2026-10-25 — 3 passed, 0 failed
Time spent: not recorded
Assistance used: AI guidance on pairs, Python syntax, hash maps and complexity
Next review: 2026-10-27 — re-solve without looking at the code

Approach and reasoning:
The current twoSum implementation scans nums once. A dictionary maps each
previously seen value to its index. For each value, look up target - value;
if present, return that stored index and the current index. Check before
inserting the current value so the same element cannot be used twice.
Python's dict implements a hash map. Equal values at different indices,
such as [3, 3], are handled correctly.

Time complexity (n = len(nums)):
- Current twoSum: O(n) average time, with average O(1) dictionary operations.
  Pathological hash collisions can make the worst case O(n^2).
- Pair-based twoSumSecond: O(n^2) worst-case time; at most n(n - 1) / 2 pairs.
- Original twoSumOri: O(n) time, but incorrect because it only checks prefix sums.

Auxiliary space:
- Current twoSum: O(n) for previously seen values and indices.
- Pair-based twoSumSecond: O(1), excluding the constant-size result.
- Original twoSumOri: O(n), because sum_list accumulates indices.
These costs describe the solution methods, not the local test harness.

Mistakes and lessons:
- A running total from the start misses pairs that exclude earlier elements.
  For [3, 2, 4], the prefix totals are 3, 5 and 9; the required pair is
  2 + 4 at indices [1, 2]. Examples 1 and 3 masked this mistake because
  their answers are the first two elements.
- Nested loops check each distinct pair when j starts at i + 1.
- A complement lookup trades O(n) extra space for O(n) average time.
- list.append changes the list and returns None; do not assign its return
  value back to the list.
- Keep return statements indented inside the function.
- Continue running later examples after an assertion or runtime failure.

Comparison with the agent solution: pending; reference not added yet.

Review history:
- 2026-10-25: guided implementation; all 3 local examples passed.
  Next: reconstruct the complement approach independently on 2026-10-27.

Run from the repository root:
    python3 problems/week1/1-1-0001-two-sum/my-solution.py

Keep local assertions outside the class. Submit the current solution method
and any required imports. Passing these examples does not confirm a LeetCode
submission or an independent re-solve.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

    def twoSumSecond(self, nums: list[int], target: int) -> list[int]:
        # updated: consider pairs of distinct indices independently.
        # Reset the sum for each pair rather than accumulating across the list.
        # O2 complexity
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise NotImplementedError("Add your twoSum implementation, then run this file again.")


    def twoSumOri(self, nums: list[int], target: int) -> list[int]:
        # original
        sum=0
        sum_list = []
        for index, value in enumerate(nums):
            sum += value
            sum_list.append(index)
            if sum == target:
                #print(sum_list)
                return sum_list
        raise NotImplementedError("Add your twoSum implementation, then run this file again.")


def run_examples() -> None:
    """Compare your results with the three examples from the problem."""
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    passed = 0
    failed = 0

    for number, (nums, target, expected) in enumerate(cases, start=1):
        try:
            actual = Solution().twoSum(nums.copy(), target)
            assert isinstance(actual, list), (
                f"expected a list of indices, got {actual!r}"
            )
            # LeetCode permits either ordering of the two indices.
            assert sorted(actual) == sorted(expected), (
                f"expected {expected} (either order), got {actual!r}"
            )
        except AssertionError as error:
            failed += 1
            print(f"Example {number} FAILED: {error}")
            print(f"  nums={nums}, target={target}")
        except Exception as error:
            # Isolate each test so a runtime error cannot hide later results.
            failed += 1
            print(f"Example {number} ERROR: {type(error).__name__}: {error}")
            print(f"  nums={nums}, target={target}, expected={expected}")
        else:
            passed += 1
            print(f"Example {number} PASSED: {actual}")

    print(f"\nResults: {passed} passed, {failed} failed, {len(cases)} total.")



if __name__ == "__main__":
    run_examples()
