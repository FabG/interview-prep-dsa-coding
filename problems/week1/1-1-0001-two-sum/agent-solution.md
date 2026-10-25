# 1.1 Two Sum — Agent solution

- Problem: [description](problem-description.md)
- Author: Codex (agent-written explanation and code)
- Basis: the local problem description; no external solution consulted for this update
- Created: October 25, 2026
- Context: the agent had seen the user's code earlier in the conversation; this is not a blind independent attempt.
- Validation: local examples and additional edge cases; not submitted to LeetCode

## Approach

For each value, calculate the missing value needed to reach the target. Keep a
mapping from previously visited values to their indices. If the missing value
is already present, return its index and the current index. Otherwise record
the current value for subsequent iterations.

Look up the missing value before recording the current element. This ensures
we never pair an element with itself, while still allowing equal values at
different indices, such as `[3, 3]` with target `6`.

## Python solution

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        previous_indices: dict[int, int] = {}

        for index, value in enumerate(nums):
            needed = target - value
            if needed in previous_indices:
                return [previous_indices[needed], index]
            previous_indices[value] = index

        raise ValueError("No valid pair exists")
```

The final exception is defensive: the problem guarantees a valid pair, so it
will not be reached for valid input. The input list is not modified.

## Why it works

Before each iteration, the dictionary contains indices only from earlier
positions. Any returned pair therefore uses distinct indices and sums to the
target. When the later element of the valid pair is reached, the earlier
value is in the dictionary, so the lookup finds a solution. If a repeated
value replaces an older index, the replacement still identifies an earlier
element with the same value and is equally valid for a future pair.

## Complexity

- Time: O(n) on average, using average O(1) dictionary operations.
- Auxiliary space: O(n) in the worst case.
- Pathological hash collisions can increase worst-case time to O(n²).

## Local validation

All three examples from the description pass. Additional cases checked:

| Input | Target | Expected indices (either order) |
| --- | --- | --- |
| `[0, 4, 3, 0]` | `0` | `[0, 3]` |
| `[-3, 4, 3, 90]` | `0` | `[0, 2]` |
| `[2, 5, 5, 11]` | `10` | `[1, 2]` |
