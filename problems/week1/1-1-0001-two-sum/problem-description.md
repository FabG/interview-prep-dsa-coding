# 1.1 Two Sum

- LeetCode problem: 1
- Difficulty: Easy
- Source: [Two Sum on LeetCode](https://leetcode.com/problems/two-sum/)
- Captured: October 25, 2026
- Language: Python

## Task

Given the integer list `nums` and integer `target`, identify two distinct positions whose values sum to the target. Return those positions, rather than the values. Either ordering of the two indices is acceptable.

Each input has exactly one valid pair. An index cannot be used twice, although the values at the two positions may be equal.

This description summarizes the linked LeetCode problem.

## Examples from LeetCode

| nums | target | Expected indices | Check |
| --- | --- | --- | --- |
| `[2, 7, 11, 15]` | `9` | `[0, 1]` | Positions 0 and 1 contain 2 and 7. |
| `[3, 2, 4]` | `6` | `[1, 2]` | Positions 1 and 2 contain 2 and 4. |
| `[3, 3]` | `6` | `[0, 1]` | Equal values occupy two distinct positions. |

## Input limits

- List length: 2 through 10,000, inclusive.
- Each list value: −1,000,000,000 through 1,000,000,000, inclusive.
- Target: the same integer range as the list values.
- Exactly one pair satisfies the requirement.

## Follow-up

Can your approach run faster than quadratic time, `O(n²)`?

## Workspace

- [My solution](my-solution.py)
- [Agent solution](agent-solution.md)
- [Progress tracker](../../../TRACKER.md)
