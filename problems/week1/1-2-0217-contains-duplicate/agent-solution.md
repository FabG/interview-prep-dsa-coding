# 1.2 Contains Duplicate — Agent solution

- Problem: [description](problem-description.md)
- Author: Codex (agent-written explanation and code)
- Basis: the local problem description; no external solution consulted for this update
- Created: October 25, 2026
- Context: the agent had seen the user's code earlier in the conversation; this is not a blind independent attempt.
- Validation: local examples and additional edge cases; not submitted to LeetCode

## Approach

Scan the list while keeping a set of values already encountered. If the
current value is in the set, a duplicate has been found: return `True`
immediately. Otherwise add it and continue. Return `False` only after the
entire list has been checked without finding a repeat.

## Python solution

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()

        for value in nums:
            if value in seen:
                return True
            seen.add(value)

        return False
```

The input list is not modified. An early return avoids processing the rest of
the list once a duplicate is found.

## Why it works

Before each iteration, `seen` contains every distinct value from earlier
positions. Membership therefore means the current value has appeared before,
which proves a duplicate exists. If the loop finishes, each value was absent
when first checked, so every element is distinct.

## Complexity

- Time: O(n) on average for a full scan, using average O(1) set operations.
  A duplicate near the beginning allows O(1) best-case time.
- Auxiliary space: O(k) for k distinct values visited before returning,
  up to O(n) in the worst case.
- Pathological hash collisions can increase worst-case time to O(n²).

## Local validation

All three examples from the description pass. Additional cases checked:

| Input | Expected |
| --- | --- |
| `[7]` | `False` |
| `[0, 0]` | `True` |
| `[-1, 0, -1]` | `True` |
| `[-1000000000, 0, 1000000000]` | `False` |
