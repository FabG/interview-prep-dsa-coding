# 1.2 Contains Duplicate — LeetCode reference solution

- Problem: [description](problem-description.md)
- Problem source: [LeetCode Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- Status: captured from code supplied by the user as the LeetCode solution
- Exact solution URL: not provided
- Source type: not specified (submission, official editorial, or community solution)
- Author: not specified
- Captured date: October 25, 2026
- Acceptance status: not confirmed

## Explanation

Create a set containing the distinct values from `nums`. If the original list
has more elements than the set, at least one value was repeated. Return the
boolean result of that comparison.

- Time: O(n) on average for set construction; the length comparison is O(1).
- Auxiliary space: O(k) for k distinct values, or O(n) in the worst case.

## Reference code

Code supplied by the user:

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Idea: convert list to set to remove duplicates
        # and compare the size of the list and set - if they don't match we know there was a dup somewhere
        unique_nums = set(nums)
        return len(nums) > len(unique_nums)
```

## Comparison with my solution

The implementation uses the same set construction and length comparison as
[my solution](my-solution.py), with the same behavior and complexity. This
version omits the unreachable scaffold exception after the return statement.
